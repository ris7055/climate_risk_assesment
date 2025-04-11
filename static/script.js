let map;
let marker;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 0, lng: 0 },
        zoom: 2
    });
}

document.getElementById('locationForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const lat = document.getElementById('lat').value;
    const lon = document.getElementById('lon').value;

    // Send request to back-end
    const response = await fetch('/assess_risk', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ lat, lon })
    });
    const data = await response.json();

    if (data.error) {
        document.getElementById('result').innerHTML = `Error: ${data.error}`;
        return;
    }

    // Display result
    document.getElementById('result').innerHTML = `
        <p>Risk Score: ${data.risk.toFixed(2)}%</p>
        <p>Recommendation: ${data.recommendation}</p>
    `;

    // Update map
    const position = { lat: parseFloat(data.lat), lng: parseFloat(data.lon) };
    map.setCenter(position);
    map.setZoom(10);
    if (marker) marker.setMap(null);
    marker = new google.maps.Marker({
        position,
        map,
        title: `Risk: ${data.risk.toFixed(2)}%`
    });
});

// Initialize map on page load
window.onload = initMap;
