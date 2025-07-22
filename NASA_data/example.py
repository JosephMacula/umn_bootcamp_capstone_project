#Here's an example of using the get_Giovanni_data function together with the get_city_bounds function to automate the process of downloading either NO2,
#SO2, or PM 2.5 pollution data as area-averaged time series data in csv format from NASA's Giovanni web portal. You'll need to have an EarthData account
#(it's free to make one) and will need to pass your username as password as the first and second arguments, respectively, in the call to the
#get_Giovanni_data function in the final for loop below. 

from get_Giovanni_data import get_Giovanni_data
from get_coordinates import get_city_bounds

brazilian_cities = ['Rio de Janeiro', 'Sao Paulo', 'Manaus']
br_city_bounds = {}
for i in range(0, len(brazilian_cities)):
    br_city_bounds[brazilian_cities[i]] = get_city_bounds(brazilian_cities[i], api_key, 'br').get('bounding_box')

for i in br_city_bounds:
    get_Giovanni_data('your_EarthData_username', 'your_EarthData_password', '2020-01-01','2021-01-01','SO2', list(br_city_bounds[i]), 'your_download_directory', i)

