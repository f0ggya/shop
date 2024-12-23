const reg_form = document.getElementsByClassName('reg_form')[0]
const log_form = document.getElementsByClassName('log_form')[0]

function show_reg(){
    document.getElementById('reg').style.display = 'flex';
    document.getElementsByTagName('main')[0].style.filter = 'blur(20px)'
}

function start_reg(elem){
    if (elem.textContent == 'Если нет аккаунта создать?'){
        log_form.style.display = 'none'
        reg_form.style.display = 'block'
        reg_form.style.width = 'fit-content'
    }
    else{
        log_form.style.display = 'block'
        reg_form.style.display = 'none'
        reg_form.style.width = '0'
    }
}