import pandas as pd
from selenium import webdriver
import time
import threading
from selenium.webdriver.common.keys import Keys
import predicting_part
import config
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
def loginAndCreateTickets(text1, text2):
    inc_id=503
    try:
        
        config.logger.info('Logging into ITSM tool for generating ticket')
        options = Options() 
        options.headless = True
        options.add_argument("--window-size=1920,1200")
        driver = webdriver.Chrome(options=options,executable_path=ChromeDriverManager().install())
#         driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        # Gets the URL 
        print("Opening browser with ITSM")
        # Gets the URL 
        driver.get('https://staging-ci.symphonysummit.com/Afsservicedesk/Summit_WebLogin.aspx')
        
        driver.maximize_window()
        
        time.sleep(3)
        
        # Finds the user name and password by id from HTML
        element = driver.find_element_by_id("txtLogin")
        element1 = driver.find_element_by_id("txtPassword")
        
        # Enters the user name and password
        element.send_keys("afsauto@aforeserve.co.in")
        element1.send_keys("Afs@123#")
        
        # Clicks the login button
        driver.find_element_by_id("butSubmit").click()
        print("login complete")
        
        # This is used to check if a duplicate login window pop ups, if it does press continue otherwise pass 
        try:
            if driver.find_element_by_class_name("TitlePanel").text == 'DUPLICATE LOGIN':
                driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
                driver.find_element_by_id("ContentPanel_btnContinue").click()
            else:
                pass
        except:
            print(" ")
        
        time.sleep(1)
        driver.find_element_by_id("IM").click()
        driver.find_element_by_id("IM_LOG_TICKET").click()
        print("inside create new incident")
    except Exception as e:
        
        config.logger.exception('Error in logging into ITSM tool for generating ticket')
    try:
        element2 = driver.find_element_by_id("BodyContentPlaceHolder_txtSymptom")
        element3 = driver.find_element_by_class_name("nicEdit-main")
        element2.send_keys(text1)
        print("entering symptom")
        element3.send_keys(text2)
        print("entering Details")
        time.sleep(3)
        driver.find_element_by_id("BodyContentPlaceHolder_btnSave").click()
        print("submit clicked")
        time.sleep(5)
        driver.find_element_by_class_name("bootbox-close-button").click()
        print("closing page")
        time.sleep(2)
        driver.find_element_by_id("IM").click()
        driver.find_element_by_id("IM_MY_TICKETS").click()
        print("inside insident list")
        time.sleep(5)
        try:
#             id="BodyContentPlaceHolder_gvMyTickets"
            
            inc_id = driver.find_element_by_xpath('//*[@id="BodyContentPlaceHolder_gvMyTickets"]/tbody/tr[3]/td[1]/a[1]').text
            print("storing incident id")
            
        except:
            print("fail to get id")
            config.logger.exception('Error in storing attributes of a ticket ')      
    except:
        print("fail to generate ticket")
        inc_id = 0
        config.logger.exception('error in generating ticket')
        pass
    driver.find_element_by_xpath('//*[@id="imgProfile"]').click()
    driver.find_element_by_xpath('//*[@id="hrefLogout"]').click()
    print("Log Out complete and Task Successfull")
    driver.quit()
    
    #threading.Timer(180, loginAndFetchTickets).start()
    
    return inc_id
