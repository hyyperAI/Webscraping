from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
service = Service("C:\Windows\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org")
# x=driver.find_element(by="name",value="q")
# print(x.size)

search_bar=(driver.find_element(By.XPATH,value='//*[@id="id-search-field"]'))
print(search_bar.size)


# submit_button=driver.find_element(By.CSS_SELECTOR,"container")
""" id =site-map second div then another div , untitled-list in which third number of list  and then anchor tag  """
# submit_button=driver.find_element(By.XPATH,'//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(submit_button.text)

# x=driver.find_elements(By.ID,"site-map")
# for item in x:
#     try:
#         item.find_element(By.TAG_NAME,"li")
#     except:
#         print("not found")
try:
    y=((driver.find_element(By.CLASS_NAME,"site-base  ")))
    print((y.find_element(By.CLASS_NAME,'element-3')).text)
except:
    print("Submit button not found")

try:
    z=driver.find_elements(By.CLASS_NAME,"container")
    print((z.find_element(By.CLASS_NAME,"tier-1 element-2 a")).text)
except:
    print("not found")