import phonenumbers
import folium
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

# Input: Get phone number from user
def get_phone_number():
    number = input("Enter a phone number with country code (e.g., +923111097442): ")
    return number

# Main function to process phone number
def main():
    # Step 1: Parse phone number
    phone_number = get_phone_number()
    parsed_number = phonenumbers.parse(phone_number)

    # Step 2: Retrieve location and carrier
    location = geocoder.description_for_number(parsed_number, "en")
    carrier_name = carrier.name_for_number(parsed_number, "en")
    
    if not location:
        print("Unable to determine the location of the phone number.")
        return

    if not carrier_name:
        carrier_name = "Unknown Carrier"

    print(f"Carrier: {carrier_name}")
    print(f"Location: {location}")


    api_key = "f060fa8c6e63452ba58d6fb2542eb693"
    geocoder_service = OpenCageGeocode(api_key)

    try:
        results = geocoder_service.geocode(location)
        if not results:
            print("Unable to find geographic coordinates for the location.")
            return
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']
        print(f"Coordinates: Latitude {lat}, Longitude {lng}")

    except Exception as e:
        print(f"Error while fetching coordinates: {e}")
        return

    # Step 4: Generate and save map
    try:
        map_object = folium.Map(location=(lat, lng), zoom_start=12)
        folium.Marker(
            location=[lat, lng],
            tooltip=f"Location: {location}",
            popup=f"Carrier: {carrier_name}",
            icon=folium.Icon(color="blue"),
        ).add_to(map_object)
        map_file = "phone_location_map.html"
        map_object.save(map_file)
        print(f"Map saved as {map_file}. Open it in a browser to view.")
    except Exception as e:
        print(f"Error while generating map: {e}")

if __name__ == "__main__":
    main()

