// Dashboard chart rendering via Chart.js.
function renderDashboardCharts(data) {
  const trendLabels = data.trend.map((d) => d.day);
  const sales = data.trend.map((d) => d.sales);
  const purchases = data.trend.map((d) => d.purchases);

  new Chart(document.getElementById('stockTrendChart'), {
    type: 'line',
    data: {
      labels: trendLabels,
      datasets: [{
        label: 'Sales (OUT)',
        data: sales,
        borderColor: '#dc3545',
        tension: 0.3,
      }],
    },
  });

  new Chart(document.getElementById('salesPurchaseChart'), {
    type: 'bar',
    data: {
      labels: trendLabels,
      datasets: [
        { label: 'Sales', data: sales, backgroundColor: '#0d6efd' },
        { label: 'Purchases', data: purchases, backgroundColor: '#198754' },
      ],
    },
  });

  new Chart(document.getElementById('categoryChart'), {
    type: 'pie',
    data: {
      labels: data.category_distribution.map((c) => c.category),
      datasets: [{
        data: data.category_distribution.map((c) => c.total),
      }],
    },
  });
}
