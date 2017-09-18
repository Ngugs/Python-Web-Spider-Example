from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
#from wait_for import wait_for
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
def link_has_gone_stale(link_text,br):
    try:
        br.find_element_by_link_text(link_text) 
        return False
    except StaleElementReferenceException:
        return True
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 50)
driver.get('https://www.linkedin.com/')
#driver.get('https://www.linkedin.com/search/results/people/?facetGeoRegion=[%22gb%3A0%22]&facetNetwork=[%22F%22%2C%22S%22]&origin=FACETED_SEARCH')
try:
    #links = driver.find_elements_by_tag_name('a')
    #for link in links:
        #if link.get_attribute('href')== 'https://www.linkedin.com/login/#':
            #link.click()
    #link = driver.find_element_by_link_text('Sign in')
    #link= wait.until(EC.presence_of_element_located((By.LINK_TEXT,'Sign in')))
    #link.click() 
    #wait_for('Sign in',driver)
    #driver.find_element_by_xpath('//*[@id="uno-reg-join"]/div/div/div/div[2]/div[1]/div/div/p/a')
    #signinlink = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="uno-reg-join"]/div/div/div/div[2]/div[1]/div/div/p/a')))
    #signinlink.click()
    boxid = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-email"]')))
    boxpass = driver.find_element_by_xpath('//*[@id="login-password"]')
    buttonpost = driver.find_element_by_xpath('//*[@id="login-submit"]')
    boxid.clear()
    boxpass.clear()
    boxid.send_keys("@.com")
    boxpass.send_keys("xxx!")
    buttonpost.click()
    #name1= wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'name actor-name')))
    #actornames = driver.find_element_by_class_name('name actor-name')          
    #print len(actornames)
    #print driver.title
    #assert "LinkedIn" in driver.title
    #driver.find_element_by_id('nav-settings__dropdown-trigger').click()
    #wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ember3681"]'))).click()
    #driver.find_element_by_xpath('//*[@id="ember3681"]').click()
    #driver.execute_script("document.getElementById('ember3613').click();",driver.find_element_by_id('ember3613'))
    time.sleep(20)
    actions = ActionChains(driver)
    about = driver.find_element_by_link_text('About')
    actions.key_down(Keys.CONTROL).click(about).key_up(Keys.CONTROL).perform()
    driver.switch_to.window(driver.window_handles[-1])
    driver.get('https://www.linkedin.com/search/results/people/?facetGeoRegion=[%22gb%3A0%22]&facetNetwork=[%22F%22%2C%22S%22]&origin=FACETED_SEARCH')
    time.sleep(20)
    pros = driver.find_element_by_id('ember1889')
    print pros.text
    driver.quit()
except TimeoutException:
        print "dddddd"

