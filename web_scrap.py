from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https:/inventwithpython.com')

try:
    ele = browser.find_element('cover-thumb')
    print('Found <%> element with that class_name!' %(ele.tag_name))
except:
    print('not found')

