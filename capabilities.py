# adb shell "dumpsys window windows | grep -E 'mCurrentFocus'" .
# adb shell "dumpsys window windows"
# Use this command after u open ur application in emulator and know their appPackage and appActivity


capabilities = {
    "deviceName": "",
    "platformName": "",
    "appPackage": "",
    "appActivity": "",
    "app": ""
}

airmirror_capabilities = {
    "deviceName": "Android Emulator",
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "appPackage": "com.sand.airmirror",
    "appium:settings[IgnoreUnimportantViews]": "true",
    "appWaitActivity": "com.sand.airmirror.ui.guide.GuideActivity_",
    "app": "C:\\Users\\GIGACHAD\\PycharmProjects\\appium\\app\\AirMirror.apk"
}

sn_capabilities = {
    "deviceName": "Android Emulator",
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "appium:settings[IgnoreUnimportantViews]": "true",
    "appPackage": "com.mytona.seekersnotes.android",

    "appWaitActivity": "com.mytona.seekersnotes.android.MainActivity",
    "app": "C:\\Users\\GIGACHAD\\PycharmProjects\\appium\\app\\sn.apk"
}

saucelab_capabilities = {
    "appium:deviceName": "Android Emulator",
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "appium:settings[IgnoreUnimportantViews]": "true",
    "appium:appPackage": "com.swaglabsmobileapp",
    "appium:appWaitActivity": "com.swaglabsmobileapp.MainActivity",
    "appium:app": "C:\\Users\\GIGACHAD\\PycharmProjects\\appium\\app\\saucelabs.apk"
}
