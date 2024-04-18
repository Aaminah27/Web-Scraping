from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd

website = 'https://www.adamchoi.co.uk/overs/detailed'
driver = webdriver.Chrome()
driver.get(website)

all_matches_button = driver.find_element(By.XPATH, "//label[@analytics-event='All matches']")
all_matches_button.click()

#we needed to use Select as the dropdown we are dealing with is dynamic and may have ajax behind it
dropdown = Select(driver.find_element(By.ID,'country'))
#selecting dropdown by what we see on the web page
dropdown.select_by_visible_text('Spain')
#as after selecting country, the web page takes some time to load the required information
time.sleep(3)
matches = driver.find_elements(By.TAG_NAME,'tr')

date=[]
home_team=[]
score =[]
away_team=[]

for match in matches:
    print(match.text)
    #here print returns data in form 12-08-2023 Arsenal 2 - 1 Nott'm Forest
    #now for each row are going to get each column separately
    #in xpath indexes start from 1 rather than 0 so to get date we need to access first index
    date.append(match.find_element(By.XPATH, './td[1]').text)
    home_team.append(match.find_element(By.XPATH, './td[2]').text)
    score.append(match.find_element(By.XPATH, './td[3]').text)
    away_team.append(match.find_element(By.XPATH, './td[4]').text)


driver.quit()

df = pd.DataFrame({'date':date,'home_team':home_team,'score':score,'away_team':away_team})
df.to_csv('football_scores.csv',index=False)
print(df)
