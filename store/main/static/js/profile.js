const safety = document.querySelector('.safety')
const create_shop = document.querySelector('.create_shop')
const safe = document.getElementById('safe')
const login = document.getElementById('login')
const password1 = document.getElementById('password1')
const password2 = document.getElementById('password2')
const create_shopbtn = document.getElementById('create_shop')

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

create_shopbtn.addEventListener('click', function(){
    fetch('/create_shop', {
        method: 'POST'
    })
    .then(response => {
        return response.json()})
    .then(data=>{
        create_shopbtn.style.display = 'none'
        create_shop.innerHTML += ' <form><input type="text" name="name" value="'+ data["name"] +'"><input type="color" name="color" value="'+ data["bg"] +'"><input type="text" name="url" value="'+ data["url"] +'"><input type="file" name="file"><input type="submit" value="save"></form>'
    })
})