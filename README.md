# Climate_risk_assesment_prototype
This repository is for the participants of KITAHACK Team Sustainovators
![image](https://github.com/user-attachments/assets/5849d1a9-747d-461d-8098-68ce9951b1de)

## Overview
`
The Climate Risk Assessment Tool is a web application built with Flask and Google Earth Engine (GEE) to assess flood risk for a given location based on latitude and longitude inputs. 
The app fetches environmental data (precipitation, elevation, land cover) from GEE, calculates a flood risk score, and provides actionable recommendations. 
It features a Google Maps interface to visualize the location and risk score on a map. This project was developed to help users in flood-prone regions, such as Malaysia, 
understand their climate risk and take preventive measures. The app currently focuses on flood risk but can be extended to assess other climate risks like landslides or heatwaves.
`
### Features:
**>Flood Risk Assessment:** Calculates a flood risk score (0%–100%) based on maximum daily precipitation, elevation, and land cover data.\
**>Actionable Recommendations:** Provides recommendations based on the risk score (e.g., "Install flood barriers immediately").\
**>Interactive Map**: Displays the assessed location on a Google Map with a marker showing the risk score.\
**>Detailed Output:** Shows raw data including maximum daily precipitation, number of heavy rain days, elevation, and land cover type.\
**>Customizable:** Easily extendable to include more data sources, risk types, or a machine learning model for better accuracy.

### Project Structure:
```
climate-risk-app/
├── static/
│   ├── script.js        # JavaScript for front-end logic (map, form handling)
│   └── style.css        # CSS for styling the web app
├── templates/
│   └── index.html       # HTML template for the web app
├── app.py               # Main Flask application script
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation (this file)
```

### Prerequisites:
To run this project, you’ll need the following:
```
> Python 3.8+: Ensure Python is installed on your system.
> Google Cloud Project: A Google Cloud project with the Earth Engine API enabled.
> Google Maps API Key: A Google Maps API key for the map visualization.
> Earth Engine Account: An Earth Engine account and authentication set up.
> Git: To clone the repository.
```
### Setup Instructions:
**1. Clone the Repository**\
Clone this repository to your local machine:
```
git clone https://github.com/your-username/climate-risk-app.git
cd climate-risk-app
```
**2. Set Up a Virtual Environment**\
Create and activate a virtual environment to manage dependencies:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
**3. Install Dependencies:**
flask==2.0.1
earthengine-api==0.1.357
requests==2.28.1
Install the required Python packages listed in requirements.txt:
```
pip install -r requirements.txt
```
**4. Set Up Google Cloud and Earth Engine**

a. Create a Google Cloud Project:\
b. Go to [console.cloud.google.com.](console.cloud.google.com)\
c. Create a new project (e.g., climate-risk-app)\
d. Enable the Earth Engine API for your project.\
e. Link a billing account (required for some APIs, even for free-tier usage).\

**Authenticate with Google Cloud:**\
a. Install the Google Cloud SDK: [cloud.google.com/sdk](cloud.google.com/sdk)\
b. Authenticate with your Google account
```
gcloud auth login
```
c. set your project ID
```
gcloud config set project your-project-id
```
d. Generate Application Default Credentials:
```
gcloud auth application-default login
```
e. Set the quota project for Earth Engine:
```
gcloud auth application-default set-quota-project your-project-id
```

**Authenticate with Earth Engine:**

Run the Earth Engine authentication command:
```
earthengine authenticate
```
**5. Get a Google Maps API Key**
Go to [console.cloud.google.com](console.cloud.google.com)\
Enable the Maps JavaScript API for your project.\
Create an API key under APIs & Services > Credentials.\
Add the API key to templates/index.html:
```
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY"></script>
```
Replace YOUR_API_KEY with your actual Google Maps API key.

**6. Run the Application**
Start the Flask server:
```
python app.py
```
The app will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000). Open this URL in your browser to use the app.

### Usage:
1. Enter Coordinates:
Input the latitude and longitude of the location you want to assess (e.g., Kuala Lumpur: Latitude 3.1390, Longitude 101.6869).
The app accepts decimal degrees (e.g., 5.4164, not 5° 24' 59").
2. Assess Risk:
Click the "Assess Risk" button.
The app will fetch data from Google Earth Engine (maximum daily precipitation, elevation, land cover) and calculate a flood risk score.
3. View Results:
The risk score (0%–100%) and recommendation will be displayed below the map.
Additional data (precipitation, heavy rain days, elevation, land cover) will also be shown.
The map will zoom to the specified location with a marker showing the risk score.

### Example Inputs:
```
Penang, Malaysia:
Latitude: 5.4164
Longitude: 100.3327

Kuala Lumpur, Malaysia:
Latitude: 3.1390
Longitude: 101.6869

Cameron Highlands, Malaysia:
Latitude: 4.4721
Longitude: 101.3801
```
### How It Works:
Back-End (app.py)\
**Flask Server:** Handles HTTP requests and renders the web interface.\

**Google Earth Engine:**
Fetches maximum daily precipitation for November 2023 using the CHIRPS dataset.
Counts the number of days with heavy rainfall (>20 mm/day).
Fetches elevation data using the SRTM dataset.
Fetches land cover data using the MODIS dataset.

**Risk Calculation:**\
Base risk score: risk_score = min(precip / 50, 1.0) (50 mm/day threshold for 100% risk).\

**Adjustments:**\
Elevation <5 meters: Increase risk by 20%.\
Urban land cover (MODIS class 13): Increase risk by 10%.\
Frequency of heavy rain: Add up to 30% based on the number of heavy rain days.\
Final risk: risk_percentage = risk_score * 100.\

**Recommendations:**\
80%: "Install flood barriers immediately."\
40%-80%: "Monitor water levels and prepare sandbags."\
<40%: "No immediate action needed."\

**Front-End (index.html, script.js, style.css)**\
HTML (index.html): Provides the user interface with input fields for latitude and longitude, a Google Map, and a result section.
JavaScript (script.js): Handles form submission, sends requests to the back-end, updates the map, and displays the results.
CSS (style.css): Styles the web app for a clean and user-friendly appearance.




