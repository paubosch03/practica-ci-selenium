from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class WebCheck(LiveServerTestCase):
    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.selenium = webdriver.Chrome(options=options)

    def tearDown(self):
        self.selenium.quit()

    def test_home_page_title(self):
        # Obre la pàgina principal
        self.selenium.get(self.live_server_url)
        # Comprova que el títol visible (h1) és el correcte
        body_text = self.selenium.find_element(By.TAG_NAME, "body").text
        self.assertIn("Portal segur", body_text)
