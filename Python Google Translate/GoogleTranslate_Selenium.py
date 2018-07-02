######################################################
## Author: ANIMIKH AICH (animikhaich@gmail.com)     ##
## 12 January 2018                                  ##
## Google Translate Using Python                    ##
## RNS Institute of Technology, Bengaluru, India    ##
######################################################


import numpy as np
from selenium import webdriver
import warnings
import time
import csv


def translate(myInput, language):
    # To ignore the warning generated by PhantomJS -- Not officially supported by Selenium
    warnings.filterwarnings("ignore")

    # List of Languages supported
    f = open('./Assets/Language_List.csv', 'r')

    # Read data from csv file
    reader = csv.reader(f)
    lang_list = np.array([])
    for data in reader:
        lang_list = np.append(lang_list, data)

    # f = open('Language_List.csv','r')
    # Take input from the user and convert the language to lower for easy detection
    print('Please wait....')

    # Start measuring the time
    time_start = time.time()

    myLang = language.lower()

    # Find index of the desired language from the list
    # Set the url language code as per selected language
    index = np.where(lang_list == myLang)[0][0]
    if index % 2 == 0:
        to_lang = lang_list[index+1]
    else:
        to_lang = lang_list[index]

    # Construct the complete URL to search
    base_url = 'https://translate.google.com/#'
    from_lang = 'en'
    final_url = base_url + from_lang + '/' + to_lang

    # Initialize Selenium Driver
    # PhantomJS is used, Chrome is kept as backup for debugging
    driver = webdriver.PhantomJS('./Selenium Web Drivers/phantomjs.exe')
    # driver = webdriver.Chrome('./Selenium Web Drivers/chromedriver.exe')

    # Perform operation to detect the translated text
    driver.set_page_load_timeout(30)        # Incase Page doesn't load
    driver.get(final_url)                   # Search the URL
    driver.find_element_by_name('text').send_keys(myInput.lower())  # Input the Desired text to be translated
    # driver.find_element_by_id('gt-submit').click()          # Click on the translate button (not Mandatory)
    time.sleep(1)
    text_output = driver.find_element_by_id('result_box')   # Get the output text

    time.sleep(1)   # Else it does not print the data

    # Stop Measuring the time
    time_end = time.time()
    time_taken = time_end - time_start  # Time required
    f.close()
    print('The amount of time taken to run the script is %.3f' %time_taken)
    # driver.quit()
    return str(text_output.text)


if __name__ == '__main__':
    myInput = input('Enter the text to be translated: ')
    language = input('Enter the language to be translated to: ')
    translated_text = translate(myInput, language)
    print(translated_text)
