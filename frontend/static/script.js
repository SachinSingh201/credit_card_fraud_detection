const form = document.getElementById('prediction-form');

form.addEventListener('submit', async function(e) {

    e.preventDefault();

    const data = {
        merchant: Number(document.getElementById('merchant').value),
        category: Number(document.getElementById('category').value),
        amt: Number(document.getElementById('amt').value),
        gender: Number(document.getElementById('gender').value),
        lat: Number(document.getElementById('lat').value),
        long: Number(document.getElementById('long').value),
        city_pop: Number(document.getElementById('city_pop').value),
        job: Number(document.getElementById('job').value),
        unix_time: Number(document.getElementById('unix_time').value),
        merch_lat: Number(document.getElementById('merch_lat').value),
        merch_long: Number(document.getElementById('merch_long').value)
    };

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error('Server returned ' + response.status + ' ' + response.statusText);
        }

        const result = await response.json();

        document.getElementById('result-box').style.display = 'block';

        if(result.error) {
            document.getElementById('prediction-result').innerText = 'Error';
            document.getElementById('prediction-result').style.color = '#ef4444';
            document.getElementById('probability-result').innerText = result.error;
        }
        else {
            document.getElementById('prediction-result').innerText = result.prediction;
            document.getElementById('prediction-result').style.color = result.prediction === 'Fraud Transaction' ? '#ef4444' : '#22c55e';

            document.getElementById('probability-result').innerText =
                'Fraud Probability: ' + (result.fraud_probability * 100).toFixed(2) + '%';
        }
    } catch (error) {
        document.getElementById('result-box').style.display = 'block';
        document.getElementById('prediction-result').innerText = 'Connection Error';
        document.getElementById('prediction-result').style.color = '#ef4444';
        document.getElementById('probability-result').innerText = error.message;
    }

});