
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

def giant(driver):
    url = "https://covidinfo.reportsonline.com/covidinfo/GiantFood.html"
    driver.get(url)
    booked = driver.find_element_by_xpath("html").text
    no_appt = "There are currently no COVID-19 vaccine appointments available. Please check back later. We appreciate your patience as we open as many appointments as possible. Thank you."
    status = "None"
    print("Giant:", booked)
    if booked != no_appt:
        status = "Available"
        print("AVAILABLE AT GIANT")
    return status



def cvs(driver):
    url = "https://www.cvs.com/immunizations/covid-19-vaccine"
    driver.get(url)

    try:
        md_xpath = "/html/body/content/div/div/div/div[3]/div/div/div[2]/div/div[5]/div/div/div/div/div/div[1]/div[2]/div/div[2]/div/div/div/div/div[1]/ul/li[10]/div/a/span"
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, md_xpath))).click()

        bethesda_xpath = "/html/body/div[2]/div/div[18]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[5]/div/div/table/tbody/tr[2]/td[2]/span"
        booked = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, bethesda_xpath))).text

        no_appt = "Fully Booked"
        status = "None"

        print("CVS:", booked)
        if booked != no_appt:
            status = "Available"
            print("AVAILABLE AT CVS")

    except NoSuchElementException:
        print("CVS: Error")
        status = "Error"
        
    return status

def walgreens(driver):
    url = "https://www.walgreens.com/findcare/vaccination/covid-19"
    driver.get(url)

    try:
        started_xpath = "/html/body/div[2]/section/section/div[2]/section/section/section[2]/a/span"
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, started_xpath))).click()

        search_xpath = "/html/body/div[2]/div/div/section/section/section/section/section/section[2]/div/span/button"
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, search_xpath))).click()
        
        try:
            alert_xpath = '/html/body/div[2]/div/div/section/section/section/section/section/section[1]/p'
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, alert_xpath)))
        except TimeoutException:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, search_xpath))).click()
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, alert_xpath)))

        
        booked = driver.find_element_by_xpath(alert_xpath).text
        no_appt = "COVID-19 vaccination appointments are not available within 25 miles of 20810 for next 3 days"
        status = "None"
        print("Walgreens:", booked)
        
        if booked != no_appt:
            status = "Available"
            print("AVAILABLE AT WALGREENS")
        
    except:
        print("Walgreens: error")
        status = "Error" 

    return status

def safeway(driver):
    try:
        url = "https://mhealthcheckin.com/covidvaccine?clientId=1600101762362&region=Maryland&urlId=%2Fvcl%2Fcovid2781"
        driver.get(url)

        attest_xpath = "/html/body/div/div/main/div/div[2]/div/div[9]/div[5]/div/div[1]/div[2]/label/input"
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, attest_xpath))).click()

        submit_xpath = "/html/body/div/div/main/div/div[2]/div/div[9]/div[5]/div/div[2]/button"
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, submit_xpath))).click()

        dropdown_xpath = "/html/body/div[1]/div[3]/div/div/div[1]/div/div[2]/div/div[3]/div/div/form/div/select"
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, dropdown_xpath)))
        dropdown=Select(driver.find_element_by_xpath(dropdown_xpath))
        dropdown_word = "COVID Vaccine Dose 1 Appt"
        dropdown.select_by_visible_text(dropdown_word)

        setup_xpath = "/html/body/div[1]/div[3]/div/div/div[1]/div/div[2]/div/div[4]/div[2]/div[1]/div/button"
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, setup_xpath))).click()

        time.sleep(3) #element will exist but be non-interactable
        next_xpath = "/html/body/div[1]/div[3]/div/div/div[2]/div/div[2]/div/div[4]/div[2]/div[1]/div/button"
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, next_xpath))).click()

        time.sleep(3)
        output_xpath = "/html/body/div[1]/div[3]/div/div/div[3]/div/div[2]/div/div[3]/div/div/form/div[2]/div[4]/div/p"
        booked = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, output_xpath))).text

        status = "None"

        print("Safeway:", booked)
    
        no_appt = "There is no availability at this time. Please try a different search or check back later as more availability may open."
        if booked != no_appt:
            status = "Available"
            print("AVAILABLE AT SAFEWAY")
        
    except:
        status = "Error" 

    return status

    