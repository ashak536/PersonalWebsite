from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def run_system_test():
    driver = webdriver.Chrome()
    
    try:
        driver.get("http://127.0.0.1:5000/projects")
        driver.maximize_window()
        time.sleep(1) 
        add_btn = driver.find_element(By.LINK_TEXT, "+ Add Project")
        add_btn.click()
        time.sleep(1)
        
        driver.find_element(By.NAME, "name").send_keys("Selenium Dynamic Project")
        driver.find_element(By.NAME, "description").send_keys("Automated black-box verification example.")
        driver.find_element(By.NAME, "url").send_keys("https://github.com/ashak536/selenium-test")
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)

        page_source = driver.page_source
        if "Selenium Dynamic Project" in page_source:
            print("System Test Passed: Project successfully added via UI simulation!")
        else:
            print("System Test Failed: Card element not found in DOM.")
            
    except Exception as e:
        print(f"An error occurred during system simulation: {e}")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    run_system_test()