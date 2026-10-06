---
layout: release
title: Google Drive Integration
locale: en-US
---

# Google Drive Integration

DanceXR can synchronize content from a shared Google Drive folder to the device's content library. This is useful on Quest or Android when you manage the source files on another device.

## Link and download a folder

1. Put the content you want to import into a Google Drive folder. Organize actor, motion and other packages so you can identify what is being downloaded.
2. Make that folder accessible through its sharing link. DanceXR's folder downloader does not sign into your Google account; a restricted folder cannot be read through this flow.
3. In DanceXR's content/download menu, select **Link Google Drive**.
4. Enter the folder's share URL or its folder ID. A short URL that redirects to the folder link can also be used.
5. Select the linked folder to start synchronization. Watch its status until the download finishes, then open the corresponding content browser to load an item.

Keep the linked folder available when synchronizing again. Downloaded models still need to follow the supported [content-library formats](../preparecontent); receiving a file does not guarantee it is a usable actor or motion.

## If synchronization fails

Check the folder sharing permission and link first, then the device's connection and available storage. If the downloader offers **Retry**, retry after correcting the cause. Google can also restrict downloads; a transient failure does not necessarily mean the model package is broken. Avoid repeatedly restarting a blocked download.

For a package that downloads but will not load, use the normal [content preparation guide](../preparecontent) to check its format, archive structure and accompanying textures.

{% include video id="N7o0CdbFvD4" provider="youtube" %}
