const themeKey = "theme";
const darkTheme = "dark";
const lightTheme = "light";
const darkIcon = document.querySelector("#dark-icon");
const lightIcon = document.querySelector("#light-icon");
const setIcons = (theme) => {
  if (theme === darkTheme) {
    darkIcon.classList.remove("hidden")
    lightIcon.classList.add("hidden")
  } else {
    lightIcon.classList.remove("hidden")
    darkIcon.classList.add("hidden")
  }
}
const setTheme = (theme) => {
  setIcons(theme)
  if (theme === darkTheme) {
    document.firstElementChild.classList.add("dark");
  } else {
    document.firstElementChild.classList.remove("dark")
  }
  localStorage.setItem(themeKey, theme);
}
const initTheme = () => {
  let theme = localStorage.getItem(themeKey) || darkTheme;
  setIcons(theme);
  setTheme(theme);
}
const addToggleTheme = () => {
  let btn = document.querySelector("#theme-changer")
  btn.addEventListener("click", () => {
    let theme = localStorage.getItem(themeKey) || darkTheme;
    let newTheme = theme === darkTheme ? lightTheme : darkTheme;
    setTheme(newTheme);
  });
}
initTheme();
addToggleTheme();
