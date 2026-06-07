from selenium import webdriver #utilizo el driver para despues guardarlo en una variable
from webdriver_manager.chrome import ChromeDriverManager #Traigo el driver para el navegador que quiero trabajar
from selenium.webdriver.chrome.service import Service #Este servicio recibe el chrome driver manager y me instala la version correcta segun mi navegador
import pytest #para utilizar la funcion de fixture

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()