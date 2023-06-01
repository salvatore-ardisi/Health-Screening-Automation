from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
driver.get('https://www.teamworksapp.com/ext/F06F3C49-0552-8232-499474135C714145')

time.sleep(3)

elem = driver.find_element_by_xpath('//*[@id="AddEditFilterForm_name"]')
elem.send_keys('Your Name', Keys.TAB)

elem = driver.find_element_by_xpath('//*[@id="AddEditFilterForm_email"]')
elem.send_keys('Your Email', Keys.TAB)

time.sleep(2)

button = driver.find_element_by_xpath('//*[@id="AddEditFilterForm"]/div[3]/div/button')
button.click()

time.sleep(4)

consent = driver.find_element_by_xpath('//*[@id="root_I consent to University receiving a record of my completed assessment._0"]')
consent.click()

time.sleep(1)

campus = driver.find_element_by_xpath('//*[@id="root"]/span[4]/div/div[2]')
campus.click()

time.sleep(1)

pleasantville = driver.find_element_by_xpath('//*[@id="rc_select_0"]')
time.sleep(1)
pleasantville.send_keys(Keys.TAB)
pleasantville.send_keys(Keys.ENTER)
pleasantville.send_keys(Keys.ENTER)

time.sleep(1)

reason = driver.find_element_by_xpath('//*[@id="root"]/span[5]/div/textarea')
time.sleep(1)
reason.send_keys("Class")
time.sleep(1)

email = driver.find_element_by_xpath('//*[@id="root"]/span[6]/div/textarea')
time.sleep(1)
email.send_keys("Your email")
time.sleep(1)

id_number = driver.find_element_by_xpath('//*[@id="root"]/span[7]/div/textarea')
time.sleep(1)
id_number.send_keys("Your ID")
time.sleep(1)

phone = driver.find_element_by_xpath('//*[@id="root"]/span[8]/div/textarea')
time.sleep(1)
phone.send_keys("Your Phone")
time.sleep(1)

fever = driver.find_element_by_xpath('//*[@id="root"]/span[9]/div/div[2]/span[2]/label/span[1]/input')
time.sleep(1)
fever.click()
time.sleep(1)

chills = driver.find_element_by_xpath('//*[@id="root"]/span[10]/div/div[2]/span[2]/label/span[1]/input')
time.sleep(1)
chills.click()
time.sleep(1)

allergies = driver.find_element_by_xpath('//*[@id="root"]/span[11]/div/div[2]/span[2]/label/span[1]/input')
time.sleep(1)
allergies.click()
time.sleep(1)

asymptomatic = driver.find_element_by_xpath('//*[@id="root"]/span[12]/div/div[2]/span[2]/label/span[1]/input')
time.sleep(1)
asymptomatic.click()
time.sleep(1)

finish = driver.find_element_by_xpath('//*[@id="Complete_Quickform_Screen"]/div/form/div/div/button')
time.sleep(1)
finish.click()

time.sleep(5)
driver.close()
