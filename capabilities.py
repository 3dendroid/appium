# adb shell "dumpsys window windows | grep -E 'mCurrentFocus'" .
# Use this command after u open ur application in emulator and know their appPackage and appActivity


capabilities = {
    "deviceName": "",
    "platformName": "",
    "appPackage": "",
    "appActivity": "",
    "app": ""
}

capabilities = {
    "deviceName": "Android Emulator",
    "platformName": "Android",
    "appPackage": "com.sand.airmirror",
    "appWaitActivity": "com.sand.airmirror.ui.guide.GuideActivity_",
    "app": "C:\\Users\\GIGACHAD\\PycharmProjects\\appium\\app\\AirMirror.apk"
}
