from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("C:/Users/KskYm/Downloads/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

planets_data = []

# Define Exoplanet Data Scrapping Method
def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )

        ## ADD CODE HERE ##
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for td_tag in soup.find_all('td',attrs={'class','star'}):
            tr_tags=td_tag.find_all('tr')
            temp_list=[]
            for index,tr_tag in enumerate(tr_tags):
                if index==0:
                    temp_list.append(tr_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(tr_tag.contents[0])
                    except:
                        temp_list.append('')
            planets_data.append(temp_list)
        browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        



        
# Calling Method    
scrape()

# Define Header
headers = ["name", "distance", "mass", "radius"]

# Define pandas DataFrame   

planet_df=pd.DataFrame(planets_data,columns=headers)
planet_df.to_csv('scrape_data.csv',index=True,index_label='id')
# Convert to CSV

    


