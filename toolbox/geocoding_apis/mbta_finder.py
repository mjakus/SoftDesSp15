"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/ghttps://developers.google.com/maps/documentation/geocoding/eocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json
from pprint import pprint


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"
API_KEY = "BgEaUbVv9ca0u9ylWC6BAyUY"


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)
    latitude = response_data["results"][0]["geometry"]["location"]["lat"]
    longitude = response_data["results"][0]["geometry"]["location"]["lng"]
    return(latitude, longitude)


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """

    place = place_name.replace(' ', '+')
    address = GMAPS_BASE_URL + "?" + "address=" + place
    return get_json(address)
    # return str(address)

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    address = MBTA_BASE_URL + '?api_key=' + MBTA_DEMO_API_KEY + '&lat=' + latitude + '&lon=' + longitude + '&format=json'    
    f = urllib2.urlopen(address)
    response_text = f.read()
    response_data = json.loads(response_text)
    station = response_data['stop'][0]['stop_name']
    distance = response_data['stop'][0]['distance']
    return (station,distance)

def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    lat_and_long = get_lat_long(place_name)
    nearest_station = get_nearest_station(str(lat_and_long[0]), str(lat_and_long[1]))
    return nearest_station

print find_stop_near("Museum of Fine Art")