import requests
import config


class ZipCode:

    def __init__(self):
        self.zipcode = ""
        self.latlng = tuple()
        self.ADDRESS = ""
        self.geo_data = dict()

    def get_ltd_lng(self):
        """
        The get_ltd_lng uses input address to find latitude longitude values of the given location using Google API
        :return: tuple of latitude and longitude of the location
        """
        params = {
            'address': self.ADDRESS,
            'sensor': 'false',
            'key': config.api_key,
        }
        response = requests.get(url="https://maps.googleapis.com/maps/api/geocode/json", params=params)
        response.raise_for_status()

        # check if response is OK then only proceed
        data = response.json()
        if data['status'] == 'OK':
            self.geo_data['lat'] = data['results'][0]['geometry']['location']['lat']
            self.geo_data['lng'] = data['results'][0]['geometry']['location']['lng']

            return self.geo_data['lat'], self.geo_data['lng']
        else:
            return None

    def get_zipcode(self,address):
        """
        The get_zipcode uses input address to find zipcode of the given location using Google API and latitude and longitude returned from get_ltd_lng()
        :return: tuple of latitude and longitude of the location
        """
        self.ADDRESS=address
        latlng = self.get_ltd_lng()
        if latlng:
            params = {
                'latlng': f"{latlng[0]},{latlng[1]}",
                'key': config.api_key,
            }
            response = requests.get(url="https://maps.google.com/maps/api/geocode/json", params=params)
            data = response.json()

            # check if response is OK then only proceed

            if data['status'] == 'OK':
                result = (data['results'][0]['address_components'])

                for diction in result:
                    if diction['types'] == ['postal_code']:
                        self.zipcode = diction['long_name']
                        break

                return True
        else:
            return False
