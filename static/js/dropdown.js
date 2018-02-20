
function DropdownPopulate() {
    var url = '/names';
    Plotly.d3.json(url, function(error, response){
        if (error) {
            return console.warn(error);
        }
        var sel = document.getElementById('Sample_IDs');
        for(var i=0; i<names.length; i++) {
            var opt = document.createElement('option');
            opt.innerHTML = names[i];
            opt.value = names[i];
            sel.appendChild(opt);
        }
    });
}

DropdownPopulate();