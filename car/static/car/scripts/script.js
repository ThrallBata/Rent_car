document.getElementById('menu-home').onclick = function () {
    document.getElementById('main').scrollIntoView({behavior: "smooth"});
}

document.getElementById('menu-car').onclick = function () {
    document.getElementById('cars').scrollIntoView({behavior: "smooth"});
}

document.getElementById('menu-price').onclick = function () {
    document.getElementById('price').scrollIntoView({behavior: "smooth"});
}


document.getElementById("main-action").onclick = function () {
    document.getElementById("cars").scrollIntoView({behavior: "smooth"});
}

let buttons = document.getElementsByClassName("car-button");
for (let i = 0; i < buttons.length; i++) {
    buttons[i].onclick = function () {
        document.getElementById("price").scrollIntoView({behavior: "smooth"});
    }
}


document.addEventListener("DOMContentLoaded", function () {
    let layer = document.querySelector('.price-image');
    document.addEventListener('mousemove', (event) => {
        layer.style.transform = 'translate3d(' + ((event.clientX * 0.1) / 10) + 'px,' + ((event.clientY * 0.2) / 10) + 'px,0px)';
    });

    const elem = document.querySelector(".main");
    document.addEventListener('scroll', () => {
        elem.style.backgroundPositionX = '0' + (0.15 * window.pageYOffset) + 'px';
    })
});


/*150 strok za 20/01/2023 le
document.getElementById("price-action").onclick = function () {
        alert("Спасибо за заявку, мы свяжемся с вами в ближайшее время!");
}; */
// work 07.02.2023 base inf site, host server 14/02/2023

