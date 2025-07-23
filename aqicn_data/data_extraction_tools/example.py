#This simple loop will automatically download the historical air pollution data available on aqicn.org for the 
#cities in the 'cities' list and will save them in the directory you specify.

from get_aqicn_data import get_aqicn_data

cities = ['Baotou', 'Shenzhen', 'Beijing']
for i in cities:
  get_aqicn_data(i, 'your_directory_path')
