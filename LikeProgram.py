# This program allows the user to log into TikTok and like all content relating to hashtags specified by the user. The user can input multiple hashtags at once and can 
# also control the number of posts liked by the program.
#
#
# TODO: Convert file from .py to .exe for exporting and sending to client to use without dependence on Pycharm IDE.
#       Add GUI for improved control/ functionality.

import pyautogui as pygui
import time
import webbrowser

#### TIKTOK
url = 'tiktok.com'
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
VideoCount = 5 # SET NO. OF VIDEOS THE PROGRAM SHOULD LIKE
hashtags = "theblankfaces" # SET WHICH HASHTAGS TO FILTER BY (to set multiple hashtags just insert a space between them e.g. "#tbf #manchester"

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab(url)
time.sleep(5)

pygui.click(1538,125)  # clicks login button
time.sleep(0.5)
pygui.click(930,439)  # clicks use email address

time.sleep(45)  # allows time for user to login

 # SEARCH FOR THE BLANKFACES
pygui.click(977, 129)  # moves to and clicks search bar
pygui.write(hashtags)

    # SCROLL AND LIKE

pygui.click(1202,660)  # moves to and clicks first video

for i in range(1, VideoCount):
    time.sleep(1)
    print(i)
    pygui.press('down')
    pygui.doubleClick(1035, 639)  # double clicks to like the video
####
