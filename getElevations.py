import argparse
import json
import requests

def get_elevation(lat, lng):
    url = f"https://api.open-elevation.com/api/v1/lookup?locations={lat},{lng}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        elevation = data['results'][0]['elevation']
        return elevation
    else:
        print(f"Failed to get data: {response.status_code}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get elevation data for given latitude and longitude.')
    parser.add_argument('coordinatesJSON', type=str, help='JSON string containing coordinates')

    args = parser.parse_args()
    coordinates_string = args.coordinatesJSON
    coordinates = json.loads(coordinates_string)

    output = []

    for coord in coordinates:
        lat = coord.get('latitude')
        lng = coord.get('longitude')

        elevation = get_elevation(lat, lng)

        if elevation is not None:
            output.append({'latitude':lat, 'longitude':lng, 'elevation': elevation})
            print(f"The elevation at latitude {lat} and longitude {lng} is {elevation} meters.")

    # Set the output variable
    print(f"\"elevationsJSON=\'{json.dumps(output)}\'\" >> $GITHUB_OUTPUT")
