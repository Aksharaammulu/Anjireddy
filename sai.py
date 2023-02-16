import time
import logging
import azure.functions as func
from azure.storage.blob import BlobServiceClient
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
URL = 'https://www.linkedin.com/login'
URl1 = 'https://www.linkedin.com/authwall?trk=bf&trkInfo=AQGe_PNM6JL4FAAAAYTgf5coz8Hg0kNtYRzUE4ZqNg74fAJQXZp1YCLV0Mi67TPYr9Q8q-r7LeFj_eZLl_Oqpe1K-AgdlYb9D1rDUEIgSaSrH0f_y5FN9Vt9hHYBrvZJ8D-N4zs=&original_referer=&sessionRedirect=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fgoutam-sahu-b8721b92%2Fdetails%2Fskills%2F'
driver.get(URL)
username = driver.find_element(By.XPATH, '//input[@id="username"]').send_keys('aksharaammulu9@gmail.com')
password = driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('Tanubuddy@2016')
time.sleep(3)
driver.find_element(By.XPATH, "//button[text()='Sign in']").click()
time.sleep(30)
driver.find_element(By.XPATH, '//div[@class="t-16 t-black t-bold"]').click()
time.sleep(3)
driver.execute_script("return arguments[0].scrollIntoView();", driver.find_element(By.XPATH, '//*[text()="Skills"]//parent::span[@aria-hidden="true"]'))
time.sleep(3)
driver.find_element(By.XPATH, '//*[text()="Microsoft Azure"]//parent::span[@aria-hidden="true"]').is_displayed()
time.sleep(3)
driver.find_element(By.XPATH, '//*[text()="Microsoft Azure"]//parent::span[@aria-hidden="true"]').text

input=['https://www.linkedin.com/in/goutam-sahu-b8721b92/details/skills/',
'https://www.linkedin.com/in/tejas-sonune-859835198/','https://www.linkedin.com/in/prateek-koul-1b4791134/',
'https://www.linkedin.com/in/saipreethi-reddy-a81053220',
'https://www.linkedin.com/in/swetha-vasudevan-1aa00b191',
'//https:www.linkedin.com/in/rohan-somadder/',
'https://www.linkedin.com/in/rahul-deshmukh-26083a184',
'//https:www.linkedin.com/in/nagashree-b-79bb9020b',
'//https:www.linkedin.com/in/aayush2095/',
'https://www.linkedin.com/in/mohammed-mustafa-9684b0189']
# for i in input:
#     driver.get(i)
#     if (i==driver.find_element(By.XPATH, '//*[text()="Microsoft Azure"]//parent::span[@aria-hidden="true"]').text):
#         print('yes')
#     else:
#         print('no')
# time.sleep(30)
print(len(input))
i=1
while i<=len(input):
    driver.execute_script("window.open('');") 
    driver.switch_to.window(driver.window_handles[1])
    driver.get(input)
    text=driver.find_element(By.XPATH, '//*[text()="Microsoft Azure"]//parent::span[@aria-hidden="true"]').text
    t1='Microsoft Azure'
    if text==t1:
        print('yes')
    else:
        print('no')
i=i+1
print(i)

# create blob service client and container client
credential = DefaultAzureCredential()
storage_account_url = "https://" + os.environ["par_storage_account_name"] + ".blob.core.windows.net"
client = BlobServiceClient(account_url=storage_account_url, credential=credential)
blob_name = "test" + str(datetime.now()) + ".txt"
blob_client = client.get_blob_client(container=os.environ["par_storage_container_name"], blob=blob_name)
blob_client.upload_blob(link_list)
