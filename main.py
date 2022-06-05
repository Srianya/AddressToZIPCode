# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests

# get latitude and longitude from an address
def get_ltd_lng():
    params = {
        'address': 'oshiwara industerial center goregaon west mumbai',
        'sensor': 'false',
        'region': 'india',
        'key': 'AIzaSyDI3MAXOazF420JYU2yJD3glMo_OQiaKgw',
    }
    response = requests.get(url="https://maps.googleapis.com/maps/api/geocode/json",params=params)
    response.raise_for_status()
    data = response.json()
    geodata = dict()
    geodata['lat'] = data['results'][0]['geometry']['location']['lat']
    geodata['lng'] = data['results'][0]['geometry']['location']['lng']
    #print(data)
    return (geodata['lat'],geodata['lng'])


def get_zipcode(lat,lng):
    lat = lat
    lng = lng
    params = {

        'key': 'AIzaSyDI3MAXOazF420JYU2yJD3glMo_OQiaKgw',
    }
    response = requests.get(url=f"https://maps.google.com/maps/api/geocode/json?latlng={lat},{lng}",params=params)
    data = response.json()
    print(data)

if __name__ == '__main__':
    lat,lng = get_ltd_lng()[0],get_ltd_lng()[1]
    get_zipcode(lat,lng)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
