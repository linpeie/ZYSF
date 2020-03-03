# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:LPE
# datetime:2020-02-24 11:25
# software: PyCharm
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# # 跟谷歌浏览器建立连接，启动chromedriver.exe  打开chrome
driver = webdriver.Chrome()
# 发送命令，访问HIS13登录页面
driver.get("http://10.16.0.78/his-common-test/#/home")
# 窗口最大化
driver.maximize_window()
# 点击账号输入框输入账号
driver.find_element_by_xpath('//input[@type="text"]').send_keys('9999')
# 点击密码输入框输入密码
driver.find_element_by_xpath('//input[@type="password"]').send_keys('')
# 点击登录
driver.find_element_by_xpath('//span[text()="登录"]').click()
# # 点击取消
# driver.find_element_by_xpath('//button[@class="ivu-btn ivu-btn-primary"]//span[text()="取消"]').click()
# 等待是否出现确认继续登录弹窗，若存在就点击
loc_login = (By.XPATH, '//span[text()="继续登录"]')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc_login))
driver.find_element(*loc_login).click()
# 选择住院收费处
# driver.find_element_by_xpath('//div[contains(text(),"住院收费处")]')
# driver.find_element_by_xpath('//div[contains(text(),"住院收费系统")]')
# loc_adress = (By.XPATH, '//div[@class="ivu-carousel-track"]//div[contains(text(),"住院收费系统")]')
# 查找住院收费处
loc_adress = (By.XPATH, '//div[contains(text(),"住院收费处")]')
# print(loc_adress)
# 等待住院收费处元素可见
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc_adress))
# 点击住院收费处进入下一页面
driver.find_element(*loc_adress).click()
# 查找HIS13住院收费处
loc_his = (By.XPATH, '//div[text()="HIS13住院收费系统"]/parent::div[@class="bs_box"]')
# print(loc_his)
# 等待HIS13住院收费元素可见
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc_his))
# time.sleep(3)
# 鼠标选择HIS13住院收费处
double_ele = driver.find_element(*loc_his)
# print(double_ele)
# 鼠标双击进入新版HIS13系统
ActionChains(driver).double_click(double_ele).perform()
# 退出登录
driver.find_element_by_xpath('//i[@class="iconfont icontc ivu-icon"]').click()
# 关闭窗口
driver.close()
# 关闭会话
driver.quit()


