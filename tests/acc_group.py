# Author: Rishabh Chauhan
# License: BSD
# Location for tests  of FreeNAS new GUI
# Test case count: 4

from source import *
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


import time
import unittest
import xmlrunner
import random
try:
    import unittest2 as unittest
except ImportError:
    import unittest


xpaths = {
          'submenuGroup': '//*[@id="1-0"]',
          'newGroupName': '//*[@id="bsdgrp_group"]/mat-input-container/div/div[1]/div/input',
          'fabTrigger': '//*[@id="myFab"]/div/smd-fab-trigger/button',
          'fabAction': '//*[@id="add_action_button"]/span/mat-icon',
          'saveButton': '//*[@id="save_button"]',
          'permitsudoCheckbox': '//*[@id="bsdgrp_sudo"]/mat-checkbox/label/div'
        }

class create_group_test(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        driver.implicitly_wait(30)
        pass

    # Test navigation Account>Users>Hover>New User and enter username,fullname,password,confirmation and wait till user is  visibile in the list
    def test_01_nav_acc_group(self):
        # Click  Account menu
        print (" navigating to the group submenu")
        # Click User submenu
        driver.find_element_by_xpath(xpaths['submenuGroup']).click()
        time.sleep(2)
        # get the ui element
        ui_element1=driver.find_element_by_xpath('//*[@id="breadcrumb-bar"]/ul/li[2]/a')
        # get the weather data
        page_data=ui_element1.text
        print ("the Page now is: " + page_data)
        # assert response
        self.assertTrue("Group" in page_data)


    def test_02_create_newgroup(self):
        print (" creating a new group without root access")
        # scroll down to find hover tab
        driver.find_element_by_tag_name('html').send_keys(Keys.END)
        time.sleep(2)
        # Perform hover to show menu
        hover_element = driver.find_element_by_xpath(xpaths['fabTrigger'])
        hover = ActionChains(driver).move_to_element(hover_element)
        hover.perform()
        time.sleep(1)
        # Click create new group option
        driver.find_element_by_xpath(xpaths['fabAction']).click()
        # Enter New Groupname
        time.sleep(1)
        driver.find_element_by_xpath(xpaths['newGroupName']).send_keys(newgroupname)
        # Click on save new Group button
        driver.find_element_by_xpath(xpaths['saveButton']).click()
        # check if there is a generic error when making a duplicate group, and print the error
        self.error_check()

    def test_03_create_supergroup(self):
        print (" creating a new Super group with root access")
        time.sleep(1)
        # Click Group submenu
        driver.find_element_by_xpath(xpaths['submenuGroup']).click()
        # Perform hover to show menu
        hover_element = driver.find_element_by_xpath(xpaths['fabTrigger'])
        hover = ActionChains(driver).move_to_element(hover_element)
        hover.perform()
        time.sleep(1)
        # Click create new group option
        driver.find_element_by_xpath(xpaths['fabAction']).click()
        # Enter New Groupname
        time.sleep(1)
        driver.find_element_by_xpath(xpaths['newGroupName']).send_keys(supergroupname)
        # Check Permit Sudo  checkbox
        driver.find_element_by_xpath(xpaths['permitsudoCheckbox']).click()
        # Click on save new Group button
        driver.find_element_by_xpath(xpaths['saveButton']).click()
        # check if there is a generic error when making a duplicate group, and print the error
        self.error_check()

    def test_04_create_duplicategroup(self):
        print (" creating a duplicate group")
        # Click Group submenu
        driver.find_element_by_xpath(xpaths['submenuGroup']).click()
        # scroll down to find hover tab
        driver.find_element_by_tag_name('html').send_keys(Keys.END)
        time.sleep(2)
        # Perform hover to show menu
        hover_element = driver.find_element_by_xpath(xpaths['fabTrigger'])
        hover = ActionChains(driver).move_to_element(hover_element)
        hover.perform()
        time.sleep(1)
        # Click create new group option
        driver.find_element_by_xpath(xpaths['fabAction']).click()
        # Enter New Groupname
        time.sleep(1)
        driver.find_element_by_xpath(xpaths['newGroupName']).send_keys(newgroupname)
        # Click on save new Group button
        driver.find_element_by_xpath(xpaths['saveButton']).click()
        # check if there is a generic error when making a duplicate group, and print the error
        self.error_check()
        time.sleep(20)



    # Next step-- To check if the new user is present in the list via automation


    # method to test if an element is present
    def is_element_present(self, how, what):
        """
        Helper method to confirm the presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        try: driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True

    def error_check(self):
        if self.is_element_present(By.XPATH, '//*[contains(text(), "Close")]'):
            if self.is_element_present(By.XPATH,'/html/body/div[5]/div[2]/div/mat-dialog-container/error-dialog/h1'):
                ui_element=driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/mat-dialog-container/error-dialog/h1')
                error_element=ui_element.text
                print (error_element)
            driver.find_element_by_xpath('//*[contains(text(), "Close")]').click()
            print ("Duplicate user cannot be created")

    @classmethod
    def tearDownClass(inst):
        pass


def run_create_group_test(webdriver):
    global driver
    driver = webdriver
    suite = unittest.TestLoader().loadTestsFromTestCase(create_group_test)
    xmlrunner.XMLTestRunner(output=results_xml, verbosity=2).run(suite)

