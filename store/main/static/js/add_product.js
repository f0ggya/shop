const modal = document.getElementById('add_product')

function add_product(){
    modal.style.display = 'block'
}

function del_product(id){
    const row = document.getElementById(id)
    row.remove()
    fetch('/del_product/', {
        method: 'DELETE',
        body: JSON.stringify({
            'id': id
        })
    })
}

function update_product(id){
    const row = document.getElementById(id)
    const info = row.querySelectorAll('td')
    let name = info[0].textContent.trim()
    let description = info[1].textContent.trim()
    let price = info[2].textContent.trim()
    let img = info[3].getAttribute('src')
    document.getElementById('name').value = name;
    document.getElementById('img').value = img;
    document.getElementById('description').value = description;
    document.getElementById('price').value = parseInt(price);
    modal.querySelector('form').setAttribute('action', `/update_product/${ id }`)
    modal.style.display = 'block'
}