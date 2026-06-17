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

BASE = 'https://jsonplaceholder.typicode.com'

@pytest.fixture(scope='module')
def posts_url():
  return f"{BASE}/posts"

@pytest.fixture(scope='module')
def post_by_id_url():
  def _get_url(post_id):
    return f"{BASE}/posts/{post_id}"
  return _get_url

def pytest_html_results_table_header(cells):
    """Añade una columna 'URL' justo después de 'Test ID'."""
    cells.insert(2, 'URL')

def pytest_html_results_table_row(report, cells):
    """Rellena la columna con la URL almacenada en el atributo 'page_url'."""
    cells.insert(2, getattr(report, 'page_url', '-'))

#conftest.py - Agrega al inicio del archivo
import pathlib

#Carpeta donde guardamos las capturas
target = pathlib.Path('reports/screens')
target.mkdir(parents=True, exist_ok=True) #Crea si no existe

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
   """Se ejecuta despues de cada fase (setup/call/teardown) de cada test"""
   outcome = yield #Dejamos que Pytest genere el reporte
   report = outcome.get_result() #Obtenemos el objeto report

   #Solo capturamos en fallos de la fase principal
   if report.when == 'call' and report.failed:
      driver = item.funcargs.get('driver') #Obtenemos el fixture driver
      if driver:
         file_name = target / f"{item.name}.png"
      driver.save_screenshot(str(file_name)) #Captura
         
         #Adjuntamos al reporte HTML
      if hasattr(report,'extra'):
            report.extra.append({
               'name': 'screenshot',
               'format': 'image',
               'content': str(file_name)
            })

"""
tryfirst=True = Ejecuta este hook antes que otros

hookwrapper=True = Permite envolver la ejecución

outcome = yield = Pausa para que Pytest haga su trabajo

report.when == 'call' = Solo en la fase de ejecución principal

report.failed = Solo cuando el test falló

"""

# Cambia el título del reporte
def pytest_html_report_title(report):
    report.title = "TalentoLab – Resumen de ejecución"

# Agrega datos a la sección Environment
def pytest_configure(config):
    if hasattr(config, "_metadata"):
        config._metadata["Proyecto"] = "TalentoLab"
        config._metadata["Descripción"] = "Suite UI + API completa"
        config._metadata["Entorno"] = "Testing"

