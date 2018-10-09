from selenium import webdriver
import time
import re
# user="cs1160341"
# passkey="password"
# course="COL351"
user=raw_input("Enter Your Username\n")  #Enter your username e.g. cs1160341
passkey=raw_input("Enter Your Password\n")  #Enter your password
course=raw_input("Enter Your Course Code\n")    #Enter your course

driver=webdriver.Chrome()
driver.get("https://moodle.iitd.ac.in/login/index.php")
def func():
	box=driver.find_element_by_tag_name('form')
	text=box.text
	s=text[50:80]
	s=s.encode('ascii','ignore')
	p=[int(asd) for asd in re.findall(r'\d+', s)]
	# print p
	# print s
	match=re.search(r'first',s)
	if (not match):
		driver.refresh()
		func()
		return
	username=driver.find_element_by_id('username')
	username.clear()
	username.send_keys(user)
	pwd=driver.find_element_by_id('password')
	pwd.clear()
	pwd.send_keys(passkey)
	val=driver.find_element_by_id('valuepkg3')
	val.clear()
	val.send_keys(p[0])
	sub=driver.find_element_by_id('loginbtn')
	sub.click()
	btna=driver.find_element_by_link_text('2')
	btna.click()
	btna=driver.find_element_by_partial_link_text(course)
	a=btna.get_property('href')
	driver.get(a)
func()
