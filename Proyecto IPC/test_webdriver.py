from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Configuración del controlador Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())

# Abre una página web
driver.get("https://www.google.com")
print("¡Selenium y WebDriver funcionan correctamente!")
driver.quit()
