const search_input = document.getElementById('search')
const search_panel =  document.getElementsByClassName('search_panel')[0]
search_input.addEventListener('input', function() {
    let text = search_input.value
    let item_html = ''
    fetch('/search_mini', {
        method:'POST', 
        body: JSON.stringify({'text': text})
    })
    .then(response => {
        return response.json()
    })
    .then(data => {
        for (item in data){
            console.log(item)
            item_html += '<div class="item_mini" onclick="open_product('+ data[item].id +')"><h5>'+ data[item].name +'</h5><h6>'+data[item].price+'</h6></div>'
        }
        search_panel.innerHTML = item_html
        search_panel.style.display = 'flex';
    })
})

function open_product(id){
    window.open('/product/'+id)
}