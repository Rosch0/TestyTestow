from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

@given('I go to web')
def I_go_to_web(context):
    context.driver.get("https://www.saucedemo.com/")


#@when('accept cookies')
#def step_accept_cookies(context):
    # Implementacja akceptacji plików cookie na stronie
    #accept_button = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')))
    #accept_button.click()
    # Asercja sprawdzająca, czy przycisk został kliknięty i pliki cookie są zaakceptowane
    #assert 'cookies_accepted' in context.driver.page_source, "Failed to accept cookies"

@when('enter username')
def step_enter_username(context):
    # Implementacja wprowadzania nazwy użytkownika
    username_input = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.ID, 'user-name')))
    username_input.send_keys("standard_user")
    # Asercja sprawdzająca, czy pole nazwy użytkownika zostało wypełnione poprawnie
    assert username_input.get_attribute("value") == "standard_user", "Failed to enter username"

@when('enter password')
def step_enter_password(context):
    # Implementacja wprowadzania hasła
    password_input = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
    password_input.send_keys("secret_sauce")
    # Asercja sprawdzająca, czy pole hasła zostało wypełnione poprawnie
    assert password_input.get_attribute("value") == "secret_sauce", "Failed to enter password"

@then('click button to login')
def step_click_login_button(context):
    # Implementacja kliknięcia przycisku logowania
    login_button = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]')))
    login_button.click()
    # Asercja sprawdzająca, czy przycisk logowania został kliknięty i nastąpiło zalogowanie
    assert 'dashboard' in context.driver.current_url, "Failed to click login button and log in successfully"
