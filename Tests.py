from selenium import webdriver
from selenium.webdriver.common.by import By
from Locators import *
import time

site = 'https://stellarburgers.nomoreparties.site/' # сайт для тестирования

# словарь с тестовыми данными
entities = {'name': 'Андрей',
            'email': 'andreyshevchenko777@yandex.ru',
            'valid_password': 'shevchenko',
            'invalid_password': 12345
            }
class TestForRegistration: # Тесты для регистрации
    def test_registration_with_valid_value(self): # Первая регистрация с правильно заполненными полями

        driver = webdriver.Chrome()

        driver.get(site)
        driver.find_element(By.XPATH, HomePage.LoginButton).click()
        driver.find_element(By.CSS_SELECTOR, AuthorizationPage.registration).click()

        name_field = driver.find_element(By.CSS_SELECTOR, RegistrationPage.name_field)
        name_field.send_keys(entities['name'])

        email_field = driver.find_element(By.CSS_SELECTOR, RegistrationPage.email_field)
        email_field.send_keys(entities['email'])

        pass_field = driver.find_element(By.CSS_SELECTOR, RegistrationPage.password_field)
        pass_field.send_keys(entities['valid_password'])

        driver.find_element(By.XPATH, RegistrationPage.reg_button).click()
        driver.implicitly_wait(3)

        reg_new_button_text = driver.find_element(By.CSS_SELECTOR, AuthorizationPage.registration).text
        assert reg_new_button_text == 'Зарегистрироваться'

        driver.quit()

    def test_registration_with_non_unique_email_fail(self): # Нельзя зарегистрироваться с повторным E-mailом

        driver = webdriver.Chrome()

        driver.get(site)
        driver.find_element(By.XPATH, HomePage.LoginButton).click()
        driver.find_element(By.CSS_SELECTOR, AuthorizationPage.registration).click()

        name_field = driver.find_element(By.CSS_SELECTOR, RegistrationPage.name_field)
        name_field.send_keys(entities['name'])

        email_field = driver.find_element(By.CSS_SELECTOR, RegistrationPage.email_field)
        email_field.send_keys(entities['email'])

        pass_field = driver.find_element(By.CSS_SELECTOR, RegistrationPage.password_field)
        pass_field.send_keys(entities['valid_password'])

        driver.find_element(By.XPATH, RegistrationPage.reg_button).click()
        driver.implicitly_wait(3)

        text = driver.find_element(By.CSS_SELECTOR, RegistrationPage.reg_error).text
        assert text == 'Такой пользователь уже существует'

        driver.quit()

    def test_registration_if_invalid_password_apeard_error(self): # Регистрация с неверным паролем
        driver = webdriver.Chrome()

        driver.get(site)
        driver.find_element(By.XPATH, HomePage.LoginButton).click()
        driver.find_element(By.CSS_SELECTOR, AuthorizationPage.registration).click()

        pass_field = driver.find_element(By.CSS_SELECTOR, RegistrationPage.password_field)
        pass_field.send_keys(entities['invalid_password'])

        name_field = driver.find_element(By.CSS_SELECTOR, RegistrationPage.name_field)
        name_field.send_keys(entities['name'])

        driver.find_element(By.CSS_SELECTOR, RegistrationPage.email_field).click()

        driver.implicitly_wait(3)
        text = driver.find_element(By.CSS_SELECTOR, RegistrationPage.reg_error).text
        assert text == 'Некорректный пароль'

        driver.quit()

