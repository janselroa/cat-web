const card = document.querySelector(".card-cat");
const button = document.getElementById("button");
const getCats = () => {
    let xhr = new XMLHttpRequest();
    xhr.open("GET", "https://api.thecatapi.com/v1/images/search?limit=5")
    xhr.addEventListener("load", (data) => {
        const datosJSON = JSON.parse(data.target.response);
        for (let i of datosJSON) {
            console.log(i.url)
            const img = document.createElement("img")
            img.setAttribute("src", i.url)
            card.appendChild(img)
        }
    });
    xhr.send();

}
getCats()
button.addEventListener("click", () => {
    getCats();
})