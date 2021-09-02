#import web driver  from selenium package
from selenium import webdriver

#call the function chrome form webdriver
driver = webdriver.Chrome()

#this get funciton will will take the URL and open the passed website 
driver.get("https://web.whatspp.com/")  #after this part if you run the code the whatsapp web is open

#ask the user to scan the QR code untill the script is paused
input("Scam QR code and press any key to start")

#after this we catch the element spac section to whom we want to send the message using different method
var=driver.find_element_by_css_selector('span["title=Rohit Patel"]')    #diff method like id, title, method, class_name, etc
                                                                        #select the span by title name 

#this clcik method the script utill the and key not press then it open the chatbox off th person
var.click() 

testinput = driver.find_element_by_xpath("/html/body/div[1]/div/div[4]")  #here copy the xpath which is uninque path if the there si the 
                                                                          #commmon claasses prent then we use thiss xpath

#loop for sending the message by 10 times
for i in range(10)
testinput.send_keys("Selenium Testing")
testinput.send_Keys(keys.RETURN)
