from selenium import webdriver

def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("--disable-dev-shm-usage")  # Corrected argument name
    options.add_argument("--no-sandbox")  # Corrected argument name
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--disable-blink-features=AutomationControlled")  # Corrected argument name

    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com")
    return driver

def main():
    driver = get_driver()
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    text = element.text
    driver.quit()  # Make sure to quit the driver after you're done using it
    return text

if __name__ == "__main__":
    print(main())
