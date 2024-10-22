from selenium import webdriver
import unittest
import logging
from selenium.webdriver.common.by import By

class FlaskServerPingTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up logging
        logging.basicConfig(level=logging.INFO)
        cls.logger = logging.getLogger(cls.__name__)

        # Set up the WebDriver (you might need to specify the path to your WebDriver)
        cls.driver = webdriver.Chrome()
        cls.logger.info("WebDriver initialized.")

    @classmethod
    def tearDownClass(cls):
        # Close the WebDriver
        cls.driver.quit()
        cls.logger.info("WebDriver closed.")

    def test_ping(self):
        self.driver.get("http://127.0.0.1:5000")
        self.logger.info(f"Page title: {self.driver.title}")
        self.assertIn("User Information", self.driver.title)

    def test_form(self):
        self.driver.get("http://127.0.0.1:5000")
        self.driver.find_element(By.ID, "name").send_keys("Test User")
        self.driver.find_element(By.ID, "email").send_keys("testmail@test.nl")
        self.driver.find_element(By.ID, "receiver").send_keys("testmail@test.nl")
        self.driver.find_element(By.ID, "subject").send_keys("Test Subject")
        self.driver.find_element(By.ID, "body").send_keys("This is a test body.")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        self.logger.info("Form submitted successfully.")
    

if __name__ == "__main__":
    unittest.main()