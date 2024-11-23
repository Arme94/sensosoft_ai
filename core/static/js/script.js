document.addEventListener('DOMContentLoaded', () => {
    // Botones
    const generateReportBtn = document.getElementById('generate-report');
    const predictResultsBtn = document.getElementById('predict-results');
    const detectAnomaliesBtn = document.getElementById('detect-anomalies');
    
    // Campo de datos sensoriales
    const sensorialDataInput = document.getElementById('sensorial-data');
    const resultDiv = document.getElementById('result');

    // Función para mostrar resultados
    const showResult = (message) => {
        resultDiv.innerHTML = `<p>${message}</p>`;
    };

    // Llamadas Fetch
    const callAPI = async (endpoint, data = {}) => {
        try {
            const response = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data),
            });
            const result = await response.json();
            if (response.ok) {
                showResult(`Resultado: ${JSON.stringify(result)}`);
            } else {
                showResult(`Error: ${result.error || 'Algo salió mal.'}`);
            }
        } catch (error) {
            showResult(`Error de conexión: ${error.message}`);
        }
    };

    // Eventos de los botones
    generateReportBtn.addEventListener('click', () => {
        callAPI('/api/generate-report/');
    });

    predictResultsBtn.addEventListener('click', () => {
        const data = sensorialDataInput.value;
        callAPI('/api/predict-results/', { datos: data });
    });

    detectAnomaliesBtn.addEventListener('click', () => {
        const data = sensorialDataInput.value;
        callAPI('/api/detect-anomalies/', { datos: data });
    });
});
