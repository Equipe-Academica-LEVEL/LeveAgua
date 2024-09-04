// semanal.js

document.addEventListener('DOMContentLoaded', function() {
    // Labels para os dias da semana
    const labels = [
        'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'
    ];
    
    // Dados de exemplo para cada dia da semana
    const data = [
        50, 75, 60, 90, 80, 70, 65
    ];

    const ctx = document.getElementById('grafico-semana').getContext('2d');

    // Cria o gráfico de linha
    const myChart = new Chart(ctx, {
        type: 'line', // Tipo de gráfico: linha
        data: {
            labels: labels, // Labels no eixo X representando os dias da semana
            datasets: [{
                label: 'Consumo Semanal (Litros)',
                data: data, // Dados de consumo para cada dia
                fill: false,
                borderColor: 'rgba(153, 102, 255, 1)', // Cor da linha
                tension: 0.1 // Suavidade da curva da linha
            }]
        },
        options: {
            responsive: true,  // Faz o gráfico ser responsivo
            maintainAspectRatio: true, // Mantém a proporção do gráfico
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
