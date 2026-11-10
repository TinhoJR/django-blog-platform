
import requests


def get_location(ip) :
    response = requests.get("https://ipapi.co/{}/json".format(ip),timeout=5) 
    data = response.json() 
    # country = data.get("country_name") 
    # city = data.get("city")
    # region = data.get("region")
    # latitude = data.get("latitude")
    # longitude = data.get("longitude")

    return data
