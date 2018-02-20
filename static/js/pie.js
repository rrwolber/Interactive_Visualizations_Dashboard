function PiePlot() {
    var url = "/samples/<sample>";
    Plotly.d3.json(url, function(error, response){
        if (error) {
            return console.warn(error);
        }
        var layout = {
            title: "Bacteria Present"
            };
        Plotly.newPlot('BBBpie', [response], layout);
    });
}

PiePlot();