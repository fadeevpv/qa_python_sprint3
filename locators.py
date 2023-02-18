# links
main_page = 'https://stellarburgers.nomoreparties.site/'   #ссылка на страницу авторизации
registration_page = 'https://stellarburgers.nomoreparties.site/register'  #ссылка на страницу регистрации
recovery_password_page = 'https://stellarburgers.nomoreparties.site/forgot-password' #ссылка на страницу восстановления пароля

# buttons
button1_inter_user_page = '//button[text()="Войти"]'  #кнопка войти на странице входа
button2_reg_user_registartion_page = '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]' #кнопка зарегестрировать на странице регистрации
button3_take_order_main_page = '//button[text()="Оформить заказ"]'  #кнопка оформит ьзаказ на странице конструктора после авторизациии
button4_inter_reg_page = '//a[@href="/login"]' #кнопка войти на странице регистрации пользователя
button5_inter_account_main_page = '//button[text()="Войти в аккаунт"]' #кнопка войти на главной странице
button6_personal_page_from_main_page = '//p[text()="Личный Кабинет"]'  #кнопка перехода в личный кабинет на главной странице
button7_inter_from_registration_page = '//a[@href="/login"]'  #кнопка Войти на страниции регистрации для перехода в авторизации
button8_inter_from_recovery_password_page = '//a[@class="Auth_link__1fOlj"]' #кнопка для перехода к странице регистрации
button9_inter_to_constructor = '//p[text()="Конструктор"]'   #переход к конструктору
button10_logout = '//button[text()="Выход"]'

# input forms
input_name_user_reg_page = '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'  #форма ввода имени пользователя на странице регистрации
input_email_user_reg_page = '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input' #формма вода электронной почты на странице регистрации
input_user_password_reg_page = '//input[@name="Пароль"]'                                  #форма ввода пароля на страниции регистрации
input_email_login_page = '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'    #формма вода электронной почты на странице атворизации
input_password_login_page = '//input[@name="Пароль"]'                                     #форма ввода пароля на страниции авторизации
information_about_page = '//p[text()="В этом разделе вы можете изменить свои персональные данные"]' #информация о личном кабинете пользователя

# erros
error_message_invalid_password_registartion_page = '//p[text()="Некорректный пароль"]'   #ошибка ввода некорретного пароля

# links_locators
lik_to_sterra_burgers = '//*[@id="root"]/div/header/nav/div/a'  #ссылка \ кнопка для перехода к конструктору по логотипу

# headers
construct_burgers = '//h1[@class="text text_type_main-large mb-5 mt-10"]'  #Название страницы Конструктор бургеров
header_inter_page = '//h2[text()="Вход"]'                                  #Название загаловка ВХОД на странице атворизации

# constructor sections
rolls = '//span[text()="Булки"]'          #для перехода к разделу булки
sauces = '//span[text()="Соусы"]'         #для перехода к разделу соусы
filling = '//span[text()="Начинки"]'      #для перехода к разделу начинка

# burger elements
fillings_cheese_with_asteroid_mold = '//*[@id="root"]/div/main/section[1]/div[2]/ul[3]/a[9]'   #последний элемент списка начинок
sauces_traditional_galactic_sauce = '//*[@id="root"]/div/main/section[1]/div[2]/ul[2]/a[3]'    #последний элемент ссписка соусов
rolls_crater_roll_n_200i = '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[2]/img'         #последний элемент списка булок

#detail elements
asteroid_mold_check = '//*[@id="root"]/div/section[1]/div[1]/div/p'   #для проверки послднего элемента в списке начинок
galactic_sauce_check = '//*[@id="root"]/div/section[1]/div[1]/div/p'  #для проверки послднего элемента в списке соусов
rolls_crater_check = '//*[@id="root"]/div/section[1]/div[1]/div/p'    #для проверки послднего элемента в списке булок

# user credentials
user_mail = 'fadeev_qa_python_06@ya.ru'
user_password = '123456'







