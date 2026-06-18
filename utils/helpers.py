from selenium.webdriver.common.by import By

# Función reutilizable de login. El driver se encuentra en la carpeta conftest.py como fixture
def login(driver):
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "/inventory.html" in driver.current_url
    print ("La URL contiene 'Inventory'")

def validate_api_response(response, expected_status,
    expected_fields=None, max_time=1.0):
        """Función helper para validar respuestas API con los 5
    niveles"""
        # Nivel 1: Status
        assert response.status_code == expected_status
        # Nivel 2: Headers
        if expected_status != 204: # 204 No Content puede no tener Content-Type
            assert 'application/json' in response.headers.get('Content-Type', '')
        # Nivel 3-4: Estructura y contenido (si hay expected_fields)
        if expected_fields and response.text:
            body = response.json()
            assert expected_fields <= set(body.keys())
        # Nivel 5: Performance
        assert response.elapsed.total_seconds() < max_time
        return response.json() if response.text else {}