class TestForLoginLogOut: # Тесты на Вход и Выход
    def test_login_on_home_page_success (self): # Авторизация с домашней страницы выполняется
        driver = webdriver.Chrome()

        driver.get(site)
        driver.find_element(By.XPATH, HomePage.LoginButton).click()

        name_field = driver.find_element(By.CSS_SELECTOR, AuthorizationPage.email_field)
        name_field.send_keys(entities['email'])

        pass_field = driver.find_element(By.CSS_SELECTOR, AuthorizationPage.password_field)
        pass_field.send_keys(entities['valid_password'])

        driver.find_element(By.CSS_SELECTOR, AuthorizationPage.LoginButton).click()
        driver.find_element(By.CSS_SELECTOR, AuthorizationPage.personalcabinet).click()

        driver.implicitly_wait(3)
        actual_name = driver.find_element(By.CSS_SELECTOR, PersonalCabinet.name_field)
        actual_email = driver.find_element(By.CSS_SELECTOR, PersonalCabinet.login_field)

        assert actual_name
        assert actual_email

        driver.quit()

    def test_login_from_personal_cabinet_success(self): # Авторизация через Личный кабинет выполняется
        driver = webdriver.Chrome()

        driver.get(site)
        driver.find_element(By.CSS_SELECTOR, HomePage.personalcabinet).click()

        name_field = driver.find_element(By.CSS_SELECTOR, AuthorizationPage.email_field)
        name_field.send_keys(entities['email'])

        pass_field = driver.find_element(By.CSS_SELECTOR, AuthorizationPage.password_field)
        pass_field.send_keys(entities['valid_password'])

        driver.find_element(By.CSS_SELECTOR, AuthorizationPage.LoginButton).click()
        driver.find_element(By.CSS_SELECTOR, AuthorizationPage.personalcabinet).click()

        driver.implicitly_wait(3)
        actual_name = driver.find_element(By.CSS_SELECTOR, PersonalCabinet.name_field)
        actual_email = driver.find_element(By.CSS_SELECTOR, PersonalCabinet.login_field)

        assert actual_name
        assert actual_email

        driver.quit()

    def test_login_from_registration_form_success(self): # Авторизация из формы регистрации
        driver = webdriver.Chrome()

        driver.get(site)
        driver.find_element(By.XPATH, HomePage.LoginButton).click()
        driver.find_element(By.CSS_SELECTOR, AuthorizationPage.registration).click()
        driver.find_element(By.CSS_SELECTOR, RegistrationPage.LoginButton).click()

        name_field = driver.find_element(By.CSS_SELECTOR, AuthorizationPage.email_field)
        name_field.send_keys(entities['email'])

        pass_field = driver.find_element(By.CSS_SELECTOR, AuthorizationPage.password_field)
        pass_field.send_keys(entities['valid_password'])

        driver.find_element(By.CSS_SELECTOR, AuthorizationPage.LoginButton).click()
        driver.find_element(By.CSS_SELECTOR, AuthorizationPage.personalcabinet).click()

        driver.implicitly_wait(3)
        actual_name = driver.find_element(By.CSS_SELECTOR, PersonalCabinet.name_field)
        actual_email = driver.find_element(By.CSS_SELECTOR, PersonalCabinet.login_field)

        assert actual_name
        assert actual_email

        driver.quit()

    def test_login_with_password_recovery_frame_success(self): #Авторизация через страницу востановления пароля
        driver = webdriver.Chrome()

        driver.get(site)
        driver.find_element(By.XPATH, HomePage.LoginButton).click()
        driver.find_element(By.XPATH, AuthorizationPage.password_recovery).click()
        driver.find_element(By.XPATH, RecoveryPasswordPage.LoginButton).click()

        name_field = driver.find_element(By.CSS_SELECTOR, AuthorizationPage.email_field)
        name_field.send_keys(entities['email'])

        pass_field = driver.find_element(By.CSS_SELECTOR, AuthorizationPage.password_field)
        pass_field.send_keys(entities['valid_password'])

        driver.find_element(By.CSS_SELECTOR, AuthorizationPage.LoginButton).click()
        driver.find_element(By.CSS_SELECTOR, AuthorizationPage.personalcabinet).click()

        driver.implicitly_wait(3)
        actual_name = driver.find_element(By.CSS_SELECTOR, PersonalCabinet.name_field)
        actual_email = driver.find_element(By.CSS_SELECTOR, PersonalCabinet.login_field)

        assert actual_name
        assert actual_email

        driver.quit()

    def test_logout_success(self): #Выход из Аккаунта
        driver = webdriver.Chrome()

        driver.get(site)
        driver.find_element(By.XPATH, HomePage.LoginButton).click()

        name_field = driver.find_element(By.CSS_SELECTOR, AuthorizationPage.email_field)
        name_field.send_keys(entities['email'])

        pass_field = driver.find_element(By.CSS_SELECTOR, AuthorizationPage.password_field)
        pass_field.send_keys(entities['valid_password'])

        driver.implicitly_wait(1)
        driver.find_element(By.CSS_SELECTOR, AuthorizationPage.LoginButton).click()
        driver.find_element(By.CSS_SELECTOR, AuthorizationPage.personalcabinet).click()
        driver.find_element(By.XPATH, PersonalCabinet.LogOutButton).click()

        reg_page = driver.find_element(By.CSS_SELECTOR, AuthorizationPage.LoginButton)

        assert reg_page.is_displayed()

        driver.quit()

