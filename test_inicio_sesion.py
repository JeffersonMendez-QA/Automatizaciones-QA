import pytest
from playwright.sync_api import Page, expect

def test_login_y_busqueda_solicitud(page: Page):
    # 1. Login
    page.goto("https://siu-qa.scalahed.info/usuarios/login/#")
    page.get_by_placeholder("Ingresa tu matrícula").fill("000585051")
    page.locator("#id_password").fill("@Jefferson7")
    page.get_by_text("Entrar").click()

  
    
#  Pasar el cursor sobre el contenedor general de la barra lateral para desplegarla
    page.locator("#menuLateral").hover()

    #  Esperar a que la opción #item4 sea clickeable y hacer clic
    item_solicitud = page.locator("#item4")
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
    """opcion_buscar = page.locator("span.buscarPersonaMenu").first
    opcion_buscar.wait_for(state="visible")
    opcion_buscar.click()"""
   
    # 4. Formulario de Búsqueda por Matrícula
    
    page.locator("#id_matricula").fill("010785069")
    page.locator("#search_app").click()