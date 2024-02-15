from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

class Test026(unittest.TestCase):

    def testcase02(self):
        self.driver = None
        self.driver = webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")
        self.driver.get("http://127.0.0.1/026/testcase.html")
        
        first = self.driver.find_element(By.ID, "firstName")
        lastname = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")
        submit = self.driver.find_element(By.ID, "submit")
        
        first.send_keys("Johnj")
        lastname.send_keys("canoncanoncano")
        age.send_keys("149")
        submit.click()
        
        result = self.driver.find_element(By.ID, "firstname").text
        self.assertEqual("First Name:Johnj", result)
        
        # บันทึกรูปภาพหน้าจอและบันทึกลงในไฟล์ชื่อ testjhone11.png

    # ทดสอบอื่น ๆ สามารถเพิ่มต่อจากนี้ได้

if __name__ == "__main__":
    unittest.main()


