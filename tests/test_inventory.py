from pages.login_page import LoginPage
from pages.inventory import InventoryPage


def test_inventory(driver):
    LoginPage(driver).open().completar_usuario("standard_user").completar_clave("secret_sauce").enviar() #Llamo al método de login para iniciar sesión antes de probar el inventario    
    
    
    inventory_page = InventoryPage(driver) #Corroboro el título de la página
    titulo = inventory_page.obtener_titulo()
    print(f"El título obtenido es: {titulo}")
    #assert titulo == "Products", f"Se esperaba 'Products' pero se obtuvo '{titulo}'"

    inventory_page.obtener_productos() #Corroboro la cantidad de productos
    print(f"Se encontraron {len(inventory_page.obtener_productos())} productos en la página de inventario.")

    

