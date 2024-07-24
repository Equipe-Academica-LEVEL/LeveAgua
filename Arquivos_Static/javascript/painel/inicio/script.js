const painel = document.querySelector('#painel')
painel.addEventListener('click', b1)
const relatorios = document.querySelector('#relatorios')
relatorios.addEventListener('click', b2)
const config = document.querySelector('#configuracoes')
config.addEventListener('click', b3)

function b1(){
    painel.classList.add('is-selected')
    relatorios.classList.remove('is-selected')
    config.classList.remove('is-selected')
}

function b2(){
    painel.classList.remove('is-selected')
    relatorios.classList.add('is-selected')
    config.classList.remove('is-selected')
}

function b3(){
    painel.classList.remove('is-selected')
    relatorios.classList.remove('is-selected')
    config.classList.add('is-selected')
}