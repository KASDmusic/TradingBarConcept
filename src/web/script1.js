var xValues = [0,5,10,15,20,25,30,35,40,45];
var yValue = [7, 7, 6.7, 6.4, 6.7, 6.4, 6.7, 7.0, 7.3, 7.0, 7.3, 7.0, 6.7]

    new Chart("myChart", {
    type: "line",
    data: {
        labels: [7, 7, 6.7, 6.4, 6.7, 6.4, 6.7, 7.0, 7.3, 7.0, 7.3, 7.0, 6.7],
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