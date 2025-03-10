function add_cart(id){
    fetch('/add_cart/', {
        method: 'POST',
        body: JSON.stringify({id:id})
        })
}