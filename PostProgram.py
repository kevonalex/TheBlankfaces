import pyautogui as pygui
import time
import webbrowser

#### TIKTOK
url = 'tiktok.com'
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab(url)

time.sleep(5)

pygui.click(1538,125)  # clicks login button
time.sleep(2)
pygui.click(930,439)  # clicks use email address