class TestRouting: # Тест переходов между страницами

    def test_routing_from_HomePage_to_PersonalCabinet_success(self): # Переход с Домашней страницы в Личный кабинет при авторизации успешно происходит

        driver = webdriver.Chrome()

        driver.get(site)
        driver.find_element(By.XPATH, HomePage.LoginButton).click()

        name_field = driver.find_element(By.CSS_SELECTOR, AuthorizationPage.email_field)
        name_field.send_keys(entities['email'])

        pass_field = driver.find_element(By.CSS_SELECTOR, AuthorizationPage.password_field)
        pass_field.send_keys(entities['valid_password'])

        driver.find_element(By.CSS_SELECTOR, AuthorizationPage.LoginButton).click()
        driver.find_element(By.CSS_SELECTOR, AuthorizationPage.personalcabinet).click()

        driver.implicitly_wait(3)
        profile_button = driver.find_element(By.CSS_SELECTOR, PersonalCabinet.ProfileButton)
        order_history_button = driver.find_element(By.CSS_SELECTOR, PersonalCabinet.OrderHistoryButton)
        logout_button = driver.find_element(By.XPATH, PersonalCabinet.LogOutButton)

        assert profile_button
        assert order_history_button
        assert logout_button

        driver.quit()

    def test_routing_to_constructor_from_personal_cabinet_by_string(self): # переход в конструктор нажатием на строку "Конструктор"
        driver = webdriver.Chrome()

        driver.get(site)
        driver.find_element(By.XPATH, HomePage.LoginButton).click()

        name_field = driver.find_element(By.CSS_SELECTOR, AuthorizationPage.email_field)
        name_field.send_keys(entities['email'])

        pass_field = driver.find_element(By.CSS_SELECTOR, AuthorizationPage.password_field)
        pass_field.send_keys(entities['valid_password'])

        driver.find_element(By.CSS_SELECTOR, AuthorizationPage.LoginButton).click()
        driver.find_element(By.CSS_SELECTOR, AuthorizationPage.personalcabinet).click()
        driver.find_element(By.XPATH, HomePage.constructor).click()

        welcome_title = driver.find_element(By.XPATH, HomePage.WelcomeTitle)

        assert welcome_title.is_displayed()

        driver.quit()

    def test_routing_in_constructor_from_personal_cabinet_click_on_logo(self): # переход в конструктор нажатием на логотип

        driver = webdriver.Chrome()

        driver.get(site)
        driver.find_element(By.XPATH, HomePage.LoginButton).click()

        name_field = driver.find_element(By.CSS_SELECTOR, AuthorizationPage.email_field)
        name_field.send_keys(entities['email'])

        pass_field = driver.find_element(By.CSS_SELECTOR, AuthorizationPage.password_field)
        pass_field.send_keys(entities['valid_password'])

        driver.find_element(By.CSS_SELECTOR, AuthorizationPage.LoginButton).click()
        driver.find_element(By.CSS_SELECTOR, AuthorizationPage.personalcabinet).click()
        driver.find_element(By.CSS_SELECTOR, HomePage.LogoTitle).click()

        welcome_title = driver.find_element(By.XPATH, HomePage.WelcomeTitle)

        assert welcome_title.is_displayed()

        driver.quit()

class TestConstructorRouting: # Переходы в конструктере

    def test_navigate_to_filling_section_first_item_check(self): # переход к разделу "Начинки" с проверкой названия секции и одного из первых элементов

        driver = webdriver.Chrome()

        driver.get(site)

        driver.find_element(By.XPATH, ConstructorPage.FillingSectionTab).click()

        filling_section = driver.find_element(By.XPATH, ConstructorPage.FillingSection)

        one_of_first = driver.find_element(By.CSS_SELECTOR, ConstructorPage.FirstElementInSection)

        assert filling_section.is_displayed()
        assert one_of_first.is_displayed()

        driver.quit()

    def test_navigate_to_filling_section_first_item_check(self):  # Переход к разделу "Начинки", "Соусы", "Булки" с проверкой названия секции и одного из первых элементов

        driver = webdriver.Chrome()

        driver.get(site)

        driver.find_element(By.XPATH, ConstructorPage.FillingSectionTab).click()
        filling_section = driver.find_element(By.XPATH, ConstructorPage.FillingSection)
        one_of_first_filling = driver.find_element(By.CSS_SELECTOR, ConstructorPage.FirstElementInSectionFilling)

        assert filling_section.is_displayed()
        assert one_of_first_filling.is_displayed()

        driver.find_element(By.XPATH, ConstructorPage.SouseSectionTab).click()
        souse_section = driver.find_element(By.XPATH, ConstructorPage.SouseSection)
        one_of_first_souse = driver.find_element(By.CSS_SELECTOR, ConstructorPage.FirstElementInSectionSouse)

        assert souse_section.is_displayed()
        assert one_of_first_souse.is_displayed()

        driver.find_element(By.XPATH, ConstructorPage.BunSectionTab).click()
        bun_section = driver.find_element(By.XPATH, ConstructorPage.BunSection)
        one_of_first_bun = driver.find_element(By.CSS_SELECTOR, ConstructorPage.FirstElementInSectionBun)

        assert bun_section.is_displayed()
        assert one_of_first_bun.is_displayed()

        driver.quit()