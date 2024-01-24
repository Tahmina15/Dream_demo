import os
import time
import traceback

import pytest
from selenium import webdriver
from Utilities import Excel_Utils


# Command-line option to specify the browser (e.g., --browser_name chrome)
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="edge"
    )


# Fixture to set up the WebDriver and other properties
@pytest.fixture(scope="class")
def set_up(request):
    # browser_name = "chrome"
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=options)
    else:
        print("Unsupported browser - :" + browser_name)
    request.cls.driver = driver
    driver.get("https://www.dreams.co.uk/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    # This is the setup code, the test runs here
    yield driver

    # Teardown: Capture screenshot on failure and close the WebDriver
    if request.node.session.testsfailed > 0:
        take_screenshot(request.cls.driver, request.node.name)

    request.cls.driver.quit()


def take_screenshot(driver, screenshot_name):
    try:
        screenshot_directory = "screenshots"
        if not os.path.exists(screenshot_directory):
            os.makedirs(screenshot_directory)

        # Include browser and window size information in the screenshot filename
        browser_name = driver.capabilities['browserName']
        window_size = driver.get_window_size()
        screenshot_name_with_info = f"{screenshot_name}_{browser_name}_{window_size['width']}x{window_size['height']}"

        screenshot_path = os.path.join(screenshot_directory, screenshot_name_with_info + ".png")
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")
    except Exception as e:
        error_message = f"An error occurred while taking screenshot: {str(e)}"
        print(error_message)
        traceback.print_exc()
