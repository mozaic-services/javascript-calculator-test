import time, sys, warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
# Supress PhantomJS deprecation warnings
warnings.filterwarnings("ignore")
phantom_driver = "C:\\Program Files (x86)\\phantomjs\\bin\\phantomjs.exe"
driver = webdriver.PhantomJS(phantom_driver)
# Selenium script target URL
if len(sys.argv) > 1:
	target_site = sys.argv[1]
else:
	# Default target URL
	target_site = "https://calculator.demo.mozaicdemo.cloud"
print('\n\n Target ==> %s\n' % target_site)

# Convert symbols into equivalent HTML IDs
def convert(number):
	number = str(number)
	if number in {'0','1','2','3','4','5','6','7','8','9'}:
		result = "btn"+number
	elif number == '+':
		result = "btnPlus"
	elif number == '-':
		result = "btnMinus"
	elif number == '*':
		result = "btnTimes"
	elif number == '/':
		result = "btnDiv"
	elif number == '=':
		result = "btnEquals"
	else:
		print("[ERROR] Conversion failed!")
		sys.exit(1)
	return result

# Test everything
def test():
	error_count = 0
	n1_int = randint(1,9)
	n2_int = randint(1,9)
	correct_answer = n1_int + n2_int
	print('---- Running Test [1/4] ----')
	print('Expecting %r + %r = %r' % (n1_int,n2_int,correct_answer))
	driver.get(target_site)
	driver.find_element_by_id(convert(n1_int)).click()
	driver.find_element_by_id(convert('+')).click()
	driver.find_element_by_id(convert(n2_int)).click()
	driver.find_element_by_id(convert("=")).click()
	ans = driver.find_element_by_class_name("log").text
	try:
		assert ans == str(correct_answer)
		print('Results %r + %r = %s\nAddition functionality working!' % (n1_int,n2_int,ans))
	except AssertionError:
		print("Results %r + %r = %s\n\n\t[!] Assertion Failed [!]\n     Test [1/4] failed, addition functionality broken." % (n1_int,n2_int,ans))
		error_count+=1
	correct_answer = n1_int - n2_int
	print('\n---- Running Test [2/4] ----')
	print('Expecting %r - %r = %r' % (n1_int,n2_int,correct_answer))
	driver.get(target_site)
	driver.find_element_by_id(convert(n1_int)).click()
	driver.find_element_by_id(convert('-')).click()
	driver.find_element_by_id(convert(n2_int)).click()
	driver.find_element_by_id(convert("=")).click()
	ans = driver.find_element_by_class_name("log").text
	try:
		assert ans == str(correct_answer)
		print('Results %r - %r = %s\nSubtraction functionality working!' % (n1_int,n2_int,ans))
	except AssertionError:
		print("Results %r - %r = %s\n\n\t[!] Assertion Failed [!]\n     Test [2/4 failed, subtraction functionality broken." % (n1_int,n2_int,ans))
		error_count+=1
	correct_answer = n1_int * n2_int
	print('\n---- Running Test [3/4] ----')
	print('Expecting %r * %r = %r' % (n1_int,n2_int,correct_answer))
	driver.get(target_site)
	driver.find_element_by_id(convert(n1_int)).click()
	driver.find_element_by_id(convert('*')).click()
	driver.find_element_by_id(convert(n2_int)).click()
	driver.find_element_by_id(convert("=")).click()
	ans = driver.find_element_by_class_name("log").text
	try:
		assert ans == str(correct_answer)
		print('Results %r x %r = %s\nMultiplication functionality working!' % (n1_int,n2_int,ans))
	except AssertionError:
		print("Results %r x %r = %s\n\n\t[!] Assertion Failed [!]\n     Test [3/4] failed, multiplication functionality broken..." % (n1_int,n2_int,ans))
		error_count+=1
	correct_answer = str(n1_int / n2_int)[:1]
	print('\n---- Running Test [3/4] ----')
	print('Expecting %r / %r = %s' % (n1_int,n2_int,correct_answer))
	driver.get(target_site)
	driver.find_element_by_id(convert(n1_int)).click()
	driver.find_element_by_id(convert('/')).click()
	driver.find_element_by_id(convert(n2_int)).click()
	driver.find_element_by_id(convert("=")).click()
	ans = driver.find_element_by_class_name("log").text
	ans = ans[:1]
	try:
		assert ans == str(correct_answer)
		print('Results %r / %r = %s\nDivision functionality working!' % (n1_int,n2_int,ans))
	except AssertionError:
		print("Results %r / %r = %s\n\n\t\t[!] Assertion Failed [!]\n     Test [4/4] failed, division functionality broken..." % (n1_int,n2_int,ans))
		error_count+=1
	if error_count > 0:
		sys.exit(1)
	else:
		sys.exit(0)

test()
