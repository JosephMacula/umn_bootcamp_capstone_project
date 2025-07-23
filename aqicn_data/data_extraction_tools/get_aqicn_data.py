import glob
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait   

def get_aqicn_data(city, download_directory, file_name = None):

	driver_options = Options()
	driver_options.set_preference("browser.download.folderList", 2)
	driver_options.set_preference("browser.download.manager.showWhenStarting", False)
	driver_options.set_preference('browser.download.dir', download_directory)
	driver_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

	driver = webdriver.Firefox(options = driver_options)

	city = city.lower()
	url = 'https://aqicn.org/historical/#!city:' + city

	driver.get(url)
	first_download_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.histui.ui.basic.primary.button")))
	driver.execute_script("arguments[0].click();", first_download_button)
	second_download_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.histui.ui.large.primary.button")))
	driver.execute_script("arguments[0].click();", second_download_button)

	if file_name != None:
		downloaded_csv_files = glob.glob(download_directory+'/*.csv')
		most_recent_csv = max(downloaded_csv_files, key=os.path.getctime)
		os.rename(most_recent_csv, download_directory+'/'+file_name+'.csv')
