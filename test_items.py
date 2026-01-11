import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize(
    "link", ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"]
)
def test_add_to_cart_btn(browser, link):
    browser.get(link)
    assert browser.find_element(
        By.CSS_SELECTOR, "button.btn-add-to-basket"
    ), f'"Add to cart" button is not found at page {link}'
