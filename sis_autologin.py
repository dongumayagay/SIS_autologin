from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

credentials = dict(username='', month='', day='', year='', password='')

driver = webdriver.Chrome('chromedriver.exe')

url = driver.get('https://sis1.pup.edu.ph/students/')
try:
    login: object = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[3]/td/div[2]/input[1]")))
except:
    driver.quit()
driver.find_element_by_name('txtUser').send_keys(credentials['username'])
driver.find_element_by_name('cboMonth').send_keys(credentials['month'])
driver.find_element_by_name('cboDay').send_keys(credentials['day'])
driver.find_element_by_name('cboYear').send_keys(credentials['year'])
driver.find_element_by_name('txtPwd').send_keys(credentials['password'])
driver.find_element_by_id('checkbox_ra10931').click()
login.click()
driver.get(('/'.join([text if index != len((driver.current_url).split('/'))-1  else 'grades.php' for index, text in enumerate((driver.current_url).split('/'))])))