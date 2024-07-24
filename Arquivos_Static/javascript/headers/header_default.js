function menuShow(){
    let menuMobile = document.querySelector('.mobile-menu');
    let headerShadow = document.querySelector('header');
    if(menuMobile.classList.contains('is-active')){
        menuMobile.classList.remove('is-active');
        headerShadow.classList.remove('is-shadow');
    }
    else{
        menuMobile.classList.add('is-active');
        headerShadow.classList.add('is-shadow');
    }
}