from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
 
    URL = "https://www.saucedemo.com"
    _TITLE = (By.CLASS_NAME, "title")
    _PRODUCTS = (By.CLASS_NAME, "inventory_item")
    _ADD_BUTTONS = (By.CSS_SELECTOR, "button[data-test*='add-to-cart']")
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    _MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    _LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):              
        self.driver.get(self.URL)
        return self

    def obtener_titulo(self):
        """Obtiene el título de la página de inventario."""
        return self.driver.find_element(*self._TITLE).text
    
    def obtener_productos(self):
        #Obtiene la lista de productos disponibles.
        return self.driver.find_elements(*self._PRODUCTS)
    
    
