from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import warnings
import glob
import os

def get_Giovanni_data(start_time, end_time, measurement, boundary_box, download_directory, file_name = None):
	warnings.warn("Remember: boundary box elements should be in the following order: west longitude, south latitude, east longitude, north latitude. If this convention is not followed, unexpected behavior or errors may occur.")
	if type(start_time) != str or type(end_time) != str:
		raise ValueError("start time and end time must be of type 'str' and in the format 'YEAR-MONTH-DAY': e.g., '2000-01-01'")
	if type(boundary_box) != list:
		raise ValueError("boundary_box must be of type 'list'")

	#setting up the web driver and opening the Giovanni webpage
	driver_options = Options()
	driver_options.set_preference('browser.download.dir', download_directory)
	driver = webdriver.Firefox()
	driver.get('https://giovanni.gsfc.nasa.gov/giovanni/')

	#ensure that the webpage loads first, then click the login button to get to the user login page.
	
	WebDriverWait(driver, 100).until(EC.invisibility_of_element_located((By.ID,  "progressModal")))
	login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id = 'loginButton']")))
	login_button.click()

	#enters a valid username and password, then clicks the login button to return to the Giovanni page. Hardcoded right now but 
	#will eventually be function inputs. 

	username = driver.find_element(By.XPATH, "//input[@id = 'username']")
	password = driver.find_element(By.XPATH, "//input[@id = 'password']")
	username.send_keys("joseph.macula@colorado.edu")
	password.send_keys("Cargillproject1!")
	gio_login = driver.find_element(By.XPATH, "//input[@value = 'Log in']")
	gio_login.click()

	#Giovanni takes a while to reload, so we need an explicit wait here to be sure we don't try to click before the loading
	#animation is complete. 
	
	WebDriverWait(driver, 100).until(EC.invisibility_of_element_located((By.ID,  "progressModal")))


	#Right now this is hardedcoded. Need to change this. 
	
	select_plot = 'service=ArAvTs'
	start = 'starttime='+ start_time 
	end = 'endtime='+ end_time 
	bdy_box = 'bbox='+str(boundary_box[0])+','+str(boundary_box[1])+','+str(boundary_box[2])+','+str(boundary_box[3])
	data_type = 'variableFacets=dataFieldMeasurement%3A'+measurement+'%3B'

	if measurement == 'SO2':
	    data_source = 'data=OMSO2e_003_ColumnAmountSO2'
	elif measurement == 'NO2':
	    data_source = 'data=OMNO2d_003_ColumnAmountNO2CloudScreened'
	elif measurement == 'Particulate Matter':
	    data_source = 'data=M2TMNXAER_5_12_4_TOTCMASS25'
	else: 
	    raise ValueError("Measurement must be one of the following: 'SO2', 'NO2', or 'Particulate Matter'")
	    print('sorry, we''re working on adding more functionality!')

	#Assembling the URL that will get Giovanni loaded with all the user-specified search terms
	new_url = 'https://giovanni.gsfc.nasa.gov/giovanni/#' + '&' + select_plot + '&' + start + '&' + end + '&' + bdy_box + '&' + data_source + '&' + data_type

	#Refreshing the page with this new URL
	driver.get(new_url)
	driver.refresh()


    	#This is an almost-certainly highly imperfect solution to an ElementClickIntercepted exception. The following two WebDriverWait
	#are the solution I found to ensure that the 'Plot Data' button gets clicked. 
	
	WebDriverWait(driver, 100).until(EC.invisibility_of_element_located((By.ID,  "progressModal")))
	plot_data = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "sessionDataSelToolbarplotBTN-button")))
	WebDriverWait(driver, 100).until(EC.invisibility_of_element_located((By.ID,  "progressModal")))
	plot_data.click()

	#The timeout parameter is really big because Giovanni can be really slow. Could try and tune this number later if one
	#doesn't want to wait as long as is necessary for the plot to return. 
	
	WebDriverWait(driver, 100000).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@id,'downloadToggleButton')]")))

	#Click the download button and then click the CSV button from the dropdown menu that appears. If your browser is 
	#configured to automatically download files into a specified directory, that's where the CSV file will land. 
	
	download_button = driver.find_element(By.XPATH, "//button[contains(@id,'downloadToggleButton')]")
	ActionChains(driver).move_to_element(download_button).click().perform()
	csv_download = driver.find_element(By.XPATH, "//*[@title = 'Download CSV']")
	csv_download.click()

	#renaming the downloaded file, provided that file_name is not the default 'None' value
	if file_name != None:
		downloaded_csv_files = glob.glob(download_directory+'/.csv')
		most_recent_csv = max(downloaded_csv_files, key=os.path.getctime)
		os.rename(most_recent_csv, download_directory+'/'+file_name+'.csv')
	
