const safety = document.querySelector('.safety')
const create_shop = document.querySelector('.create_shop')
const safe = document.getElementById('safe')
const login = document.getElementById('login')
const password1 = document.getElementById('password1')
const password2 = document.getElementById('password2')

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

safe.addEventListener('click', function(){

    if (password1 == password2){
        fetch('/change_profile', {
            method: 'POST',
            body: JSON.stringify({'login': login.value, 'password1': password1.value, 'password2': password2.value})
        })
    }
    else{
        
    }
})