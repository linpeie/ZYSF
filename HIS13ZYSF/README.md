# 自动化测试数据驱动框架

**web自动化测试框架**

## 1. 环境说明

#### python版本：3.6.1

#### 依赖包安装

打开命令行输入: `pip install -r requirements.txt`

注意：requirements.txt使用相对路径和绝对路径都可以。(可直接拖动文件到命令窗口)


#### 使用chrome浏览器，需要下载chromedrive
	1. 查看chrome版本号：帮助->关于Google Chrome，在打开的设置页面中间可以看到Chrome的当前版本，例如：当前Chrome版本59，下载v2.32版本的chromedriver
	2. 下载chromedrive驱动：https://chromedriver.storage.googleapis.com/index.html
	3. 注意浏览器chrome与chromedriver的对应版本（我的chrome是59，因此选择2.32的chromedriver），建议关闭浏览器自动更新
	4. 把chromedriver.exe放在python路径下,也可随便放到你喜欢的目录,并设置环境变量

#### 目录对应说明


	|-- README.md：说明
	|-- requirements.txt：依赖包文件
	|-- appModules：存放业务脚本
	  |-- loginAction.py：登录脚本
	  ...
	|-- config：存放配置文件
	  |-- pageElementLocator.ini：存储定位页面元素的定位表达式
	  |-- varConfig.py：存放一些全局变量
	|-- logs：存放日志文件
	|-- pageObjects：存放页面对象封装文件
	  |-- basePage.py：页面共同的对象封装文件，例如封装菜单对象等
	  |-- loginPage.py：登录页面上的对象封装
	  ...
	|-- testData：存放测试数据文件
	  |-- testData：测试数据文件
	|-- testScripts：存放测试脚本
	  |-- testPersonInfo.py：用户信息管理的测试脚本
	  ...
	|-- util：存放工具类文件
	  |-- browser.py：封装了启动浏览器的方法
	  |-- HTMLTestRunner.py：生成测试报告的模块
	  |-- HTMLTestRunner_Chart.py：生成测试报告的模块(带图标，可以保存十次执行记录)
	  |-- log.py：封装了日志输出的方法
	  |-- mail.py：封装了发送邮件的方法
	  |-- objectMap.py：封装了定位页面元素的方法
	  |-- parseExcel.py：用于解析excel的方法
	  |-- parsePageElementLocator.py：用于解析页面元素定位表达式的文件(解析pageElementLocator.ini)
	  |-- screenshots.py：用于截图并保存在logs\screenshots目录下
	  |-- wrappers.py：元素高亮和截图的装饰器，用在objectMap.py
	|-- start.py：主程序

## 2. 使用

#### pageElementLocator.ini

把定位表达式放在 pageElementLocator.ini，不同页面存在不同的[section]中，表达式右侧用“>>”分开，例如：页面中有个用户名的输入框对象的id值是loginID，表达式可写成 username = id>>loginId 

    1. id
    2. name
    3. tag name
    4. class name
    5. xpath
    6. css selector
    7. link text
    8. partial link text

#### objectMap.py

获取单个页面元素对象：`getElement(driver, "id", "kw")`

获取多个页面元素对象：`getElements(driver, "tag name", "a")`

#### pageObjects 封装页面对象

参考 loginPage.py 

```python
from util.objectMap import getElement, getElements
from util.parsePageElementLocator import ParsePageElementLocator

class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.parsePEL = ParsePageElementLocator()
        self.Options = self.parsePEL.getItemsSection("login_page")

    def userNameObj(self):
        try:
            # 从定位表达式配置文件中读取定位用户名输入框的定位方式和表达式
            locateType, locatorExpression = self.Options["username".lower()].split(">>")
            # 获取登录页面的用户名输入框页面对象，并返回给调用者
            element = getElement(self.driver, locateType, locatorExpression)
            return element
        except Exception as e:
            raise e
```

#### appModules 业务脚本

参考 loginAction.py

```python
import time
from config.varConfig import url
from pageObjects.loginPage import LoginPage

class LoginAction(object):
    def __init__(self):
        print('login...')

    @staticmethod
    def login(driver, username, password):
        try:
            driver.get(url)
            login = LoginPage(driver)
            if username:
                login.userNameObj().send_keys(username)
            if password:
                login.passwordObj().send_keys(password)
            code = login.getCodeValue()
            login.codeObj().send_keys(code)
            login.loginBtn().click()
            time.sleep(0.5)
        except Exception as e:
            raise e
```

#### testScript 测试脚本

参考 testPersonInfo.py 

函数命名都以test开头，后面执行start.py时测试套件会自动执行所有以test开头的测试脚本，测试数据表中每列数据对应的字段都定义在varConfig.py中

#### start.py 主程序

执行结束需要自动发一封邮件的记得配置收发邮箱的账号；

不需要发送邮件的把email.send()注释掉。

## 3. 运行

方式一：直接运行
`python start.py`

方式一：使用IDE运行（Pycharm/Sublime…）
`打开项目，执行start.py`

