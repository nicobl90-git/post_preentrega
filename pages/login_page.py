#Todo lo relacionado a lo que hace mi login
#Copio el método que redacté en Helpers y lo traigo acá
#Voy a traer el driver, el username y password

#LO QUE NECESITO:
#La URL
#El driver
#Los selectores y modulos de selenium que me permiten traerlos

#-----------------------------------------------------
# ESTRUCTURA DE LA CLASE 09
#-----------------------------------------------------
"""
#-----------------------------------------------------
ANTERIORMENTE LO HACIAMOS ASÍ:

def login(driver, username, password):

    # wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com")

    wait.until(
        EC.presence_of_element_located((By.ID, "user-name"))
    ).send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
#-----------------------------------------------------
"""


"""
from selenium.webdriver.support.ui import WebDriverWait #para generar esperas en ciertas partes del código
from selenium.webdriver.support import expected_conditions as EC #creo condiciones esperadas para despues utilizarlas en el codigo.
from selenium.webdriver.common.by import By #para localizar los elementos

#PRIMERO DEFINO EL CONSTRUCTOR

class LoginPage:

    #puedo definir la URL en una variable global para referenciarla en el resto de scripts
    URL = "https://www.saucedemo.com"

    #Puedo definir también variables privadas para hacer referencia a los locators y evitar repeticiones tediosas
    #Le pongo guion bajo y mayusculas para definir que son privadas

    _USERNAME = (By.ID, "user-name") #Este selector podría cambiar a futuro en la web y lo cambio solo desde acá
    _PASSWORD = (By.ID, "password") #Este selector podría cambiar a futuro en la web y lo cambio solo desde acá
    _LOGIN_BUTTON = (By.ID, "login-button") #Este selector podría cambiar a futuro en la web y lo cambio solo desde acá
    #El mensaje combinado es: "este valor es fijo (constante) y pertenece solo a esta clase (privado)".


    #defino el driver primero
    def __init__(self, driver):
        self.driver = driver
        #Coloco el Wait dentro del mismo constructor
        self.wait = WebDriverWait(self.driver, 10)

    #Puedo definir un método para que abra el navegador con la URL
    def open(self):
        self.driver.get(self.URL) #el driver abre la URL como parámetro que definí antes
        return self

    def login(self, username, password):
        self.wait.until(
            EC.presence_of_element_located(self._USERNAME) #Acá remplazo el locator por la variable que definí antes
        ).send_keys(username)
        self.driver.find_element(*self._PASSWORD).send_keys(password) #Acá remplazo el locator por la variable que definí antes
        self.driver.find_element(*self._LOGIN_BUTTON).click() #Acá remplazo el locator por la variable que definí antes

"""      
#-----------------------------------------------------
# ESTRUCTURA A PARTIR DE LA CLASE 10
#-----------------------------------------------------

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # URL de la página de login
    URL = "https://www.saucedemo.com/"
    # Locators (selectores de elementos)
    _USER_INPUT = (By.ID, "user-name")
    _PASS_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        """
        Constructor que recibe la instancia del WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open(self):
        """Navegar a la página de login"""
        self.driver.get(self.URL)
        return self
 
    def completar_usuario(self, usuario):
        """Escribir el nombre de usuario"""
        campo = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT))
        campo.clear()
        campo.send_keys(usuario)
        return self
 
    def completar_clave(self, clave):
        """Escribir la contraseña"""
        campo = self.driver.find_element(*self._PASS_INPUT)
        campo.clear()
        campo.send_keys(clave)
        return self
    
    def enviar(self):
        """Hacer clic en el botón de login"""
        self.driver.find_element(*self._LOGIN_BUTTON).click()
        return self