TRABAJOS Y EJERCICIOS DE LA CLASE 09 EN ADELANTE

SE ELIMINA EL ARCHIVO DE PREENTREGA Y CARPETA ANTERIOR DE TEST

CLASE 09: POM
-Cambios hechos:
    --Se crean las carpetas Pages, Tests y Data
    --Se refactoriza la parte de Login, Inventory y Cart (tanto en Pages como Tests)
    --El pytest corre statisfactoriamente para las 3 páginas

CLASE 10: MANEJO DE DATOS DE PRUEBA
-Cambios hechos:
    --Creo la rama feature/csv_users
    --Agrego el archivo users.csv
    --Modifico el archivo Login para que tome los datos csv (tanto Page como Test)
    --Modifico el metodo Login de los archivos Inventory y Cart para que corran bien
    --Pytest corre bien el Login con los usuarios csv y los otros dos tests
    --Creo el archivo json para productos
    --Separo casos de Login y Cart según usuarios (USERS y csv) y productos por json o por hardcode
    --Elimino los tests de Faker por ahora
    --Genero reporte html con el comando pytest --html=reporte.html --self-contained-html
    

CLASE 11: Automatización de pruebas de API (1)
-Cambios hechos:
    --Creo la rama feature/requests
    --Creo los tests básicos, get, post y login
    --Todos corren bien con pyest/python3
    --Agrego markers a los tres tests y al archivo pytest.ini
    --Corro todos los comandos satisfactoriamente
        pytest -m api -v
        pytest tests_api/ -v
        pytest tests/ tests_api/ --html=reporte_completo.html