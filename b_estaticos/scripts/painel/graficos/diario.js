// diario.js

document.addEventListener('DOMContentLoaded', function() {
    // Dados de exemplo diretamente no script
    const labels = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']; // Labels para os dias da semana
    const data = [12, 19, 3, 5, 2, 3, 7]; // Dados de consumo em litros

    const ctx = document.getElementById('grafico-dia').getContext('2d');

    // Cria o gráfico de linha
    const myChart = new Chart(ctx, {
        type: 'line', // Tipo de gráfico: linha
        data: {
            labels: labels, // Labels no eixo X
            datasets: [{
                label: 'Consumo Diário (Litros)', // Legenda do gráfico
                data: data, // Dados no eixo Y
                fill: false, // Não preencher a área sob a linha
                borderColor: 'rgba(54, 162, 235, 1)', // Cor da linha
                tension: 0.1 // Suavidade da curva da linha
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true // Iniciar o eixo Y no valor 0
                }
            }
        }
    });
});
