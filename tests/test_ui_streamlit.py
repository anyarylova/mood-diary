import time
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_streamlit_register_login_log_mood():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("http://localhost:8501")
        time.sleep(5)  # Let Streamlit load

        username = f"testuser_{uuid.uuid4().hex[:8]}"
        password = "testpass"  # nosec B105

        # Fill username and password
        inputs = driver.find_elements(By.TAG_NAME, "input")
        username_input = inputs[0]
        password_input = inputs[1]
        username_input.send_keys(username)
        password_input.send_keys(password)

        # Click Register
        register_button = next(btn for btn in driver.find_elements(
            By.TAG_NAME, "button") if "Register" in btn.text)
        register_button.click()
        time.sleep(2)

        # Click Login
        login_button = next(btn for btn in driver.find_elements(
            By.TAG_NAME, "button") if "Login" in btn.text)
        login_button.click()

        # Wait for sidebar greeting
        wait.until(EC.presence_of_element_located(
            (By.XPATH, f"//p[contains(text(), '{username}')]")
            ))

        # Mood form: leave dropdown as-is and fill note
        text_area = wait.until(EC.presence_of_element_located(
            (By.TAG_NAME, "textarea")
            ))
        text_area.send_keys("testing with the sad mood.")

        # Submit
        submit_button = next(btn for btn in driver.find_elements(
            By.TAG_NAME, "button") if "Submit Mood" in btn.text
            )
        submit_button.click()

        # Confirm submission
        wait.until(EC.presence_of_element_located((
            By.XPATH, "//*[contains(text(), 'Mood logged successfully!')]"
            ))
            )

    except Exception as e:
        driver.save_screenshot("debug.png")
        raise e
    finally:
        driver.quit()
