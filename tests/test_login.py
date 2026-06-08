#Voy a importar el login_page para poder utilizar sus métodos y así evitar repetir código en cada test

from pages.login_page import LoginPage #Importa la clase LoginPage desde esa localización
#Importo los usuarios de USERS.CSV para poder utilizarlos en el test de login
from utils.datos import leer_csv_login
import pytest #para utilizar la funcion de PARAMETRIZAR

#Voy a INSTANCIAR la clase LoginPage para poder utilizar sus métodos

@pytest.mark.parametrize("username, password, debe_funcionar", leer_csv_login("data/users.csv")) #Utilizo la función de parametrizar para leer los datos del CSV y pasarlos como parámetros al test
def test_login(driver, username, password, debe_funcionar):
    #-------
    #Una forma de hacerlo es la siguiente:

    #LoginPage(driver).open() 
    #LoginPage(driver).login("standard_user", "secret_sauce")

    #-------
    #Para que el código sea mas legible, hago lo siguiente:

    login_page = LoginPage(driver) #Instancio la clase y le paso el driver como parámetro

    login_page.open()
    login_page.completar_usuario(username) #Llamo al método de completar usuario y le paso el username como parámetro
    login_page.completar_clave(password) #Llamo al método de completar contraseña y le paso el password como parámetro
    login_page.enviar() #Llamo al método de hacer login para iniciar sesión


