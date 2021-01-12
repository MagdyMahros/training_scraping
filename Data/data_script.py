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
csv_file = csv_file_path.__str__() + '/training_gov_data.csv'

data = {'Code': '', 'Legal Name': '', 'Business Name': '', 'RTO/Type': '', 'Chief Executive Name': '',
        'Chief Executive Email': '', 'Chief Executive h/p No.': '', 'Registration Enquiries Name': '',
        'Registration Enquiries Email': '', 'Registration Enquiries h/p No.': '', 'Public Enquiries Name': '',
        'Public Enquiries Email': '', 'Public Enquiries h/p No.': '',
        'Qualifications Code 1': '', 'Qualifications title 1': '', 'Qualifications states 1': '',
        'Qualifications Code 2': '', 'Qualifications title 2': '', 'Qualifications states 2': '',
        'Qualifications Code 3': '', 'Qualifications title 3': '', 'Qualifications states 3': '',
        'Qualifications Code 4': '', 'Qualifications title 4': '', 'Qualifications states 4': '',
        'Qualifications Code 5': '', 'Qualifications title 5': '', 'Qualifications states 5': '',
        'Qualifications Code 6': '', 'Qualifications title 6': '', 'Qualifications states 6': '',
        'Qualifications Code 7': '', 'Qualifications title 7': '', 'Qualifications states 7': '',
        'Qualifications Code 8': '', 'Qualifications title 8': '', 'Qualifications states 8': '',
        'Qualifications Code 9': '', 'Qualifications title 9': '', 'Qualifications states 9': '',
        'Qualifications Code 10': '', 'Qualifications title 10': '', 'Qualifications states 10': '',
        'Qualifications Code 11': '', 'Qualifications title 11': '', 'Qualifications states 11': '',
        'Qualifications Code 12': '', 'Qualifications title 12': '', 'Qualifications states 12': '',
        'Qualifications Code 13': '', 'Qualifications title 13': '', 'Qualifications states 13': '',
        'Qualifications Code 14': '', 'Qualifications title 14': '', 'Qualifications states 14': '',
        'Qualifications Code 15': '', 'Qualifications title 15': '', 'Qualifications states 15': '',
        'Qualifications Code 16': '', 'Qualifications title 16': '', 'Qualifications states 16': '',
        'Qualifications Code 17': '', 'Qualifications title 17': '', 'Qualifications states 17': '',
        'Qualifications Code 18': '', 'Qualifications title 18': '', 'Qualifications states 18': '',
        'Qualifications Code 19': '', 'Qualifications title 19': '', 'Qualifications states 19': '',
        'Qualifications Code 20': '', 'Qualifications title 20': '', 'Qualifications states 20': '',
        'Qualifications Code 21': '', 'Qualifications title 21': '', 'Qualifications states 21': '',
        'Qualifications Code 22': '', 'Qualifications title 22': '', 'Qualifications states 22': '',
        'Qualifications Code 23': '', 'Qualifications title 23': '', 'Qualifications states 23': '',
        'Qualifications Code 24': '', 'Qualifications title 24': '', 'Qualifications states 24': '',
        'Qualifications Code 25': '', 'Qualifications title 25': '', 'Qualifications states 25': '',
        'Qualifications Code 26': '', 'Qualifications title 26': '', 'Qualifications states 26': '',
        'Qualifications Code 27': '', 'Qualifications title 27': '', 'Qualifications states 27': '',
        'Qualifications Code 28': '', 'Qualifications title 28': '', 'Qualifications states 28': '',
        'Qualifications Code 29': '', 'Qualifications title 29': '', 'Qualifications states 29': '',
        'Qualifications Code 30': '', 'Qualifications title 30': '', 'Qualifications states 30': '',
        'Qualifications Code 31': '', 'Qualifications title 31': '', 'Qualifications states 31': '',
        'Qualifications Code 32': '', 'Qualifications title 32': '', 'Qualifications states 32': '',
        'Qualifications Code 33': '', 'Qualifications title 33': '', 'Qualifications states 33': '',
        'Qualifications Code 34': '', 'Qualifications title 34': '', 'Qualifications states 34': '',
        'Qualifications Code 35': '', 'Qualifications title 35': '', 'Qualifications states 35': '',
        'Qualifications Code 36': '', 'Qualifications title 36': '', 'Qualifications states 36': '',
        'Qualifications Code 37': '', 'Qualifications title 37': '', 'Qualifications states 37': '',
        'Qualifications Code 38': '', 'Qualifications title 38': '', 'Qualifications states 38': '',
        'Qualifications Code 39': '', 'Qualifications title 39': '', 'Qualifications states 39': '',
        'Qualifications Code 40': '', 'Qualifications title 40': '', 'Qualifications states 40': ''}

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

    # SCOPE SECTION

    # click the scope tab
    try:
        browser.execute_script("arguments[0].click();", WebDriverWait(browser, 2).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="detailsScopeTab"]'))))
    except TimeoutException:
        print('scope timeout error')
    time.sleep(2)

    # click the 50 button to display the 50 rows
    try:
        browser.execute_script("arguments[0].click();", WebDriverWait(browser, 2).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="ScopeQualification"]/table/tfoot/tr/td/div[3]/span[3]'))))
    except TimeoutException:
        print('scope table timeout error at 50')
        try:
            browser.execute_script("arguments[0].click();", WebDriverWait(browser, 2).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="ScopeQualification"]/table/tfoot/tr/td/div[3]/span[2]'))))
        except TimeoutException:
            print('scope table timeout error at 20')
            pass
    time.sleep(2)
    # scope Qualifications table
    try:
        THE_XPATH = '//*[@id="rtoDetails-5"]//h3[contains(text(), "Qualifications")]/following-sibling::div/table/tbody'
        WebDriverWait(browser, 1).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, f'{THE_XPATH}'))
        )
        table = browser.find_element_by_xpath(f'{THE_XPATH}')
        table_rows = table.find_elements_by_tag_name('tr')
        i = 1
        for tr in table_rows:
            city_list = []
            td_list = tr.find_elements_by_tag_name('td')
            for index, td in enumerate(td_list, start=1):
                if index == 1:
                    data[f'Qualifications Code {i}'] = td.text
                    print(f'Qualifications Code {i}: ', td.text)
                if index == 2:
                    data[f'Qualifications title {i}'] = td.text
                    print(f'Qualifications title {i}: ', td.text)
                if index == 4:
                    city = browser.find_element_by_xpath(
                        f'//*[@id="ScopeQualification"]/table/tbody/tr[{i}]/td[{index}]/span').get_attribute(
                        "textContent")
                    if city == 'Yes':
                        city_list.append('NSW')
                    # print('NSW: ', city)
                if index == 5:
                    city = browser.find_element_by_xpath(
                        f'//*[@id="ScopeQualification"]/table/tbody/tr[{i}]/td[{index}]/span').get_attribute(
                        "textContent")
                    if city == 'Yes':
                        city_list.append('VIC')
                    # print('VIC: ' + city)
                if index == 6:
                    city = browser.find_element_by_xpath(
                        f'//*[@id="ScopeQualification"]/table/tbody/tr[{i}]/td[{index}]/span').get_attribute(
                        "textContent")
                    if city == 'Yes':
                        city_list.append('QLD')
                    # print('QLD: ' + city)
                if index == 7:
                    city = browser.find_element_by_xpath(
                        f'//*[@id="ScopeQualification"]/table/tbody/tr[{i}]/td[{index}]/span').get_attribute(
                        "textContent")
                    if city == 'Yes':
                        city_list.append('SA')
                    # print('SA: ' + city)
                if index == 8:
                    city = browser.find_element_by_xpath(
                        f'//*[@id="ScopeQualification"]/table/tbody/tr[{i}]/td[{index}]/span').get_attribute(
                        "textContent")
                    if city == 'Yes':
                        city_list.append('WA')
                    # print('WA: ' + city)
                if index == 9:
                    city = browser.find_element_by_xpath(
                        f'//*[@id="ScopeQualification"]/table/tbody/tr[{i}]/td[{index}]/span').get_attribute(
                        "textContent")
                    if city == 'Yes':
                        city_list.append('TAS')
                    # print('TAS: ' + city)
                if index == 10:
                    city = browser.find_element_by_xpath(
                        f'//*[@id="ScopeQualification"]/table/tbody/tr[{i}]/td[{index}]/span').get_attribute(
                        "textContent")
                    if city == 'Yes':
                        city_list.append('NT')
                    # print('NT: ' + city)
                if index == 11:
                    city = browser.find_element_by_xpath(
                        f'//*[@id="ScopeQualification"]/table/tbody/tr[{i}]/td[{index}]/span').get_attribute(
                        "textContent")
                    if city == 'Yes':
                        city_list.append('ACT')
                    # print('ACT: ' + city)
            city_list = ' / '.join(city_list)
            print("CITIES: ", city_list)
            data[f'Qualifications states {i}'] = city_list
            i += 1
            if i == 40:
                break
    except(AttributeError, TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
        print(f'some error happened when finding the table. {e}')

    # TABULATE THE DATA
    course_data_all.append(copy.deepcopy(data))
    desired_order_list = ['Code', 'Legal Name', 'Business Name', 'RTO/Type', 'Chief Executive Name',
                          'Chief Executive Email', 'Chief Executive h/p No.', 'Registration Enquiries Name',
                          'Registration Enquiries Email', 'Registration Enquiries h/p No.', 'Public Enquiries Name',
                          'Public Enquiries Email', 'Public Enquiries h/p No.',
                          'Qualifications Code 1', 'Qualifications title 1', 'Qualifications states 1',
                          'Qualifications Code 2', 'Qualifications title 2', 'Qualifications states 2',
                          'Qualifications Code 3', 'Qualifications title 3', 'Qualifications states 3',
                          'Qualifications Code 4', 'Qualifications title 4', 'Qualifications states 4',
                          'Qualifications Code 5', 'Qualifications title 5', 'Qualifications states 5',
                          'Qualifications Code 6', 'Qualifications title 6', 'Qualifications states 6',
                          'Qualifications Code 7', 'Qualifications title 7', 'Qualifications states 7',
                          'Qualifications Code 8', 'Qualifications title 8', 'Qualifications states 8',
                          'Qualifications Code 9', 'Qualifications title 9', 'Qualifications states 9',
                          'Qualifications Code 10', 'Qualifications title 10', 'Qualifications states 10',
                          'Qualifications Code 11', 'Qualifications title 11', 'Qualifications states 11',
                          'Qualifications Code 12', 'Qualifications title 12', 'Qualifications states 12',
                          'Qualifications Code 13', 'Qualifications title 13', 'Qualifications states 13',
                          'Qualifications Code 14', 'Qualifications title 14', 'Qualifications states 14',
                          'Qualifications Code 15', 'Qualifications title 15', 'Qualifications states 15',
                          'Qualifications Code 16', 'Qualifications title 16', 'Qualifications states 16',
                          'Qualifications Code 17', 'Qualifications title 17', 'Qualifications states 17',
                          'Qualifications Code 18', 'Qualifications title 18', 'Qualifications states 18',
                          'Qualifications Code 19', 'Qualifications title 19', 'Qualifications states 19',
                          'Qualifications Code 20', 'Qualifications title 20', 'Qualifications states 20',
                          'Qualifications Code 21', 'Qualifications title 21', 'Qualifications states 21',
                          'Qualifications Code 22', 'Qualifications title 22', 'Qualifications states 22',
                          'Qualifications Code 23', 'Qualifications title 23', 'Qualifications states 23',
                          'Qualifications Code 24', 'Qualifications title 24', 'Qualifications states 24',
                          'Qualifications Code 25', 'Qualifications title 25', 'Qualifications states 25',
                          'Qualifications Code 26', 'Qualifications title 26', 'Qualifications states 26',
                          'Qualifications Code 27', 'Qualifications title 27', 'Qualifications states 27',
                          'Qualifications Code 28', 'Qualifications title 28', 'Qualifications states 28',
                          'Qualifications Code 29', 'Qualifications title 29', 'Qualifications states 29',
                          'Qualifications Code 30', 'Qualifications title 30', 'Qualifications states 30',
                          'Qualifications Code 31', 'Qualifications title 31', 'Qualifications states 31',
                          'Qualifications Code 32', 'Qualifications title 32', 'Qualifications states 32',
                          'Qualifications Code 33', 'Qualifications title 33', 'Qualifications states 33',
                          'Qualifications Code 34', 'Qualifications title 34', 'Qualifications states 34',
                          'Qualifications Code 35', 'Qualifications title 35', 'Qualifications states 35',
                          'Qualifications Code 36', 'Qualifications title 36', 'Qualifications states 36',
                          'Qualifications Code 37', 'Qualifications title 37', 'Qualifications states 37',
                          'Qualifications Code 38', 'Qualifications title 38', 'Qualifications states 38',
                          'Qualifications Code 39', 'Qualifications title 39', 'Qualifications states 39',
                          'Qualifications Code 40', 'Qualifications title 40', 'Qualifications states 40']

    course_dict_keys = set().union(*(d.keys() for d in course_data_all))

    with open(csv_file, 'w', encoding='utf-8', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, course_dict_keys)
        dict_writer.writeheader()
        dict_writer.writerows(course_data_all)

    with open(csv_file, 'r', encoding='utf-8') as infile, open('training_gov_data_ordered.csv', 'w', encoding='utf-8',
                                                               newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=desired_order_list)
        # reorder the header first
        writer.writeheader()
        for row in csv.DictReader(infile):
            # writes the reordered rows to the new file
            writer.writerow(row)
