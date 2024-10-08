// diario.js

document.addEventListener('DOMContentLoaded', function() {
    // Labels para cada hora do dia
    const labels = [
        '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', 
        '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', 
        '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'
    ];
    
    // Dados de exemplo para cada hora do dia
    const data = [
        5, 4, 6, 3, 2, 7, 9, 10, 12, 14, 15, 18, 
        17, 16, 20, 22, 21, 19, 13, 11, 8, 7, 6, 5
    ];

    const ctx = document.getElementById('grafico-dia').getContext('2d');

    // Cria o gráfico de linha
    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Consumo Diário (Litros)',
                data: data,
                fill: false,
                borderColor: 'rgba(54, 162, 235, 1)',
                tension: 0.1
            }]
        },
        options: {
            responsive: true,  // Faz o gráfico ser responsivo
            maintainAspectRatio: true, // Permite que o gráfico se ajuste ao contêiner sem manter a proporção
            aspectRatio: 8 / 3, // Define a proporção de aspecto como 16:9
            scales: {
                y: {
                    beginAtZero: true // Iniciar o eixo Y no valor 0
                },
                x: {
                    type: 'category', // Certifica-se de que o eixo X seja categórico
                }
            }
        }
    });
});
