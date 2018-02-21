function DropdownPopulate() {
    var url = '/names';
    Plotly.d3.json(url, function(error, response){
        if (error) {
            return console.warn(error);
        }
        alert(response)
        var sel = document.getElementById('Sample_IDs');
        for(var i=0; i<response.length; i++) {
            var opt = document.createElement('option');
            opt.innerHTML = response[i];
            opt.value = response[i];
            sel.appendChild(opt);
        }
    });
}

DropdownPopulate();