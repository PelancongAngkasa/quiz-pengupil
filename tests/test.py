import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class AuthTest(unittest.TestCase):
    
    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        server = 'http://localhost:4444'

        self.browser = webdriver.Remote(command_executor=server, options=options)
        self.addCleanup(self.browser.quit)

    def register_user(self, name, email, username, password, confirm_password):
        self.browser.get("http://localhost/quiz-pengupil/register.php")
        time.sleep(5)
        self.browser.find_element(By.NAME, "Nama").send_keys(name)
        self.browser.find_element(By.NAME, "Alamat Email").send_keys(email)
        self.browser.find_element(By.NAME, "Username").send_keys(username)
        self.browser.find_element(By.NAME, "Password").send_keys(password)
        self.browser.find_element(By.NAME, "Re-Password").send_keys(confirm_password)
        self.browser.find_element(By.NAME, "Register").click()
        time.sleep(5)
    
    def test_register_valid(self):
        self.register_user("Yusuf", "yusuf@email.com", "PelancongAngkasa", "Admin1234", "Admin1234")
        

    def test_register_email_taken(self):
        self.register_user("Yusuf", "yusuf@email.com", "PelancongBaru", "Admin1234", "Admin1234")
        self.assertIn("Email sudah terdaftar", self.browser.page_source)
    
    def test_register_invalid_password(self):
        self.register_user("Yusuf", "baru@email.com", "PelancongBaru", "12345", "12345")
        self.assertIn("Password minimal 8 karakter", self.browser.page_source)
    
    def test_register_password_mismatch(self):
        self.register_user("Yusuf", "baru@email.com", "PelancongBaru", "Admin1234", "Admin1235")
        self.assertIn("Password tidak sama !!", self.browser.page_source)
    
    def test_register_invalid_email(self):
        self.register_user("Yusuf", "yusuf@email", "PelancongBaru", "Admin1234", "Admin1234")
        self.assertIn("Format email tidak valid", self.browser.page_source)
    
    def login_user(self, username, password):
        self.browser.get("http://localhost/quiz-pengupil/login.php")
        time.sleep(5)
        self.browser.find_element(By.NAME, "username").send_keys(username)
        self.browser.find_element(By.NAME, "password").send_keys(password)
        self.browser.find_element(By.NAME, "submit").click()
        time.sleep(5)
    
    def test_login_valid(self):
        self.login_user("PelancongAngkasa", "Admin1234")
        
    
    def test_login_wrong_username(self):
        self.login_user("PelancongAngkasa!", "Admin1234")
        self.assertIn("Register User Gagal !!", self.browser.page_source)
    
    def test_login_wrong_password(self):
        self.login_user("PelancongAngkasa", "Admin12345")
        self.assertIn("Register User Gagal !!", self.browser.page_source)
    
    def test_login_empty_fields(self):
        self.login_user("", "")
        self.assertIn("Data tidak boleh kosong !!", self.browser.page_source)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, warnings='ignore')
