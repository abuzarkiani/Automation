#coding=utf-8

from selenium import webdriver
from selenium.webdriver import ActionChains
from random import randint


useNativeEvents = 1

windowPath = "/AXApplication[@AXTitle='Calculator']/AXWindow[0]"
resultGroupPath = windowPath + "/AXGroup[0]"
basicGroupPath = windowPath + "/AXGroup[1]"


print("Starting the WebDriver session")
defaultLoopDelay_sec = 1.00
defaultCommandDelay_sec = 0.100
defaultImplicitTimeout_sec = 3.000
defaultMouseSpeed = 30
defaultScreenShotOnError = False
defaultGlobalDiagnosticsDirectory = '~/Desktop/'
defaultCookies = [
    {'name': 'loop_delay', 'value': defaultLoopDelay_sec},
    {'name': 'command_delay', 'value':defaultCommandDelay_sec },
    {'name': 'implicit_timeout', 'value': defaultImplicitTimeout_sec},
    {'name': 'mouse_speed', 'value': defaultMouseSpeed},
    {'name': 'screen_shot_on_error', 'value': defaultScreenShotOnError},
    {'name': 'global_diagnostics_directory', 'value': defaultGlobalDiagnosticsDirectory}
]
desiredCapabilities = {'platform': 'Mac', 'cookies': defaultCookies}
driver = webdriver.Remote( command_executor='http://localhost:4622/wd/hub', desired_capabilities=desiredCapabilities)


print("Opening the Calculator app")
driver.get("Calculator")

def numToAXPath(num):
    if num == 0:
        return basicGroupPath + "/AXButton[@AXDescription='zero']"
    elif num == 1:
        return basicGroupPath + "/AXButton[@AXDescription='one']"
    elif num == 2:
        return basicGroupPath + "/AXButton[@AXDescription='two']"
    elif num == 3:
        return basicGroupPath + "/AXButton[@AXDescription='three']"
    elif num == 4:
        return basicGroupPath + "/AXButton[@AXDescription='four']"
    elif num == 5:
        return basicGroupPath + "/AXButton[@AXDescription='five']"
    elif num == 6:
        return basicGroupPath + "/AXButton[@AXDescription='six']"
    elif num == 7:
        return basicGroupPath + "/AXButton[@AXDescription='seven']"
    elif num == 8:
        return basicGroupPath + "/AXButton[@AXDescription='eight']"
    elif num == 9:
        return basicGroupPath + "/AXButton[@AXDescription='nine']"
    else:
        return ""
    
button_clear = driver.find_element_by_xpath(basicGroupPath + "/AXButton[@AXDescription='clear']")
button_plus = driver.find_element_by_xpath(basicGroupPath + "/AXButton[@AXDescription='add']")
button_equals = driver.find_element_by_xpath(basicGroupPath + "/AXButton[@AXDescription='equals']")
text_result = driver.find_element_by_xpath(resultGroupPath + "/AXStaticText[@AXDescription='main display']")
button_minus = driver.find_element_by_xpath(basicGroupPath + "/AXButton[@AXDescription='subtract']")
button_multiply = driver.find_element_by_xpath(basicGroupPath + "/AXButton[@AXDescription='multiply']")
button_division = driver.find_element_by_xpath(basicGroupPath + "/AXButton[@AXDescription='divide']")


def clickElement(element):
    if useNativeEvents > 0:
        # move and click the mouse like a user
        actions = ActionChains(driver)
        actions.click(element)
        actions.perform()
    else:
        # use the traditional accessibility action
        element.click()


def check_all_numbers_are_working():
    print("Check if all the numbers are working (0 to 9)")
    
    num_array = range(10)
    for num in num_array:
        n = numToAXPath(int(num))
        clickElement(driver.find_element_by_xpath(n))

def check_clear_key_is_working():
    print("Check if the clear key is working")
    clickElement(button_clear)

def check_equal_key_is_working():
    print("Check if equal key is working")
    clickElement(button_equals)

def clear_screen():
    clickElement(button_clear)

