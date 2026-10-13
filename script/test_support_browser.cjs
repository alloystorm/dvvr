/* Exercise the rendered Jekyll pages. Requires a running local site and Playwright. */
const assert = require("node:assert/strict");
const { existsSync } = require("node:fs");
const { chromium } = require("playwright");
const base = process.env.SUPPORT_BASE_URL || "http://localhost:4000";

(async () => {
  const executablePath = process.env.SUPPORT_CHROMIUM_PATH ||
    (existsSync("/usr/bin/chromium") ? "/usr/bin/chromium" : undefined);
  const browser = await chromium.launch({ executablePath, headless: true, args: ["--no-sandbox"] });
  try {
    const page = await browser.newPage();
    // Keep verification local; analytics and other third-party requests are unrelated.
    await page.route("**/*", route => new URL(route.request().url()).origin === new URL(base).origin
      ? route.continue() : route.abort());
    const errors = [];
    page.on("pageerror", error => errors.push(error.message));
    await page.goto(base + "/dancexr/support.html");
    const visible = () => page.locator(".support-item:visible");
    await page.waitForSelector(".support-controls:visible");
    assert.equal(await visible().count(), 39);
    assert.equal(await page.locator('[data-category="camera"][aria-pressed]').isVisible(), true);

    await page.locator("#supportSearch").fill("HDRI");
    assert.equal(await visible().count(), 1);
    assert.equal(await visible().first().getAttribute("id"), "support-change-sky-map");
    await page.locator("#supportSearch").fill("portrait landscape");
    assert.equal(await visible().count(), 1);
    assert.equal(await visible().first().getAttribute("id"), "support-record-without-creator");
    await visible().first().locator("summary").click();
    assert.ok((await visible().first().locator(".support-answer").textContent()).includes("Apply Resolution"));
    await page.locator("#supportSearch").fill("augmented reality");
    assert.equal(await visible().count(), 1);
    assert.equal(await visible().first().getAttribute("id"), "support-start-mobile-ar");
    await page.locator("#supportSearch").fill("");

    await page.locator("#supportSearch").fill("inverse kinematics");
    assert.equal(await visible().count(), 1, "aliases must match even without the phrase in the answer");
    assert.equal(await visible().first().getAttribute("id"), "support-model-ik-2026-5-6");
    await page.locator("#supportSearch").fill("hair prepass");
    assert.equal(await visible().count(), 1, "words may match across question and answer");
    assert.equal(await visible().first().getAttribute("id"), "support-transparent-hair");
    await page.locator("#supportSearch").fill("VR");
    assert.ok((await visible().first().locator(".support-question").textContent()).toLowerCase().includes("vr"), "question matches rank above answer-only matches");
    await page.locator("#supportSearch").fill("");

    await page.locator('[data-category="actors"][aria-pressed]').click();
    assert.equal(await visible().count(), 4);
    await page.locator("#supportType").selectOption("known-issue");
    assert.equal(await visible().count(), 0);
    assert.equal(await page.locator(".support-empty").isVisible(), true);
    assert.equal(await page.locator('[data-category="motion"][aria-pressed] [data-category-count]').textContent(), "2");
    await page.locator(".support-reset").click();
    assert.equal(await visible().count(), 39);
    assert.equal(await page.locator("#supportSearch").evaluate(element => element === document.activeElement), true);
    await page.locator("#supportSearch").fill("no-such-answer-12345");
    assert.equal(await page.locator(".support-empty").isVisible(), true);
    await page.evaluate(() => { window.location.hash = "support-white-model"; });
    await page.waitForSelector("#support-white-model[open]");
    assert.equal(await page.locator("#supportSearch").inputValue(), "");
    assert.equal(await visible().count(), 39, "a linked answer clears filters that would hide it");
    assert.equal(await page.locator("#contact").isVisible(), true);

    await page.goto(base + "/dancexr/support.html#support-find-log-files");
    await page.waitForSelector("#support-find-log-files[open]");
    assert.ok((await page.locator("#support-find-log-files pre").first().textContent()).includes("C:\\Users\\[User]\\AppData"));
    await page.setViewportSize({ width: 390, height: 844 });
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth), true, "mobile page must not overflow");

    const localeQueries = { jp: "拡張現実", zh: "增强现实", tw: "擴增實境", kr: "증강 현실" };
    const localeScripts = { jp: /[ぁ-んァ-ヶ一-龥]/, zh: /[一-龥]/, tw: /[一-龥]/, kr: /[가-힣]/ };
    const englishQuestions = await page.locator(".support-question").allTextContents();
    for (const locale of ["jp", "zh", "tw", "kr"]) {
      await page.goto(`${base}/${locale}/dancexr/support.html`);
      await page.waitForSelector(".support-controls:visible");
      assert.equal(await visible().count(), 39);
      const questions = await page.locator(".support-question").allTextContents();
      const answers = await page.locator(".support-answer-content").allTextContents();
      questions.forEach(question => {
        assert.ok(localeScripts[locale].test(question), `${locale}: question must use the local language`);
        assert.ok(!englishQuestions.includes(question), `${locale}: English fallback question`);
      });
      answers.forEach(answer => assert.ok(localeScripts[locale].test(answer), `${locale}: answer must use the local language`));
      const guideLabels = await page.locator(".support-answer > ul a").allTextContents();
      guideLabels.forEach(label => assert.ok(localeScripts[locale].test(label), `${locale}: guide label must use the local language`));
      await page.locator("#supportSearch").fill(localeQueries[locale]);
      assert.equal(await visible().count(), 1, `${locale}: local-language alias search`);
      assert.equal(await visible().first().getAttribute("id"), "support-start-mobile-ar");
      await page.locator(".support-reset").click();
      assert.notEqual(await page.locator('label[for="supportSearch"]').textContent(), "Find an answer");
      await page.locator("#supportSearch").fill("Player.log");
      assert.ok(await visible().count() > 0);
      await page.locator(".support-reset").click();
      assert.equal(await visible().count(), 39);
    }
    assert.deepEqual(errors, [], "all language pages should run without JavaScript errors");

    // Direct localized links must remain localized on the first visit, even in an English browser.
    for (const locale of ["jp", "zh", "tw", "kr"]) {
      const fresh = await browser.newContext({ locale: "en-US" });
      await fresh.route("**/*", route => new URL(route.request().url()).origin === new URL(base).origin
        ? route.continue() : route.abort());
      const direct = await fresh.newPage();
      await direct.goto(`${base}/${locale}/dancexr/support.html#support-change-sky-map`);
      await direct.waitForSelector("#support-change-sky-map[open]");
      assert.ok(new URL(direct.url()).pathname.startsWith(`/${locale}/`), `${locale}: explicit locale must not redirect to English`);
      assert.ok(localeScripts[locale].test(await direct.locator("#support-change-sky-map .support-question").textContent()));
      assert.equal(await direct.evaluate(() => localStorage.getItem("dvvr-lang")), locale);
      await fresh.close();
    }

    const noJs = await browser.newContext({ javaScriptEnabled: false });
    const fallback = await noJs.newPage();
    await fallback.goto(base + "/dancexr/support.html");
    assert.equal(await fallback.locator(".support-item").count(), 39);
    assert.equal(await fallback.locator(".support-controls").isVisible(), false);
    await fallback.locator("#support-white-model summary").click();
    assert.equal(await fallback.locator("#support-white-model .support-answer").isVisible(), true);
    await noJs.close();
    console.log("Support browser passed: aliases, word search, ranking, combined filters, counts, empty/reset, links, mobile, five locales and no-JS access.");
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
