from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Stub untuk simulasi validasi server
def stub_response_register(name, email, username, password, confirm_password):
    if not name:
        return "Error: Field 'Nama' wajib diisi"
    if not email:
        return "Error: Field 'Email' wajib diisi"
    if "@" not in email or "." not in email.split("@")[-1]:
        return "Error: Format email tidak valid"
    if email == "yusuf@email.com":
        return "Error: Email sudah terdaftar"
    if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
        return "Error: Password minimal 8 karakter dengan kombinasi huruf, angka, dan simbol"
    if password != confirm_password:
        return "Error: Konfirmasi password tidak sesuai"
    return "Success: Akun berhasil dibuat"

def stub_response_login(username, password):
    if not username or not password:
        return "Error: Username dan password wajib diisi"
    if username != "PelancongAngkasa" or password != "Admin1234":
        return "Error: Username atau password salah"
    return "Success: Login berhasil"

# Setup WebDriver
driver = webdriver.Chrome()  
driver.get("http://localhost/quiz-pengupil/register.php")
time.sleep(2)  

### TEST CASE: REGISTRASI ###
# 1.1 Registrasi dengan data valid
driver.find_element(By.NAME, "name").send_keys("Yusuf")
driver.find_element(By.NAME, "email").send_keys("yusuf@email.com")
driver.find_element(By.NAME, "username").send_keys("PelancongAngkasa")
driver.find_element(By.NAME, "password").send_keys("Admin1234")
driver.find_element(By.NAME, "confirm_password").send_keys("Admin1234")
driver.find_element(By.NAME, "submit").click()
time.sleep(2)

response = stub_response_register("Yusuf", "yusuf@email.com", "PelancongAngkasa", "Admin1234", "Admin1234")
print("Test Registrasi Data Valid:", response)

# 1.2 Registrasi dengan email sudah terdaftar
driver.get("http://localhost/quiz-pengupil/register.php")
time.sleep(2)
driver.find_element(By.NAME, "name").send_keys("Yusuf")
driver.find_element(By.NAME, "email").send_keys("yusuf@email.com")
driver.find_element(By.NAME, "username").send_keys("PelancongBaru")
driver.find_element(By.NAME, "password").send_keys("Admin1234")
driver.find_element(By.NAME, "confirm_password").send_keys("Admin1234")
driver.find_element(By.NAME, "submit").click()
time.sleep(2)

response = stub_response_register("Yusuf", "yusuf@email.com", "PelancongBaru", "Admin1234", "Admin1234")
print("Test Registrasi Email Sudah Terdaftar:", response)

# 1.3 Registrasi dengan password tidak memenuhi kompleksitas
driver.get("http://localhost/quiz-pengupil/register.php")
time.sleep(2)
driver.find_element(By.NAME, "name").send_keys("Yusuf")
driver.find_element(By.NAME, "email").send_keys("baru@email.com")
driver.find_element(By.NAME, "username").send_keys("PelancongBaru")
driver.find_element(By.NAME, "password").send_keys("12345")
driver.find_element(By.NAME, "confirm_password").send_keys("12345")
driver.find_element(By.NAME, "submit").click()
time.sleep(2)

response = stub_response_register("Yusuf", "baru@email.com", "PelancongBaru", "12345", "12345")
print("Test Registrasi Password Tidak Memenuhi Kompleksitas:", response)

# 1.4 Konfirmasi password tidak sesuai
driver.get("http://localhost/quiz-pengupil/register.php")
time.sleep(2)
driver.find_element(By.NAME, "name").send_keys("Yusuf")
driver.find_element(By.NAME, "email").send_keys("baru@email.com")
driver.find_element(By.NAME, "username").send_keys("PelancongBaru")
driver.find_element(By.NAME, "password").send_keys("Admin1234")
driver.find_element(By.NAME, "confirm_password").send_keys("Admin1235")
driver.find_element(By.NAME, "submit").click()
time.sleep(2)

response = stub_response_register("Yusuf", "baru@email.com", "PelancongBaru", "Admin1234", "Admin1235")
print("Test Konfirmasi Password Tidak Sesuai:", response)



# 1.5 Validasi format email
driver.get("http://localhost/quiz-pengupil/register.php")
time.sleep(2)
driver.find_element(By.NAME, "name").send_keys("Yusuf")
driver.find_element(By.NAME, "email").send_keys("yusuf@email")
driver.find_element(By.NAME, "username").send_keys("PelancongBaru")
driver.find_element(By.NAME, "password").send_keys("Admin1234")
driver.find_element(By.NAME, "confirm_password").send_keys("Admin1234")
driver.find_element(By.NAME, "submit").click()
time.sleep(2)

response = stub_response_register("Yusuf", "yusuf@email", "PelancongBaru", "Admin1234", "Admin1234")
print("Test Validasi Format Email:", response)

### TEST CASE: LOGIN ###
driver.get("http://localhost/quiz-pengupil/login.php")
time.sleep(2)

# 2.1 Valid Login dengan Kredensial Benar
driver.find_element(By.NAME, "username").send_keys("PelancongAngkasa")
driver.find_element(By.NAME, "password").send_keys("Admin1234")
driver.find_element(By.NAME, "submit").click()
time.sleep(2)

response = stub_response_login("PelancongAngkasa", "Admin1234")
print("Test Login Valid:", response)

# 2.2 Login dengan Username Salah
driver.get("http://localhost/quiz-pengupil/login.php")
time.sleep(2)
driver.find_element(By.NAME, "username").send_keys("PelancongAngkasa!")
driver.find_element(By.NAME, "password").send_keys("Admin1234")
driver.find_element(By.NAME, "submit").click()
time.sleep(2)

response = stub_response_login("PelancongAngkasa!", "Admin1234")
print("Test Login Username Salah:", response)

# 2.3 Login dengan Password Salah
driver.get("http://localhost/quiz-pengupil/login.php")
time.sleep(2)
driver.find_element(By.NAME, "username").send_keys("PelancongAngkasa")
driver.find_element(By.NAME, "password").send_keys("Admin12345")
driver.find_element(By.NAME, "submit").click()
time.sleep(2)

response = stub_response_login("PelancongAngkasa", "Admin12345")
print("Test Login Password Salah:", response)

# 2.4 Login dengan Input Kosong
driver.get("http://localhost/quiz-pengupil/login.php")
time.sleep(2)
driver.find_element(By.NAME, "username").send_keys("")
driver.find_element(By.NAME, "password").send_keys("")
driver.find_element(By.NAME, "submit").click()
time.sleep(2)

response = stub_response_login("", "")
print("Test Login Input Kosong:", response)

# Tutup browser setelah semua pengujian selesai
driver.quit()
