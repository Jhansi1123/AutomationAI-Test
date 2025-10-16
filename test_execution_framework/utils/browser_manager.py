from selenium import webdriver

def get_browser(browser_name='chrome'):
    if browser_name == 'chrome':
        return webdriver.Chrome()
    elif browser_name == 'firefox':
        return webdriver.Firefox()
    else:
        raise Exception("Unsupported browser")
