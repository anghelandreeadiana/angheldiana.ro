/* Interacțiuni discrete: meniu mobil și deschiderea întrebării din URL. */
(function () {
  "use strict";

  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("nav");
  if (!toggle || !nav) return;

  function setOpen(open) {
    nav.setAttribute("data-open", open ? "true" : "false");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    toggle.querySelector(".label").textContent = open ? "Închide" : "Meniu";
    document.body.classList.toggle("nav-open", open && window.innerWidth <= 1080);
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

  document.addEventListener("click", function (event) {
    if (nav.getAttribute("data-open") !== "true") return;
    if (!nav.contains(event.target) && !toggle.contains(event.target)) setOpen(false);
  });

  nav.addEventListener("click", function (event) {
    if (event.target.closest("a")) setOpen(false);
  });

  window.addEventListener("resize", function () {
    if (window.innerWidth > 1080) setOpen(false);
  });

  function openTargetedQuestion() {
    if (!window.location.hash) return;
    var target = document.getElementById(window.location.hash.slice(1));
    if (target && target.tagName === "DETAILS") target.open = true;
  }

  openTargetedQuestion();
  window.addEventListener("hashchange", openTargetedQuestion);
})();
