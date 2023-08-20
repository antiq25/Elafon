let typeChart;
let techChart;
let itemChart;

function refreshChartData() {
  $.getJSON("/get_equipment_stats")
    .done(function (data) {
      const typeLabels = Object.keys(data.type_stats);
      const typeValues = Object.values(data.type_stats);
      const techLabels = Object.keys(data.top_techs);
      const techValues = Object.values(data.top_techs);
      const itemLabels = Object.keys(data.popular_items);
      const itemValues = Object.values(data.popular_items);

      // Initialize or update the Type Chart
      if (typeChart) {
        typeChart.data.labels = typeLabels;
        typeChart.data.datasets[0].data = typeValues;
        typeChart.update();
      } else {
        typeChart = new Chart(document.getElementById("typeChart"), {
          type: "bar",
          data: {
            labels: typeLabels,
            datasets: [
              {
                label: "Equipment Types Signed Out",
                data: typeValues,
                backgroundColor: "rgba(75, 192, 192, 0.2)",
                borderColor: "rgba(75, 192, 192, 1)",
                borderWidth: 1,
                color: "rgba(255, 255, 255, 255)", 
              },
            ],
          },
          options: {
            responsive: true,
            scales: {
              y: {
                beginAtZero: true,
              },
            },
          },
        });
      }

      // Similarly, initialize or update the Technician and Item charts...

      // Technician Chart
      if (techChart) {
        techChart.data.labels = techLabels;
        techChart.data.datasets[0].data = techValues;
        techChart.update();
      } else {
        techChart = new Chart(document.getElementById("techChart"), {
          type: "bar",
          data: {
            labels: techLabels,
            datasets: [
              {
                label: "Top Technicians",
                data: techValues,
                backgroundColor: "rgba(255, 99, 132, 0.2)",
                borderColor: "rgba(255, 99, 132, 1)",
                borderWidth: 1,
              },
            ],
          },
          options: {
            responsive: true,
            scales: {
              y: {
                beginAtZero: true,
              },
            },
          },
        });
      }

      // Item Chart
      if (itemChart) {
        itemChart.data.labels = itemLabels;
        itemChart.data.datasets[0].data = itemValues;
        itemChart.update();
      } else {
        itemChart = new Chart(document.getElementById("itemChart"), {
          type: "bar",
          data: {
            labels: itemLabels,
            datasets: [
              {
                label: "Popular Items",
                data: itemValues,
                backgroundColor: "rgba(153, 102, 255, 0.2)",
                borderColor: "rgba(153, 102, 255, 1)",
                borderWidth: 1,
              },
            ],
          },
          options: {
            responsive: true,
            scales: {
              y: {
                beginAtZero: true,
              },
            },
          },
        });
      }
    })
    .fail(function () {
      alert("Failed to fetch equipment stats for the chart. Please try again.");
    });
}

// Call the function to load the data and initialize the charts
$(document).ready(function () {
  refreshChartData();
});
