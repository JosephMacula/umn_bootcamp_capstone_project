To use the get_Giovanni_data function in th get_Giovanni_data.py file, you need to be aware of what the function arguments should be. 

1. my_username: this needs to be your Earthdata username. Enter it as a string.
2. my_password: this needss to be your Earthdata password. Enter is as a string.
3. start_time and end_time: these need to be entered as strings in the following format: YEAR-MONTH-DAY': e.g., '2000-01-01'
4. measurement: this is the pollutant you want. Right now there are three options the function recognizes: 'NO2', 'SO2', and 'Particulate Matter'
                If you want something else, let me (Joe) know. 

5. boundary_box: this needs to be a list object, with the coordinates in the following order: west longitude, south latitude, east longitude, north latitude
6. download_directory: this should be the directory where you want your files to be downloaded into. This directory needs to exist and the path should be an 
                      absolute path, entered as a string. For example, '/Users/josephmacula/the_rest_of_the_path'
7. file_name: you really should set this to something! If not, the downloaded file will have the default name, which is a string of gibberish. 
              The name can be whatever string you want, but it needs to be a string. 
