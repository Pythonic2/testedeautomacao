from selenium import webdriver


class ChromeAuto:
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome = webdriver.Chrome(options=options)

    chrome.maximize_window()