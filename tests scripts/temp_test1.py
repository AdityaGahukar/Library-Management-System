import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestLsmTest01():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
  
    def test_lsmTest01(self):
        self.driver.get("http://localhost:3000/")
        self.driver.set_window_size(1536, 816)
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".bg-blue-800").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".relative:nth-child(2) .block:nth-child(1)").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".border").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".border").send_keys("Harry Potter")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".border").send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".bg-blue-700:nth-child(2)").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".bg-gray-700:nth-child(1)").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "category").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "category").send_keys("Fiction")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".p-14").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".bg-blue-700:nth-child(2)").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".bg-red-100").click()
        time.sleep(1)
        self.driver.close()

if __name__ == "__main__":
    test = TestLsmTest01()
    test.test_lsmTest01()
