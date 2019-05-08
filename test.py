import time, sys, warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
# Supress PhantomJS deprecation warnings
warnings.filterwarnings("ignore")

# Convert integers to the equivalent element ID
def convert(number):
    number = str(number)
    if number in {'0','1','2','3','4','5','6','7','8','9'}:
        result = "btn"+number
        return result
    else:
        print("No conversion occured!") 

'''
Tests addition functionality by generating two random integers
between 0-9, calculating the sum internally and comparing it to
the resulting output from the JS calculator.
'''
def additionTest():
    # Hardcoded value for when Selenium can't find webdriver in your PATH
    phantom_driver = "C:\\Program Files (x86)\\phantomjs\\bin\\phantomjs.exe"
    driver = webdriver.PhantomJS(phantom_driver)
    if len(sys.argv) > 1:
        target_site = sys.argv[1]
    else:
        # Default to hardcoded path when user hasn't specified a target URL
        target_site = "file:///C:/Users/2013l/git-src/javascript-calculator/index.html"
        
    print('Target: ' + target_site)
    # Internal calculations for comparison
    n1_int = randint(1,9)
    n2_int = randint(1,9)
    n1 = convert(n1_int)
    n2 = convert(n2_int)
    correct_answer = n1_int + n2_int
    print('Expecting %r + %r = %r' % (n1_int,n2_int,correct_answer))
    # Test calculator against internal results
    driver.get(target_site)
    driver.maximize_window()
    time.sleep(3)
    driver.find_element_by_id(n1).click()
    driver.find_element_by_id("btnPlus").click()
    driver.find_element_by_id(n2).click()
    driver.find_element_by_id("btnEquals").click()
    ans = driver.find_element_by_class_name("log").text
    try:
        assert ans == str(correct_answer)
        print('Output: %s\nAddition functionality working!' % ans)
        sys.exit(0)
    except AssertionError:
        print("Value expected: %s\nOutput value: %s\nAssertion Failed, addition functionality broken..." % (str(correct_answer), ans))
        sys.exit(1)

# Test addition functionality
additionTest()
