import pytest
from playwright.sync_api import Page, expect

def test_login_y_busqueda_solicitud(page: Page):
    # Login
    page.goto("https://siu-qa.scalahed.info/usuarios/login/#")
    page.get_by_placeholder("Ingresa tu matrícula").fill("000585051")
    page.locator("#id_password").fill("@Jefferson7")
    page.get_by_text("Entrar").click()

  
    
#  Pasar el cursor sobre el contenedor general de la barra lateral para desplegarla
    page.locator("#menuLateral").hover()

    #  Esperar a que la opción #item4 sea clickeable y hacer clic
    item_solicitud = page.locator("#item4")#mediante id es mejor
    item_solicitud.wait_for(state="visible")
    item_solicitud.click()


# 2. Navegación menú lateral
    nav_sistema = page.locator("#sistema").first
    nav_sistema.hover()
   
# Clic en el li dentro de div.solicitudes
    opcion_solicitud = nav_sistema.locator("div.solicitudes li").nth(1)
    opcion_solicitud.wait_for(state="visible")
    opcion_solicitud.click()

    # 3. Clic en Buscar Persona
   
    # 4. Formulario de Búsqueda por Matrícula

    input_matricula = page.locator("#id_matricula")
    input_matricula.wait_for(state="visible")
    
    # Enfocar y escribir carácter por carácter bien chimba
    input_matricula.click()
    input_matricula.clear()
    input_matricula.press_sequentially("010785069", delay=100)

    input_matricula.press("Enter")

    # Si pasa la aserción previa, ahora sí presionamos buscar
    page.locator("#search_app").click()

# Localizar el enlace <a> que dice "ALUMNO"
    enlace_alumno = page.get_by_role("link", name="ALUMNO")
    
    # Validar que el enlace sea visible en la sección de resultados
    expect(enlace_alumno).to_be_visible(timeout=10000)
    
    # Hacer clic para ir al perfil
    enlace_alumno.click()

    page.screenshot(path="perfil_alumno.png") #captura

    # Pausa haber si lo puedo ver el perfil
    page.wait_for_timeout(3000)