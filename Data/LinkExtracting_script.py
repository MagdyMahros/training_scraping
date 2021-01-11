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
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import os
import time

option = webdriver.ChromeOptions()
option.add_argument(" - incognito")
option.add_argument("headless")
exec_path = Path(os.getcwd().replace('\\', '/'))
exec_path = exec_path.parent.__str__() + '/Libraries/Google/v86/chromedriver.exe'
browser = webdriver.Chrome(executable_path=exec_path, options=option)

page_url = 'https://training.gov.au/Search/SearchOrganisation?Name=&IncludeUnregisteredRtos=false&IncludeNotRtos=false&orgSearchByNameSubmit=Search&AdvancedSearch=&JavaScriptEnabled=true'
links_list = []
browser.get(page_url)
delay_ = 5  # seconds

# # display 100 raws of data
# try:
#     browser.execute_script("arguments[0].click();", WebDriverWait(browser, delay_).until(
#         EC.element_to_be_clickable(
#             (By.XPATH, '//*[@id="gridRtoSearchResults"]/table/tfoot/tr/td/div[3]/a[3]'))))
# except NoSuchElementException:
#     pass
# time.sleep(3)

# KEEP CLICKING UNTIL THERE IS NO BUTTON
condition = True
while condition:
    try:
        # extract all the links to list
        links_xpath = '//*[@id="gridRtoSearchResults"]/table/descendant::a[starts-with(@title,"View Details for RTO Code")]'
        data_list = browser.find_elements_by_xpath(f'{links_xpath}')
        for a in data_list:
            link = a.get_attribute('href')
            if link not in links_list:
                links_list.append(link)
        time.sleep(1)
        browser.execute_script("arguments[0].click();", WebDriverWait(browser, delay_).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="gridRtoSearchResults"]/table/tfoot/tr/td/div[2]/a[3]/span'))))
    except TimeoutException:
        condition = False
    print(len(links_list))
    if len(links_list) == 4044:
        condition = False

# SAVE TO FILE
links_file_path = os.getcwd().replace('\\', '/') + '/links.txt'
links_file = open(links_file_path, 'w')
for link in links_list:
    if link is not None and link != "" and link != "\n":
        if link == links_list[-1]:
            links_file.write(link.strip())
        else:
            links_file.write(link.strip() + '\n')
links_file.close()
