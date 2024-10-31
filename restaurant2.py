from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import pandas as pd



# Set up the Chrome driver
service = Service("C:/ProgramData/chocolatey/lib/chromedriver/tools/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)


driver.get("https://www.zomato.com/ncr/trending-this-week")





soup = BeautifulSoup(driver.page_source, "html.parser")


# data = {'link': []}

data = {'rating':[]}

# link = soup.find_all("a" ,class_="sc-edGvlf")

# for links in link:
#   print(links.string)

# links = [a.get('href') for a in soup.find_all('a',class_='sc-edGvlf')]

for rat in soup.find_all(class_="cILgox"):
    print(str(rat))
    data['rating'].append(str(rat))






# Print links as strings
# for link in links:
#     print(str(link))
#     data['link'].append(str(link))

# rating= soup.find_all("div", class_="kcEtBq")
# for rat in rating:
#    print(rat.get_text())
#    data['rating'].append(rat.get_text())


driver.quit()


df = pd.DataFrame.from_dict(data)
df.to_csv("rating.csv", index=False)
print("Data saved to rating.csv")