"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json
from pprint import pprint


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib2.urlopen(url)  #opens url
    response_text = f.read()  #reads through url
    response_data = json.loads(response_text)  #converts data to json
    return response_data


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    new_place = place_name.replace(' ', "+")  #replaces spaces with + symbols for url 
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + new_place + "&key=AIzaSyAqswAJZEulRtIHPvMpyCEYMT8XpU8uCM4" 
    #generates url and then retrives the json
    json = get_json(url)
    results = json["results"][0]['geometry']['location']  #locates the necessary part of the dictionary in the json
    lat_long = results['lat'],results['lng']  #creates a tuple of lat and long
    return lat_long #tuple


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See l for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    #makes latitude and longitude strings so that they can be entered into url
    latitude = str(latitude)
    longitude = str(longitude)
    #defines url
    url = "http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key="+ MBTA_DEMO_API_KEY + "&lat=" + latitude + "&lon=" + longitude + "&format=json"
    #generates json object and then calls the relevant quantities 
    json = get_json(url)
    distance = json['stop'][0]['distance']
    stopname = json['stop'][0]['stop_name']
    #returns of a tuple of stopname, distance from stop
    return (stopname, distance)


def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    #get lat and long of a place name, and then seperate the returned tuple into seperate entities
    lat_long = get_lat_long(place_name)
    lat = lat_long[0]
    lon = lat_long[1]
    #get the nearest stop from the lat lon entities 
    stop_distance = get_nearest_station(lat, lon)
    #converts unicode to strings
    stop = str(stop_distance[0])
    distance = str(stop_distance[1])
    #returns a sentence indicating where the closest stop is to the place name enetered 
    return place_name +' is ' + distance + " miles away from " + stop

