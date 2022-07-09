from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import pytest
import os
import time
@pytest.fixture

#UrlFoto

def driver():
    driver = webdriver.Chrome()
    driver.get('https://opensource-demo.orangehrmlive.com') #buka situs di chrome
    driver.maximize_window()
    yield driver

def test_login_Negatif(driver):
    driver.find_element(By.ID, 'txtUsername').send_keys('Admin123') #input username
    driver.find_element(By.ID, 'txtPassword').send_keys('admin123456') #input password
    driver.find_element(By.ID, 'btnLogin').click()
    time.sleep(3)
    assert 'Invalid credentials' in driver.find_element(By.ID, 'spanMessage').text
    time.sleep(3)

def test_login_positif(driver):
    driver.find_element(By.ID, 'txtUsername').send_keys('Admin') #input username
    driver.find_element(By.ID, 'txtPassword').send_keys('admin123') #input password
    driver.find_element(By.ID, 'btnLogin').click()
    assert 'Welcome' in driver.find_element(By.ID, 'welcome').text
    driver.close()

def test_job():
    driver.find_element(By.ID, 'menu_admin_viewAdminModule').click()
    driver.find_element(By.ID, 'menu_admin_job').click()
    driver.find_element(By.ID, 'menu_admin_viewJobTitle').click()
    time.sleep(3)

    driver.find_element(By.ID, 'btnAdd').click()
    driver.find_element(By.ID, 'jobTitle_jobTitle').send_keys('Ini title baru')
    driver.find_element(By.ID, 'jobTitle_jobDescription').send_keys('ini Job desc')
    driver.find_element(By.ID, 'jobTitle_note').send_keys('ini job Note')
    driver.find_element(By.ID, 'btnSave').click()