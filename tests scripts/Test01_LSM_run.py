import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestTest01LMS():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_test01LMS(self):
        self.setup_method(None)  # Manually invoke setup_method
        self.driver.get("http://localhost:3000/")
        self.driver.set_window_size(1536, 816)
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".bg-gray-900:nth-child(1) > .bg-gray-800:nth-child(1) > .font-semibold").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".bg-gray-700:nth-child(1)").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".bg-gray-700:nth-child(2)").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".bg-gray-700:nth-child(3)").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".lg\\3A block").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".bg-gray-900:nth-child(2) > .bg-gray-800:nth-child(1) > .font-semibold").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".bg-gray-700").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".lg\\3A block").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".bg-gray-900:nth-child(1) > .bg-gray-800:nth-child(2) > p:nth-child(2)").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".bg-gray-700:nth-child(1)").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".bg-gray-700:nth-child(2)").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".bg-gray-700:nth-child(3)").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".lg\\3A block").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".bg-blue-800").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".relative:nth-child(2) .block:nth-child(1)").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".border").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".border").send_keys("Harry Potter")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".bg-blue-700:nth-child(2)").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".bg-gray-700").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "price").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "price").send_keys("600")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".bg-blue-700:nth-child(2)").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".lg\\3A block").click()
        time.sleep(1)
        self.driver.close()

if __name__ == "__main__":
    test = TestTest01LMS()
    test.test_test01LMS()
