# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

options = AppiumOptions()
options.load_capabilities({
	"appium:deviceName": "Android Emulator",
	"platformName": "Android",
	"appium:automationName": "UiAutomator2",
	"appium:appPackage": "com.swaglabsmobileapp",
	"appium:appWaitActivity": "com.swaglabsmobileapp.MainActivity",
	"appium:app": "C:\\Users\\GIGACHAD\\PycharmProjects\\appium\\app\\saucelabs.apk",
	"appium:settings[ignoreUnimportantViews]": True,
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)


driver.quit()