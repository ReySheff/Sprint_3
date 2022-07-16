class HomePage: #Основная страница

    LoginButton = '//*[@id="root"]/div/main/section[2]/div/button'  # Войти в аккаунт
    personalcabinet = '#root > div > header > nav > a > p'  # Личный кабинет
    constructor = './/p[contains(text(), "Констру")]'  # Конструктор
    WelcomeTitle = './/h1[contains(text(), "Собери")]'  # Текст "Соберите бургер"
    LogoTitle = 'div > a > svg'  # Логотип

class AuthorizationPage: # Страница авторизации
    registration = 'a[href*="register"]'  # Кнопка "Зарегистрироваться"
    personalcabinet = '#root > div > header > nav > a > p' # Кнопка Личный кабинет
    LoginButton = '#root > div > main > div > form > button'  # Кнопка "Войти"
    email_field = 'form > fieldset:nth-child(1) > div > div > input'  # Поле "Email"
    password_field = 'form > fieldset:nth-child(2) > div > div > input'  # Поле "Пароль"
    password_recovery = './/a[contains(text(), "станови")]' # Кнопка Востановить пароль


class RecoveryPasswordPage: # Страница Востановления пароля
    LoginButton = './/a[contains(text(), "Войти")]'  # Кнопка "Войти"

class RegistrationPage: # Страница регистрации
    name_field = 'form > fieldset:nth-child(1) > div > div > input'  # Поле "Имя"
    email_field = 'form > fieldset:nth-child(2) > div > div > input'  # Поле "Email"
    password_field = '[type="password"]'  # Поле "Пароль"
    reg_button = './/button[contains(text(), "арегист")]'  # Кнопка "Зарегистрироваться"
    reg_error = '[class="input__error text_type_main-default"]'  # Поп-ап ошибки
    LoginButton = '#root > div > main > div > div > p > a' # Кнопка "Войти"

class PersonalCabinet: # Страница Личного кабинета
    name_field = 'input[value*=ндре]'  # Поле "Имя"
    login_field = 'input[value*=hevchen]'  # Поле "Логин"
    LogOutButton = './/button[contains(text(), "ыход")]' # Кнопка Выход
    ProfileButton = 'a[href*="profile"]'  # Кнопка "Профиль"
    OrderHistoryButton = 'a[href*="order-history"]' # Кнопка истории заказов

class ConstructorPage:
    FillingSectionTab = './/span[contains(text(), "Начинки")]'  # Таб "Начинки"
    FillingSection = './/h2[contains(text(), "ачинк")]'  # Секция "Начинки"
    FirstElementInSectionFilling = '[alt~=метеорит]'  # Один из первых элементов секции "Начинки"
    SouseSectionTab = './/span[contains(text(), "оусы")]' # Таб "Соусы"
    SouseSection = './/h2[contains(text(), "Соусы")]'  # Секция "Соусы"
    FirstElementInSectionSouse = '[alt~=Spicy-X]'  # Один из первых элементов секции "Соусы"
    BunSectionTab = './/span[contains(text(), "улки")]'  # Таб "Булки"
    BunSection = './/h2[contains(text(), "Булки")]'  # Секция "Булки"
    FirstElementInSectionBun = '[alt~=R2-D3]'  # Один из первых элементов секции "Булки"