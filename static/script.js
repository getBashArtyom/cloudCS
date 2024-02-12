document.getElementById("predictionForm").addEventListener("submit", function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    const queryParams = new URLSearchParams(formData).toString();
    fetch(`/predict?${queryParams}`, {
        method: 'GET'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("predictionResult").innerText = "Predicted Price: $" + data.predicted_price;
    })
    .catch(error => console.error('Error:', error));
});