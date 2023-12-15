from selenium import webdriver
import time


options = webdriver.ChromeOptions()
options.add_argument("--incognito")
#options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

while True:
    driver.get("https://nakarmpsa.olx.pl")

    #Opcjonalny timer, żeby strona się na pewno załadowała
    time.sleep(2)

    #Pomiędzy kolejnymi okienkami z psami zmienia się tylko 4. cyfra w [] o +=1
    #Zawsze tylko nienakarmiony pies będzie na 1. miejscu więc nie ma sensu się bardziej bawić
    driver.find_element("xpath", '/html/body/div[1]/div/section[2]/div/div/div[2]/div/div[1]/div/div[4]/div[1]/div[1]').click()
