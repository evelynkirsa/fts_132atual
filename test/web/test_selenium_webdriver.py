# Importar Bibliotecas
import pytest
from selenium import webdriver
# 2 Classe
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class Test_selenium_webdriver():

    # Definição de Inicio - Executa Antes do teste
    def setup_method(self):
        # Declarar o objeto do selenium e instanciar como o navegador desejando
        self.driver = webdriver.Chrome('C:/Users/User/PycharmProjects/fts_132/drivers/chromedriver.exe')
        self.driver.implicitly_wait(30)  # O selenium vai esperar ate 30 segundos pelos elementos
        self.driver.maximize_window()  # vai maximizar a janela do navegador

    # Definição de fim - Executa depois do teste
    def teardown_method(self):
        # Destruir o objeto do Selenium
        self.driver.quit()

    # Definição do teste
    # Definição do Teste
    @pytest.mark.parametrize('termo, curso, preco', [
        ('mantis', 'Mantis', 'R$ 59,99'),
        ('ctfl', 'Preparatório CTFL', 'R$ 199,00'),
    ])
    def testar_comprar_curso_mantis_com_click_na_lupa(self, termo, curso, preco):
        # O Selenium abre a url indicada - site alvo do teste
        self.driver.get('https://www.iterasys.com.br')
        # O Selenium clica na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').click()
        # O Selenium apaga o conteúdo da caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').clear()
        # O Selenium escreve 'mantis' na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').send_keys(termo)
        # O Selenium clica no botão da lupa
        self.driver.find_element(By.ID, 'btn_form_search').click()
        # O Selenium clica em 'Matricule-se'
        self.driver.find_element(By.CSS_SELECTOR, 'span.comprar').click()
        # O Selenium valida o nome do curso no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text == curso
        # O Selenium valida o preço do curso
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text == preco

    def testar_comprar_curso_mantis_com_enter(self):
        # O selenium abre a url indicada - site alvo do teste
        self.driver.get('https://iterasys.com.br')
        # O selenium clica na caia de pesquisa
        self.driver.find_element(By.ID, 'searchtext').click()
        # O selenium apaga o conteudo da caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').clear()
        # O selenium escreve 'mantis' na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').send_keys('Mantis')
        # O selenium clica no botão pesquisar
        self.driver.find_element(By.ID, 'btn_form_search').send_keys(Keys.ENTER)
        # O selenium clica em matricule-se
        self.driver.find_element(By.CSS_SELECTOR, 'span.comprar').click()
        # O selenium valida o nome do curso no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text == 'Mantis'
        # O selenium valida o preço do curso
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text == 'R$ 59,99'

