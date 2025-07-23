The get_aqicn_data.py file contains a simple script that uses Selenium to automate going to aqicn.org 
and downloading historical data. All you need to do to use the function is supply a city name and the 
absolute path of the directory on your local machine where you want to save the files. **However**, please be
aware that there are some cities for which aqicn.org does not have data. There are also cities where aqicn does
not recognize the city name exactly. This is not a problem when a user manually navigate the website, as a
built-in search feature identifies names it can recognize with the city name the user entered. This code is not
at all sophisticated and just passes the city name as part of a url. So, you may encounter an error if the name
isn't exactly the one aqicn can recognize. For now, passing just the name of a major city in China seems to work
fine. 
