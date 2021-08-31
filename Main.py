from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://web.whatspp.com/")

input("Scam QR code and press any key to start")

var=driver.find_element_by_css_selector('span["title=Rohit Patel"]')
var.click()

testinput = driver.find_element_by_xpath("/html/body/div[1]/div/div[4]")

for i in range(10)
testinput.send_keys("Selenium Testing")
testinput.send_Keys(keys.RETURN)
