The code in the get_Giovanni_data.py and get_boundary_boxes.py files helps automate downloading data on a set of pollutants from NASA's Giovanni web portal. You can find a example in the example.py file. Once you specify the user-specific arguments (your Earthdata username and login, along with the desired download directory, are necessary arguments, while the filename argument is optional) the example code is ready to run. 

Some words of warning: 

1. Giovanni is a bit finnicky. The system may occasionally fail to validate your credentials. If this happens, the get_Giovanni_data function will likely encounter an exception it doesn't know how to handle and will thus throw an error. If this happens, you'll need to run the code again.

2. Giovanni is slow. This makes encountering Giovanni's quirks extra frustrating, as now you have to not only re-run code, but you will likely have to wait a while for it to finish. The get_Giovanni_data function itself also has the potential to take a while to finish running, as there are lots of implicit waits with very long timeout bounds. If getting the desired data isn't so important that you're happy to let Giovanni take its sweet time, you can modify these parameters in a downloaded copy of the code on your local machine.

**Implementation Details**

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
