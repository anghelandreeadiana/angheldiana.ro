/* Meniul pentru ecrane mici. Singurul script din site. */
(function () {
  "use strict";

  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("nav");
  if (!toggle || !nav) return;

  function setOpen(open) {
    nav.setAttribute("data-open", open ? "true" : "false");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    toggle.querySelector(".label").textContent = open ? "Închide" : "Meniu";
  }

  toggle.addEventListener("click", function () {
    setOpen(nav.getAttribute("data-open") !== "true");
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && nav.getAttribute("data-open") === "true") {
      setOpen(false);
      toggle.focus();
    }
  });

  window.addEventListener("resize", function () {
    if (window.innerWidth > 900) setOpen(false);
  });
})();
