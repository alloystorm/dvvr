document.addEventListener("DOMContentLoaded", function() {
  const searchInput = document.getElementById("supportSearch");
  if (!searchInput) return;

  searchInput.addEventListener("input", function(e) {
    const query = e.target.value.toLowerCase().trim();

    // Select all FAQ sections (the injected data-driven ones)
    const sections = document.querySelectorAll(".section:not(#contact)");
    
    sections.forEach(section => {
      let sectionHasVisibleItems = false;
      
      // Each section has headers and grids
      // We will look at each .faq-grid and its preceding <h3>
      const subHeaders = section.querySelectorAll("h3");
      
      subHeaders.forEach(header => {
        const grid = header.nextElementSibling;
        if (!grid || !grid.classList.contains("faq-grid")) return;
        
        let gridHasVisibleItems = false;
        const items = grid.querySelectorAll(".faq-item");
        
        items.forEach(item => {
          const text = item.textContent.toLowerCase();
          if (query === "" || text.includes(query)) {
            item.style.display = "";
            gridHasVisibleItems = true;
            sectionHasVisibleItems = true;
          } else {
            item.style.display = "none";
          }
        });
        
        // Hide/show the header depending on if the grid has visible items
        if (gridHasVisibleItems) {
          header.style.display = "";
          grid.style.display = "";
        } else {
          header.style.display = "none";
          grid.style.display = "none";
        }
      });
      
      // Hide/show the entire section depending on if it has any visible items
      const headerDiv = section.querySelector(".editions-header");
      if (sectionHasVisibleItems) {
        section.style.display = "";
      } else {
        // Only hide if we have actually processed grids (to avoid hiding Support Hub randomly if it doesn't have faq-grids)
        const hasGrids = section.querySelectorAll(".faq-grid").length > 0;
        if (hasGrids) {
          section.style.display = "none";
        }
      }
    });
  });
});
