from flask import Flask, render_template, request, jsonify
import ee
import requests

# Initialize Flask app
app = Flask(__name__)

# Initialize Google Earth Engine
ee.Initialize()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/assess_risk', methods=['POST'])
def assess_risk():
    # Get location from front-end
    data = request.get_json()
    lat = float(data['lat'])
    lon = float(data['lon'])

    # Example: Fetch precipitation data from GEE (simplified)
    try:
        # Define a point of interest
        point = ee.Geometry.Point([lon, lat])
        # Get precipitation data (e.g., CHIRPS dataset)
        # precip = ee.ImageCollection('UCSB-CHG/CHIRPS/DAILY') \
        #            .filterDate('2023-01-01', '2023-12-31') \
        #            .select('precipitation') \
        #            .mean() \
        #            .reduceRegion(reducer=ee.Reducer.mean(), geometry=point, scale=5000) \
        #            .get('precipitation').getInfo()
        # Get precipitation data for the most recent month (e.g., March 2023)
        precip = ee.ImageCollection('UCSB-CHG/CHIRPS/DAILY') \
                    .filterDate('2023-03-01', '2023-03-31') \
                    .select('precipitation') \
                    .mean() \
                    .reduceRegion(reducer=ee.Reducer.mean(), geometry=point, scale=5000) \
                    .get('precipitation').getInfo()

        # Simulate risk (mock ML model: high precip = high flood risk)
        # risk_score = min(precip / 100, 1.0)  # Normalize to 0-1
        # risk_percentage = risk_score * 100
        # Simulate risk (mock ML model: high precip = high flood risk)
        risk_score = min(precip / 30, 1.0)  # Normalize to 0-1, with 30 mm/day as the max threshold
        risk_percentage = risk_score * 100

        # Simple recommendation logic
        if risk_percentage > 70:
            recommendation = "Install flood barriers immediately."
        elif risk_percentage > 30:
            recommendation = "Monitor water levels and prepare sandbags."
        else:
            recommendation = "No immediate action needed."

        return jsonify({
            'risk': risk_percentage,
            'recommendation': recommendation,
            'lat': lat,
            'lon': lon
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)