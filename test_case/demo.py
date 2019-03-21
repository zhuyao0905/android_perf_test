import os

content = os.popen("adb shell ps| findstr com.excelliance.dualaid " ).read()
print(content)
UID = content.split()[0].replace('_', '')
print(UID)
