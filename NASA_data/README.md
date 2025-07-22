The code in the get_Giovanni_data.py and get_boundary_boxes.py files helps automate downloading data on a set of pollutants from NASA's Giovanni web portal. You can find a example in the example.py file. Once you specify the user-specific arguments (your Earthdata username and login, along with the desired download directory, are necessary arguments, while the filename argument is optional) the example code is ready to run. 

Some words of warning: 

1. Giovanni is a bit finnicky. The system may occasionally fail to validate your credentials. If this happens, the get_Giovanni_data function will likely encounter an exception it doesn't know how to handle and will thus throw an error. If this happens, you'll need to run the code again.

2. Giovanni is slow. This makes encountering Giovanni's quirks extra frustrating, as now you have to not only re-run code, but you have to likely wait a while for it to finish. The get_Giovanni_data function itself also has the potential to take a while to finish running, as there are lots of implicit waits with very long timeout bounds. If getting the desired data isn't so important that you're happy to let Giovanni take its sweet time, you can modify these parameters in a downloaded copy of the code on your local machine.


