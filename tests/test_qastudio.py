'''
web-site: https://testqastudio.me/

test-case positive:
1. Открыть сайт https://testqastudio.me/
2. Перейти в раздел “Бестселлеры”
3. Найти товар “ДИВВИНА Журнальный столик” и открыть его описание
4. В описании найти и проверить артикул “C0MSSDSUM7”
'''

# импортируем модули и отдельные классы
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

url = "https://testqastudio.me/"
# каждый тест должен начинаться с test_
def test_product_view_sku():
    """
    Test case TMS#1 [web][pos][auto]
    """
		# Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    #chrome_options.add_argument("--headless") # спец. режим "без браузера"
	
		# устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service()
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
		
    driver.get(url=url)          # определяем адрес страницы для теста и переходим на неё
	
    	# ищем по селектору элемент меню "Бестселлеры" и кликаем по нему
    element_catalog = driver.find_element(by=By.CSS_SELECTOR, value="[class*='tab-best_sellers']")
    element_catalog.click()

		# ищем по селектору карточку "ДИВВИНА Журнальный столик" и кликаем по нему,
    # чтобы просмотреть детали
    element_card = driver.find_element(by=By.CSS_SELECTOR, value='[class*="post-11341"]') #[class*="post-11340"]
    element_card.click()
		# ищем по имени класса артикул для "Журнального столика"
    article = driver.find_element(By.CLASS_NAME, value="sku")
		# проверяем соответствие
    assert article.text == 'C0MSSDSUM7', "Wrong article"