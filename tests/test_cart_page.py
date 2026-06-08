#-----------------------------------------------------
# ESTRUCTURA DE LA CLASE 09
#-----------------------------------------------------

from pages.login_page import LoginPage
from pages.cart_page import CartPage


def test_cart_page(driver):
    LoginPage(driver).open().completar_usuario("standard_user").completar_clave("secret_sauce").enviar() #Llamo al método de login para iniciar sesión antes de probar el inventario    
    
    cart_page = CartPage(driver) #Instancio la clase CartPage para probar sus métodos
    cart_page.agregar_primer_producto() #Agrego el primer producto al carrito
    
    contador = cart_page.obtener_contador_carrito() #Obtengo el número de productos en el carrito
    print(f"El contador del carrito muestra: {contador}")

    cart_page.ir_al_carrito() #Navego a la página del carrito

    cart_page.hacer_logout() #Hago logout para cerrar sesión al finalizar el test
