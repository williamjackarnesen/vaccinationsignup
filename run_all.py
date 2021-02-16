import requests
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, pickle
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import NoSuchElementException 
from selenium.common.exceptions import TimeoutException 
from scrapers import giant, cvs, walgreens, safeway

#RUN EVERYTHING
start_time = time.time()
driver = webdriver.Chrome("./chromedriver")
giant_status = giant(driver)
cvs_status = cvs(driver)
walgreens_status = walgreens(driver)
safeway_status = safeway(driver)
driver.close()
end_time = time.time()
print("Done in", round(end_time-start_time,1),"seconds")

print()

if giant_status == "None" and cvs_status == "None" and walgreens_status == "None" and safeway_status == "None":
	print("There are no appointments available")
else:
	print("THERE ARE APPOINTMENTS AVAILABLE")

print()