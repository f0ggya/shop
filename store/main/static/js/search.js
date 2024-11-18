const search_input = document.getElementById('search')
search_input.addEventListener('input', function() {
    let text = search_input.value
    fetch('/search_mini', {
        method:'POST', 
        body: JSON.stringify({'text': text})
    })
})