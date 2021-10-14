const menu = document.querySelector(".menu");
const barra = document.querySelector(".barra")
barra.addEventListener("click", () => {
    menu.classList.toggle("menu-desplegado")
})