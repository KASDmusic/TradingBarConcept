var xValues = [0,5,10,15,20,25,30,35,40,45];
var yValue = [6.5, 6.5, 6.2, 5.9, 5.6, 5.9, 5.6, 5.3, 5.0, 5.3, 5.6, 5.9, 6.2]

    new Chart("myChart", {
    type: "line",
    data: {
        labels: [6.5, 6.5, 6.2, 5.9, 5.6, 5.9, 5.6, 5.3, 5.0, 5.3, 5.6, 5.9, 6.2],
        datasets: [{
            pointRadius: 0,
            data: yValue,
            borderColor: "red",
            fill: false
        }/*,{
            data: [1600,1700,1700,1900,2000,2700,4000,5000,6000,7000],
            borderColor: "green",
            fill: false
        },{
            data: [300,700,2000,5000,6000,4000,2000,1000,200,100],
            borderColor: "blue",
            fill: false
        }*/]
    },
    options: {
        legend: {display: true}
    }
    });