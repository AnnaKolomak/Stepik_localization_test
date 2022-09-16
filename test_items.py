from selenium.webdriver.common.by import By
#from selenium.common.exceptions import NoSuchElementException
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_button_exist(browser):
    browser.get(link)
    #Уважаемый рецензент, расскоментируй следующую строчку для проверки
    #time.sleep(30)
    add_button = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button")
    assert add_button,"Button 'Add to busket' does not exist"   
    print("Текст кнопки: "+add_button.text)
 
