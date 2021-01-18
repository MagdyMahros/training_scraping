"""Description:
    * author: Magdy Abdelkader
    * company: Fresh Futures/Seeka Technology
    * position: IT Intern
    * date: 11-01-21
    * description:This script scrape the school address from each school at training.gov.au
"""
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
import os
import copy
import csv
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
csv_file = csv_file_path.__str__() + '/address.csv'

data = {'Code': '', 'Address': ''}

course_data_all = []

# GET EACH COURSE LINK
for each_url in links_file:
    browser.get(each_url)
    pure_url = each_url.strip()
    each_url = browser.page_source
    soup = bs4.BeautifulSoup(each_url, 'lxml')
    time.sleep(1)

    # SUMMERY SECTION
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

    # ADDRESS SECTION
    # click on contact tab
    try:
        browser.execute_script("arguments[0].click();", WebDriverWait(browser, 2).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="detailsAddressesTab"]'))))
    except TimeoutException:
        print('address timeout error')

    try:
        THE_XPATH = '//*[@id="rtoDetails-4"]//h2[contains(text(), "Head office address")]/following-sibling::div/descendant::div[contains(text(), "Physical address:")]/following-sibling::div'
        WebDriverWait(browser, 1).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, f'{THE_XPATH}'))
        )
        value = browser.find_element_by_xpath(f'{THE_XPATH}').text.replace('\n', ' ')
        print('ADDRESS: ', value)
        data['Address'] = value
    except(AttributeError, TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
        print('cant extract address')

    # TABULATE THE DATA
    course_data_all.append(copy.deepcopy(data))
    desired_order_list = ['Code', 'Address']

    course_dict_keys = set().union(*(d.keys() for d in course_data_all))

    with open(csv_file, 'w', encoding='utf-8', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, course_dict_keys)
        dict_writer.writeheader()
        dict_writer.writerows(course_data_all)

    with open(csv_file, 'r', encoding='utf-8') as infile, open('address_ordered.csv', 'w', encoding='utf-8',
                                                               newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=desired_order_list)
        # reorder the header first
        writer.writeheader()
        for row in csv.DictReader(infile):
            # writes the reordered rows to the new file
            writer.writerow(row)
