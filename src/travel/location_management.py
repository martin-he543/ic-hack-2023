import googlemaps
import src.utilities.input_protection as ip
import datetime
import json

class Location:

    def __init__(self, address: str=None):
        self.google_api_key = 'AIzaSyAloqkgOYYEh1XSRaPB6Yj85cyuQKUfFxg'
        self.gmaps = googlemaps.Client(self.google_api_key)
        self.location = self.gmaps.geolocate()['location']  # Uses IP location for an initial approximation

        # Set up an approximate address
        if not address:
            address_list = self.gmaps.reverse_geocode(self.location)[0]['address_components']
            address = ''
            for addr in address_list[0]:
                ', '.join([address, addr['long_name']])
            self.address = address
        else:
            self.address = address
            self.location = self.gmaps.geocode(address)[0]['geometry']['location']
    def __repr__(self):
        return self.address

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, new_value: str):
        if isinstance(new_value, str):
            self._address = new_value
        else:
            raise(ValueError('Incorrect Format of Address, {type(new_value)}, Input'))

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, new_value):
        if isinstance(new_value, dict):
            self._location = new_value
    def get_new_address(self):
        """
        IMPLEMENT SELECTION FROM POSTCODE
        Gets user input requests to find an address
        :return:
        :rtype:
        """

        sanitise = lambda field_data: ip.user_str_protection(field_data, None, t_string=True)
        print('Getting User Location Data Input')
        address = [sanitise(input('Enter Building/House Number')), sanitise(input('Enter the street Name')),
                   sanitise(input('Enter the City/Town/Village')), sanitise(input('Enter the postcode')),
                   sanitise(input('Enter the country'))]
        location = ', '.join(address)
        return location

    def set_address(self):
        """
        Get a user location more accurately than the approximate location
        :return:
        :rtype:
        """
        testing = True
        # input_location = input('Enter the address you will leave from.')
        if testing:
            input_location = 'Imperial College London, South Kensington Campus, London SW7 2AZ'
        validation = self.gmaps.addressvalidation(input_location)
        address = validation['result']['address']
        confirmation = input('Is this your address, Y/N:\t')
        if 'y' in confirmation.lower():
            # IMPLEMENT
            pass
        self.address = address
        return self

    def time_to_location(self, destination: str,
                         #arrival_time: datetime.datetime,
                         public_transport: bool = False) -> float:

        if public_transport:
            transport = 'transit'
        else:
            transport = 'driving'
        directions_result = self.gmaps.directions(self.address, destination,
                                                  mode=transport#,
                                                  #arrival_time=arrival_time
                                                  )

        duration = directions_result[0]['legs'][0]['duration']['value']  # Duration in seconds
        return duration

    def dist_to_location(self, destination: str,
                         #arrival_time: datetime.datetime,
                         public_transport: bool = False) -> float:

        if public_transport:
            transport = 'transit'
        else:
            transport = 'driving'
        directions_result = self.gmaps.directions(self.address, destination,
                                                  mode=transport#,
                                                  #arrival_time=arrival_time
                                                  )

        duration = directions_result[0]['legs'][0]['distance']['value']  # Distance in km
        return duration
