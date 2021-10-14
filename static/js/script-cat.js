const button = document.getElementById("button")
const img = document.querySelector(".cat-img")
button.addEventListener("click", () => {
    let xhr = new XMLHttpRequest();
    xhr.open("GET", "https://api.thecatapi.com/v1/images/search")

    xhr.addEventListener("load", (data) => {
        const datosJSON = JSON.parse(data.target.response);
        const cat_img = datosJSON[0].url
        button.textContent = "Cargando...";
        img.setAttribute("src", cat_img)
        button.textContent = "Otro Gato"
    })
    xhr.send();
})