document.addEventListener("DOMContentLoaded", function(){
    document.getElementById("burger").addEventListener("click", function(){
        document.querySelector("header").classList.toggle("open")
    })
})

// Закрыть меню на ESC
window.addEventListener('keydown', (e) => {
    if(e.key == "Escape"){
        document.querySelector(".header").classList.remove("open")
    }
});