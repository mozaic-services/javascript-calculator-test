#TODO: optimise
import time, sys, warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint

# Supress PhantomJS deprecation warnings
warnings.filterwarnings("ignore")
# Hardcoded value for when Selenium can't find webdriver in PATH
phantom_driver = "C:\\Program Files (x86)\\phantomjs\\bin\\phantomjs.exe"
driver = webdriver.PhantomJS(phantom_driver)
# Selenium script target URL
if len(sys.argv) > 1:
	target_site = sys.argv[1]
else:
	# Default to hardcoded path when user hasn't specified a target URL
	target_site = "https://s3.eu-west-2.amazonaws.com/lohanlon-bucket/index.html"
print('\n Target ==> %s\n' % target_site)

def exit():
	sys.exit(0)

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
		print("No conversion occured!") 
	return result

'''
Tests addition functionality by generating two random integers
between 0-9, calculating the sum internally and comparing it to
the resulting output from the JS calculator.
'''
def additionTest():
    # RNG & Internal calculations for comparison
	n1_int = randint(1,9)
	n2_int = randint(1,9)
	n1 = convert(n1_int)
	n2 = convert(n2_int)
	correct_answer = n1_int + n2_int
	print('\nExpecting %r + %r = %r' % (n1_int,n2_int,correct_answer))
	# Test calculator against internal results
	driver.get(target_site)
	driver.maximize_window()
	time.sleep(3)
	driver.find_element_by_id(n1).click()
	driver.find_element_by_id(convert('+')).click()
	driver.find_element_by_id(n2).click()
	driver.find_element_by_id(convert("=")).click()
	ans = driver.find_element_by_class_name("log").text
	try:
		assert ans == str(correct_answer)
		print('Results %r + %r = %s\n\nAddition functionality working!' % (n1_int,n2_int,ans))
		main_menu()
	except AssertionError:
		print("Results %r + %r = %s\n\n\t[!] Assertion Failed [!]\n     Addition functionality broken..." % (n1_int,n2_int,ans))
		sys.exit(1)	
	
def subtractionTest():
    # RNG & Internal calculations for comparison
	n1_int = randint(1,9)
	n2_int = randint(1,9)
	n1 = convert(n1_int)
	n2 = convert(n2_int)
	correct_answer = n1_int - n2_int
	print('\nExpecting %r - %r = %r' % (n1_int,n2_int,correct_answer))
	# Test calculator against internal results
	driver.get(target_site)
	driver.maximize_window()
	time.sleep(3)
	driver.find_element_by_id(n1).click()
	driver.find_element_by_id(convert('-')).click()
	driver.find_element_by_id(n2).click()
	driver.find_element_by_id(convert("=")).click()
	ans = driver.find_element_by_class_name("log").text
	try:
		assert ans == str(correct_answer)
		print('Results %r - %r = %s\n\nSubtraction functionality working!' % (n1_int,n2_int,ans))
		main_menu()
	except AssertionError:
		print("Results %r - %r = %s\n\n\t[!] Assertion Failed [!]\n     Subtraction functionality broken..." % (n1_int,n2_int,ans))
		sys.exit(1)	
		
def multiplicationTest():
    # RNG & Internal calculations for comparison
	n1_int = randint(1,9)
	n2_int = randint(1,9)
	n1 = convert(n1_int)
	n2 = convert(n2_int)
	correct_answer = n1_int * n2_int
	print('\nExpecting %r x %r = %r' % (n1_int,n2_int,correct_answer))
	# Test calculator against internal results
	driver.get(target_site)
	driver.maximize_window()
	time.sleep(3)
	driver.find_element_by_id(n1).click()
	driver.find_element_by_id(convert('*')).click()
	driver.find_element_by_id(n2).click()
	driver.find_element_by_id(convert("=")).click()
	ans = driver.find_element_by_class_name("log").text
	try:
		assert ans == str(correct_answer)
		print('Results %r x %r = %s\n\nMultiplication functionality working!' % (n1_int,n2_int,ans))
		main_menu()
	except AssertionError:
		print("Results %r x %r = %s\n\n\t[!] Assertion Failed [!]\n     Multiplication functionality broken..." % (n1_int,n2_int,ans))
		sys.exit(1)
	
def divisionTest():
    # RNG & Internal calculations for comparison
	n1_int = randint(1,9)
	n2_int = randint(1,9)
	n1 = convert(n1_int)
	n2 = convert(n2_int)
	correct_answer = n1_int / n2_int
	correct_answer = str(correct_answer)[:4] # Limit to 2 d.p.
	print('\nExpecting %r / %r = %s' % (n1_int,n2_int,correct_answer))
	# Test calculator against internal results
	driver.get(target_site)
	driver.maximize_window()
	time.sleep(3)
	driver.find_element_by_id(n1).click()
	driver.find_element_by_id(convert('/')).click()
	driver.find_element_by_id(n2).click()
	driver.find_element_by_id(convert("=")).click()
	ans = driver.find_element_by_class_name("log").text
	try:
		assert ans == str(correct_answer)
		print('Results %r / %r = %s\n\nDivision functionality working!' % (n1_int,n2_int,ans))
		main_menu()
	except AssertionError:
		print("Results %r / %r = %s\n\n\t[!] Assertion Failed [!]\n     Division functionality broken..." % (n1_int,n2_int,ans))
		sys.exit(1)
	
# Test addition functionality
def main_menu():
	print('''
\t ======== MAIN MENU ========
\t| 0) Test Addition          |
\t| 1) Test Subtraction       |
\t| 2) Test Multiplication    |
\t| 3) Test Division          |
\t|  ______________________   |
\t| 4) Exit                   |
\t ---------------------------
''')
	choice = int(input('\t  Enter your choice: '))
	options = {
		0: additionTest,
		1: subtractionTest,
		2: multiplicationTest,
		3: divisionTest,
		4: exit
	}
	options[choice]()

#Entry point
main_menu()