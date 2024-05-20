from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# open the browser after the program run
chrome_option=webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

# open the website by url
driver=webdriver.Chrome(options=chrome_option)
driver.get(url="https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location="
               "London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
time.sleep(1)
# sign-in to the linkedIn account
EMAIL="YOUR EMAIL"
PASSWORD="YOUR PASSWORD"
signin=driver.find_element(By.XPATH,value="/html/body/div[1]/header/nav/div/a[2]")
signin.click()
time.sleep(1)
email=driver.find_element(By.ID,value="username")
email.send_keys(EMAIL)
time.sleep(1)
password=driver.find_element(By.ID,value="password")
password.send_keys(PASSWORD)
time.sleep(1)
signin_button=driver.find_element(By.XPATH,value='//*[@id="organic-div"]/form/div[3]/button')
signin_button.click()
time.sleep(3)

# apply for the first job
first_job=driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li[1]/div/div')
first_job.click()

# click on easy apply
time.sleep(2)
easy_apply=driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[5]/div/div/div/button/span')
easy_apply.click()

# phone number input for job application
time.sleep(2)
ph_no=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div[4]/div/div/div[1]/div/input')
ph_no.send_keys("1234567890")

# next button
time.sleep(1)
next_button=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button/span')
next_button.click()

# review button
time.sleep(1)
review_button=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]/span')
review_button.click()

# submit application
time.sleep(2)
submit=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]/span')
submit.click()

time.sleep(3)
driver.quit()