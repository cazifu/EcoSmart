// ===== DASHBOARD FUNCTIONALITY =====

document.addEventListener("DOMContentLoaded", () => {
  initializeSidebar();
  highlightActiveMenu();
  initializeUserDropdown();
  initializeSmoothScroll();
});

// ===== SIDEBAR TOGGLE =====
function initializeSidebar() {
  const toggleBtn = document.getElementById("toggle-btn");
  const sidebar = document.getElementById("sidebar");
  const main = document.querySelector("main");

  if (toggleBtn && sidebar && main) {
    toggleBtn.addEventListener("click", () => {
      sidebar.classList.toggle("collapsed");
      main.classList.toggle("sidebar-collapsed");
    });
  }
}

// ===== MENU ITEM ACTIVE STATE =====
function highlightActiveMenu() {
  const currentPath = window.location.pathname;
  document.querySelectorAll(".menu-item").forEach((item) => {
    const href = item.getAttribute("href");
    item.classList.toggle(
      "active",
      href && (currentPath === href || currentPath.startsWith(href))
    );
  });
}

// ===== SMOOTH SCROLL =====
function initializeSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", (e) => {
      e.preventDefault();
      const target = document.querySelector(anchor.getAttribute("href"));
      if (target) target.scrollIntoView({ behavior: "smooth" });
    });
  });
}

// ===== USER DROPDOWN =====
function initializeUserDropdown() {
  const userAvatar = document.querySelector(".user-avatar");
  const userMenuBtn = document.querySelector(".user-menu-btn");
  const userDropdown = document.querySelector(".user-dropdown");

  // Support both avatar and button clicks
  const trigger = userAvatar || userMenuBtn;

  if (!trigger || !userDropdown) return;

  trigger.addEventListener("click", (e) => {
    e.stopPropagation();
    userDropdown.classList.toggle("active");
  });

  document.addEventListener("click", (e) => {
    if (!trigger.contains(e.target) && !userDropdown.contains(e.target))
      userDropdown.classList.remove("active");
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") userDropdown.classList.remove("active");
  });
}

