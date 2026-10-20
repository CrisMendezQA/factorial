from playwright.sync_api import Page, expect
import pytest

def test_calcular_factorial_numero_entero_positivo (page: Page):
    print("Given el usuario abre la página de factorial")
    page.goto("https://qainterview.pythonanywhere.com/")

    print("When introduce un número positivo 3")
    page.get_by_role("textbox", name="Enter an integer").fill("3")

    print("And hace click en calcular")
    page.get_by_role("button", name="Calculate!").click()

    print("Then debe ver el resultado del factorial 6")
    expect(page.locator("#resultDiv")).to_contain_text("6")

def test_calcular_factorial_valor_no_numerico (page: Page):
    print("Given el usuario abre la página de factorial")
    page.goto("https://qainterview.pythonanywhere.com/")

    print("When introduce un valor de texto")
    page.get_by_role("textbox", name="Enter an integer").fill("text")

    print("And hace click en calcular")
    page.get_by_role("button", name="Calculate!").click()

    print("Then debe ver un mensaje de error")
    expect(page.get_by_text("Please enter an integer")).to_be_visible()


@pytest.mark.skip(reason="Este test se deja desactivado porque existe un error conocido https://crismendezqa.atlassian.net/browse/QA-2")
def test_calcular_factorial_numero_negativo (page: Page):
    print("Given el usuario abre la página de factorial")
    page.goto("https://qainterview.pythonanywhere.com/")

    print("When introduce un número entero negativo")
    page.get_by_role("textbox", name="Enter an integer").fill("-1")

    print("And hace click en calcular")
    page.get_by_role("button", name="Calculate!").click()

    print("Then debe ver un mensaje de error")
    expect(page.get_by_text("Please enter an integer")).to_be_visible()



