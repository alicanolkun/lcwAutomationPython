import unittest

from selenium import webdriver
from selenium.webdriver.common import by

driver = webdriver.Chrome()
from selenium.webdriver.common.by import By

title = "menu-header-item__title"

class MyTestCase(unittest.TestCase):


    def test_Case(self):
        url = "https://www.lcwaikiki.com/tr-TR/TR "
        driver.maximize_window()
        driver.get(url)
        driver.find_element(By.CLASS_NAME, title).click()

        driver.find_element(By.CSS_SELECTOR,'.col-sm-4.pl-0.image_Box.visible-lg.visible-md').click()

        name = driver.find_element(By.CSS_SELECTOR, ".product-card__title").text
        self.assertIn("Kadın", name)

        driver.find_element(By.CSS_SELECTOR,'.product-card').click()
        cartTitle = driver.find_element(By.ID,'pd_add_to_cart').text
        self.assertEqual("SEPETE EKLE",cartTitle)
        driver.find_element(By.CSS_SELECTOR,'#option-size > a').click()
        driver.find_element(By.ID,'pd_add_to_cart').click()
        driver.find_element(By.ID,'shopping-cart').click()
        cartText =driver.find_element(By.CSS_SELECTOR,'.col-md-12.cart-header.mb-20>span').text
        self.assertIn("Sepetim (1 Ürün)",cartText)
        driver.find_element(By.XPATH,'//span[contains(text(),"Devam")]').click()
        driver.find_element(By.CSS_SELECTOR,'.header__middle__left>a').click()
        fastDeliveryText = driver.find_element(By.CSS_SELECTOR,'.fast-delivery>a').text
        self.assertIn("Hızlı Teslimat",fastDeliveryText)


    def tearDown(self):
      driver.quit()





if __name__ == '__main__':
    unittest.main()