def addition():
    print("Check the addition of two integer numbers")
    num1 = numToAXPath(5)
    clickElement(driver.find_element_by_xpath(num1))

    clickElement(button_plus)
    
    num2 = numToAXPath(9)
    clickElement(driver.find_element_by_xpath(num2))

    clickElement(button_equals)

    print("Reading result from screen")
    ActionChains(driver).move_to_element(text_result).perform()
    answer = text_result.text

    if int(answer) == 14:
        print("The addition of two integer numbers is Passed")
    else:
        print("The addition of two integer numbers is Failed")

def subtraction():
    print("Check the subtraction of two negative numbers")
    clear_screen()
    clickElement(button_minus)
    num1 = numToAXPath(5)
    clickElement(driver.find_element_by_xpath(num1))
    clickElement(button_minus)
    num2 = numToAXPath(9)
    clickElement(driver.find_element_by_xpath(num2))

    clickElement(button_equals)

    print("Reading result from screen")
    ActionChains(driver).move_to_element(text_result).perform()
    answer = text_result.text

    if int(answer) == -14:
        print("The subtraction of two negative numbers is Passed")
    else:
        print("The subtraction of two negative numbers is Failed")       


def multiplication():
    print("Check the multiplication of two integer numbers")
    num1 = numToAXPath(5)
    clickElement(driver.find_element_by_xpath(num1))

    clickElement(button_multiply)
    
    num2 = numToAXPath(9)
    clickElement(driver.find_element_by_xpath(num2))

    clickElement(button_equals)

    print("Reading result from screen")
    ActionChains(driver).move_to_element(text_result).perform()
    answer = text_result.text

    if int(answer) == 45:
        print("The multiplication of two integer numbers is Passed")
    else:
        print("The multiplication of two integer numbers is Failed")

def division():
    print("Check the division of two integer numbers")
    num1 = numToAXPath(9)
    clickElement(driver.find_element_by_xpath(num1))

    clickElement(button_division)
    
    num2 = numToAXPath(5)
    clickElement(driver.find_element_by_xpath(num2))

    clickElement(button_equals)

    print("Reading result from screen")
    ActionChains(driver).move_to_element(text_result).perform()
    answer = text_result.text

    if answer == str('1,8'):
        print("The division of two integer numbers is Passed")
    else:
        print("The division of two integer numbers is Failed")


def division_of_number_by_zero():
    print("Check the division of a number by zero")
    num1 = numToAXPath(9)
    clickElement(driver.find_element_by_xpath(num1))

    clickElement(button_division)
    
    num2 = numToAXPath(0)
    clickElement(driver.find_element_by_xpath(num2))

    clickElement(button_equals)

    print("Reading result from screen")
    ActionChains(driver).move_to_element(text_result).perform()
    answer = text_result.text

    if answer == 'Not a number':
        print("The division of a number by zero is Passed")
    else:
        print("The division of a number by zero is Failed")


def division_of_zero_by_any_number():
    print("Check the division of zero by any number")
    num1 = numToAXPath(0)
    clickElement(driver.find_element_by_xpath(num1))

    clickElement(button_division)
    
    num2 = numToAXPath(9)
    clickElement(driver.find_element_by_xpath(num2))

    clickElement(button_equals)

    print("Reading result from screen")
    ActionChains(driver).move_to_element(text_result).perform()
    answer = text_result.text

    if int(answer) == 0:
       print("The division of zero by any number is Passed")
    else:
        print("The division of zero by any number is Failed")       




print("Test the app’s basic operations")
useNativeEvents = 0
check_all_numbers_are_working()
check_clear_key_is_working()
check_equal_key_is_working()

print("Test the app’s functionality")
addition()
clear_screen()
subtraction()
clear_screen()
multiplication()
clear_screen()
division()
clear_screen()
division_of_number_by_zero()
clear_screen()
division_of_zero_by_any_number()




# quit the webdriver instance
print("Quitting the WebDriver session")
driver.quit()
#Add case specific print statement
