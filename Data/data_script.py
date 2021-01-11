"""Description:
    * author: Magdy Abdelkader
    * company: Fresh Futures/Seeka Technology
    * position: IT Intern
    * date: 07-01-21
    * description:This script extracts the data needed from training.gov.au
"""

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
import os
import time
import bs4

option = webdriver.ChromeOptions()
option.add_argument(" - incognito")
option.add_argument("headless")
exec_path = Path(os.getcwd().replace('\\', '/'))
exec_path = exec_path.parent.__str__() + '/Libraries/Google/v86/chromedriver.exe'
browser = webdriver.Chrome(executable_path=exec_path, options=option)

# read the url from each file into a list
links_file_path = Path(os.getcwd().replace('\\', '/'))
links_file_path = links_file_path.__str__() + '/links.txt'
links_file = open(links_file_path, 'r')

# the csv file we'll be saving the data to
csv_file_path = Path(os.getcwd().replace('\\', '/'))
csv_file = csv_file_path.__str__() + '/training_gov_data.csv'

data = {'Code': '', 'Legal Name': '', 'Business Name(s)': '', 'RTO/Type': '', 'Chief Executive Name': '',
        'Chief Executive Email': '', 'Chief Executive h/p No.': '', 'Registration Enquiries Name': '',
        'Registration Enquiries Email': '', 'Registration Enquiries h/p No.': '', 'Public Enquiries Name': '',
        'Public Enquiries Email': '', 'Public Enquiries h/p No.': '',
        'Qualifications Code 1': '', 'Qualifications title 1': '', 'Qualifications state 1': '',
        'Qualifications Code 2': '', 'Qualifications title 2': '', 'Qualifications state 2': '',
        'Qualifications Code 3': '', 'Qualifications title 3': '', 'Qualifications state 3': '',
        'Qualifications Code 4': '', 'Qualifications title 4': '', 'Qualifications state 4': '',
        'Qualifications Code 5': '', 'Qualifications title 5': '', 'Qualifications state 5': '',
        'Qualifications Code 6': '', 'Qualifications title 6': '', 'Qualifications state 6': '',
        'Qualifications Code 7': '', 'Qualifications title 7': '', 'Qualifications state 7': '',
        'Qualifications Code 8': '', 'Qualifications title 8': '', 'Qualifications state 8': '',
        'Qualifications Code 9': '', 'Qualifications title 9': '', 'Qualifications state 9': '',
        'Qualifications Code 10': '', 'Qualifications title 10': '', 'Qualifications state 10': '',
        'Qualifications Code 11': '', 'Qualifications title 11': '', 'Qualifications state 11': '',
        'Qualifications Code 12': '', 'Qualifications title 12': '', 'Qualifications state 12': '',
        'Qualifications Code 13': '', 'Qualifications title 13': '', 'Qualifications state 13': '',
        'Qualifications Code 14': '', 'Qualifications title 14': '', 'Qualifications state 14': '',
        'Qualifications Code 15': '', 'Qualifications title 15': '', 'Qualifications state 15': ''}

course_data_all = []

