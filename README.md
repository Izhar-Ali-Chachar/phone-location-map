# Phone Location Map

This Python project processes international phone numbers, retrieves their geographic locations and carrier information, and generates an interactive map using **Folium**. The map is displayed with phone number details and location markers.

## Features:
- Handles phone numbers from various countries.
- Uses **OpenCage** API to get geographic coordinates for locations.
- Displays markers on the map with detailed information (phone number, location, carrier).
- Interactive map with **MarkerCluster**, **MiniMap**, and **Fullscreen** controls.

## Requirements:
To run this project, you need to install the following dependencies:

- **phonenumbers**: For parsing phone numbers and extracting location and carrier information.
- **folium**: For creating interactive maps.
- **opencage**: For geocoding location descriptions.

You can install them using the `requirements.txt` file:

```bash
pip install -r requirements.txt
