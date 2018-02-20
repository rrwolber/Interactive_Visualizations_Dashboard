function buildPlot() {
    var url = "/samples/<sample>";
    Plotly.d3.json(url, function(error, response){
        if (error) {
            return console.warn(error);
        }
        var layout = {
            };
        Plotly.newPlot('plot', [response], layout);
    });
}

buildPlot();