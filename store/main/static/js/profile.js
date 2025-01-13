const safety = document.querySelector('.safety')
const create_shop = document.querySelector('.create_shop')

function change_block(elem){

    if (elem.textContent == 'Безопасность'){
        create_shop.classList.add('invise')
        safety.classList.remove('invise')
    }
    else{
        safety.classList.add('invise')
        create_shop.classList.remove('invise')
    }
}