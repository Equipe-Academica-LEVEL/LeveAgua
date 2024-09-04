// anual.js

document.addEventListener('DOMContentLoaded', function() {
    // Labels para os meses do ano
    const labels = [
        'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    ];
    
    // Dados de exemplo para cada mês do ano
    const data = [
        120, 150, 180, 130, 200, 220, 170, 190, 210, 250, 230, 240
    ];

    const ctx = document.getElementById('grafico-ano').getContext('2d');

    // Cria o gráfico de linha
    const myChart = new Chart(ctx, {
        type: 'line', // Tipo de gráfico: linha
        data: {
            labels: labels, // Labels no eixo X representando os meses
            datasets: [{
                label: 'Consumo Anual (Litros)',
                data: data, // Dados de consumo para cada mês
                fill: false,
                borderColor: 'rgba(75, 192, 192, 1)', // Cor da linha
                tension: 0.1 // Suavidade da curva da linha
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