# GET EACH COURSE LINK
for each_url in links_file:
    actual_cities = []
    remarks_list = []
    browser.get(each_url)
    pure_url = each_url.strip()
    each_url = browser.page_source
    soup = bs4.BeautifulSoup(each_url, 'lxml')
    time.sleep(1)

    # SUMMERY SECTION

    # summery code
    try:
        THE_XPATH = '//*[@id="rtoDetails-1"]//div[contains(text(),"Code:")]/following-sibling::div'
        WebDriverWait(browser, 1).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, f'{THE_XPATH}'))
        )
        value = browser.find_element_by_xpath(f'{THE_XPATH}').text
        print('CODE: ', value)
        data['Code'] = value
    except(AttributeError, TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
        print('cant extract summery code')

    # summery legal name
    try:
        THE_XPATH = '//*[@id="rtoDetails-1"]//div[contains(text(),"Legal name:")]/following-sibling::div'
        WebDriverWait(browser, 1).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, f'{THE_XPATH}'))
        )
        value = browser.find_element_by_xpath(f'{THE_XPATH}').text
        print('LEGAL NAME: ', value)
        data['Legal Name'] = value
    except(AttributeError, TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
        print('cant extract summery legal name')

    # summery business name
    try:
        THE_XPATH = '//*[@id="rtoDetails-1"]//div[contains(text(),"Business name(s):")]/following-sibling::div'
        WebDriverWait(browser, 1).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, f'{THE_XPATH}'))
        )
        value = browser.find_element_by_xpath(f'{THE_XPATH}').text
        print('BUSINESS NAME: ', value)
        data['Business Name'] = value
    except(AttributeError, TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
        print('cant extract summery business name')

    # summery RTO type
    try:
        THE_XPATH = '//*[@id="rtoDetails-1"]//div[contains(text(),"RTO type:")]/following-sibling::div'
        WebDriverWait(browser, 1).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, f'{THE_XPATH}'))
        )
        value = browser.find_element_by_xpath(f'{THE_XPATH}').text
        print('RTO type: ', value)
        data['RTO/Type'] = value
    except(AttributeError, TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
        print('cant extract summery RTO/type')

    # CONTACTS SECTION

    # click on contact tab
    try:
        browser.execute_script("arguments[0].click();", WebDriverWait(browser, 2).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="detailsContactsTab"]'))))
    except TimeoutException:
        print('contact timeout error')

    # Chief Executive Name
    try:
        THE_XPATH = '//*[@id="rtoDetails-3"]//h2[contains(text(), "Chief Executive")]/parent::div/descendant::div[contains(text(), "Contact name:")]/following-sibling::div'
        WebDriverWait(browser, 1).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, f'{THE_XPATH}'))
        )
        value = browser.find_element_by_xpath(f'{THE_XPATH}').text
        print('Chief Executive Name: ', value)
        data['Chief Executive Name'] = value
    except(AttributeError, TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
        print('cant extract Chief Executive Name')

    # Chief Executive Email
    try:
        THE_XPATH = '//*[@id="rtoDetails-3"]//h2[contains(text(), "Chief Executive")]/parent::div/descendant::div[contains(text(), "Email:")]/following-sibling::div'
        WebDriverWait(browser, 1).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, f'{THE_XPATH}'))
        )
        value = browser.find_element_by_xpath(f'{THE_XPATH}').text
        print('Chief Executive Email: ', value)
        data['Chief Executive Email'] = value
    except(AttributeError, TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
        print('cant extract Chief Executive Email')

    # Chief Executive h/p No.
    try:
        THE_XPATH = '//*[@id="rtoDetails-3"]//h2[contains(text(), "Chief Executive")]/parent::div/descendant::div[contains(text(), "Mobile:")]/following-sibling::div'
        WebDriverWait(browser, 1).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, f'{THE_XPATH}'))
        )
        value = browser.find_element_by_xpath(f'{THE_XPATH}').text
        print('Chief Executive h/p No: ', value)
        data['Chief Executive h/p No.'] = value
    except(AttributeError, TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
        print('cant extract Chief Executive h/p No.')

    # Registration Enquiries Name
    try:
        THE_XPATH = '//*[@id="rtoDetails-3"]//h2[contains(text(), "Registration Enquiries")]/parent::div/descendant::div[contains(text(), "Contact name:")]/following-sibling::div'
        WebDriverWait(browser, 1).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, f'{THE_XPATH}'))
        )
        value = browser.find_element_by_xpath(f'{THE_XPATH}').text
        print('Registration Enquiries Name: ', value)
        data['Registration Enquiries Name'] = value
    except(AttributeError, TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
        print('cant extract Registration Enquiries Name')

    # Registration Enquiries Email
    try:
        THE_XPATH = '//*[@id="rtoDetails-3"]//h2[contains(text(), "Registration Enquiries")]/parent::div/descendant::div[contains(text(), "Email:")]/following-sibling::div'
        WebDriverWait(browser, 1).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, f'{THE_XPATH}'))
        )
        value = browser.find_element_by_xpath(f'{THE_XPATH}').text
        print('Registration Enquiries Email: ', value)
        data['Registration Enquiries Email'] = value
    except(AttributeError, TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
        print('cant extract Registration Enquiries Email')

    # Registration Enquiries h/p No.
    try:
        THE_XPATH = '//*[@id="rtoDetails-3"]//h2[contains(text(), "Registration Enquiries")]/parent::div/descendant::div[contains(text(), "Mobile:")]/following-sibling::div'
        WebDriverWait(browser, 1).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, f'{THE_XPATH}'))
        )
        value = browser.find_element_by_xpath(f'{THE_XPATH}').text
        print('Registration Enquiries h/p No: ', value)
        data['Registration Enquiries h/p No.'] = value
    except(AttributeError, TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
        print('cant extract Registration Enquiries h/p No.')


    # Public Enquiries Name
    try:
        THE_XPATH = '//*[@id="rtoDetails-3"]//h2[contains(text(), "Public Enquiries")]/parent::div/descendant::div[contains(text(), "Contact name:")]/following-sibling::div'
        WebDriverWait(browser, 1).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, f'{THE_XPATH}'))
        )
        value = browser.find_element_by_xpath(f'{THE_XPATH}').text
        print('Public Enquiries Name: ', value)
        data['Public Enquiries Name'] = value
    except(AttributeError, TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
        print('cant extract Public Enquiries Name')

    # Public Enquiries Email
    try:
        THE_XPATH = '//*[@id="rtoDetails-3"]//h2[contains(text(), "Public Enquiries")]/parent::div/descendant::div[contains(text(), "Email:")]/following-sibling::div'
        WebDriverWait(browser, 1).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, f'{THE_XPATH}'))
        )
        value = browser.find_element_by_xpath(f'{THE_XPATH}').text
        print('Public Enquiries Email: ', value)
        data['Public Enquiries Email'] = value
    except(AttributeError, TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
        print('cant extract Public Enquiries Email')

    # Public Enquiries h/p No.
    try:
        THE_XPATH = '//*[@id="rtoDetails-3"]//h2[contains(text(), "Public Enquiries")]/parent::div/descendant::div[contains(text(), "Mobile:")]/following-sibling::div'
        WebDriverWait(browser, 1).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, f'{THE_XPATH}'))
        )
        value = browser.find_element_by_xpath(f'{THE_XPATH}').text
        print('Public Enquiries h/p No: ', value)
        data['Public Enquiries h/p No.'] = value
    except(AttributeError, TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
        print('cant extract Public Enquiries h/p No.')
