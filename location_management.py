import googlemaps
class Location:

    def __init__(self):
        self.google_api_key = 'AIzaSyAloqkgOYYEh1XSRaPB6Yj85cyuQKUfFxg'
        self.gmaps = googlemaps.Client(self.google_api_key)
        self.location = self.gmaps.geolocate()
        return self
    def get_location(self):


loc = Location()
loc.get_location()
