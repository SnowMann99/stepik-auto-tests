from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
url = 'http://suninjuly.github.io/redirect_accept.html'
browser.get(url)
opt1 = browser.find_element_by_class_name('btn')
opt1.click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
x = browser.find_element_by_id('input_value')
result = calc(int(x.text))
option1 = browser.find_element_by_id('answer')
option1.send_keys(result)
option2 = browser.find_element_by_class_name('btn')
option2.click()
time.sleep(10)
# first_window = browser.window_handles[0]
browser.quit()
