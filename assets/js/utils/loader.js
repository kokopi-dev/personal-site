const hideLoader = () => {
  let hideCss = ["-z-10", "invisible", "absolute"]
  let loader = document.querySelector("#loader");
  let mainContent = document.querySelector("#main-content");
  loader.classList.add(...hideCss);
  loader.classList.remove("grid")
  mainContent.classList.remove("hidden")
  mainContent.classList.add("grid")
  setTimeout(() => {
    loader.classList.add("hidden")
  }, 0);
};
document.addEventListener('DOMContentLoaded', function() {
  setTimeout(hideLoader, 600);
});
