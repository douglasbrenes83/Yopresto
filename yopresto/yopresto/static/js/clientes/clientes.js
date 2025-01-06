document.getElementById('toggle-menu-btn').addEventListener('click', function() {
    document.getElementById('form').style.marginTop='-450px';
    document.getElementById('list').style.display = 'block';

    
});
document.getElementById('close').addEventListener('click', function() {
    document.getElementById('list').style.display = 'none';
    document.getElementById('form').style.marginTop='90px';    
});
