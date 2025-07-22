import requests

#A function that calls the Google Maps geocoding API to obtain bounding box information for the given city, supplied 
#by the input city_name. api_key is a personal Google Maps API key and region should be a two character region code. 

def get_city_bounds(city_name, api_key, region):
    endpoint = "https://maps.googleapis.com/maps/api/geocode/json" #the URL to the API, with the specificaiton for JSON output
    params = {"address": city_name, "region": region, "key": api_key}
    
    response = requests.get(endpoint, params=params).json()
    result = response["results"][0]
    geometry = result["geometry"]
    bounds = geometry.get("bounds") 

    #returns a dict object consisting of a single key/value pair. The key is the city name, the value is a tuple
    #consisting of a boundary box for the city in the format suitable for input to the Giovanni webpage 
        
    return {"city": result['address_components'][0]['short_name'],
            "bounding_box": (bounds["southwest"]['lng'],bounds["southwest"]['lat'], bounds["northeast"]['lng'], bounds["northeast"]['lat'])}






api_key = "AIzaSyApFtPIpxJQUeFs59xdFb-HbOScsvtVBrw" #this is my google maps API key :D
city_list = ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen', 'Chengdu', 'Chongqing', 'Wuhan', 'Kunming', 'Panzhihua',
            'Shuozhou', 'Baotou', 'Ganzhou', 'Quanzhou']


#creates a dictionary object whose keys are the cities from city_list and the values are the boundary boxes for the 
#corresponding city

city_bounds = {}
for i in range(0, len(city_list)):
    city_bounds[city_list[i]] = get_city_bounds(city_list[i], api_key, 'cn').get('bounding_box')
