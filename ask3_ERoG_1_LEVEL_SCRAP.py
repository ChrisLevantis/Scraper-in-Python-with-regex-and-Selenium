## HERE WE DO SCRAPING BUT WITH THE HELP OF SELENIUM, WE GET INFORMATION SUCH AS KODIKO_PLAISIOU, PLANO_DOSEON, TITLE
from lib2to3.pgen2 import driver
from selenium import webdriver

url = "https://www.plaisio.gr/pc-perifereiaka/laptops/apple-macbook"

driver = webdriver.Firefox(executable_path="C:\\Program Files\\geckodriver\\geckodriver.exe")
driver.get(url)

TITLE_LIST = []
KODIKOS_PLAISIOU_LIST = []
PLANO_DOSEON_LIST = []

##for title
products1 = driver.find_elements_by_class_name('product-title')
file_page_1 = open("page1.txt", "w", encoding='utf-8')
for product1 in products1:
    file_page_1.write(product1.text)
    file_page_1.write("\n")
    ##print(product1.text)
    TITLE_LIST.append(product1.text) ## bazo stin lista tous titlous proionton...
file_page_1.close()
print("----------TITLE SECTOR DONE----------")
##system("page1.txt")

class Title:
    def __init__(self, title):
        self.title = title

LIST_OF_OBJ_TITLE = []

LIST_OF_OBJ_TITLE.append(Title(TITLE_LIST)) ## EISAGOGI ANTIKIMENON TIPOU Title STIN LIST ME TA OBJECT 

for obj in LIST_OF_OBJ_TITLE:
    print( obj.title, sep =' ' )


##for kodikos-plaisio
products2 = driver.find_elements_by_class_name('sku')
file_page_2 = open("page1.txt", "a", encoding='utf-8')
for product2 in products2:
    file_page_2.write(product2.text)
    file_page_2.write("\n")
    ##print(product2.text)
    KODIKOS_PLAISIOU_LIST.append(product2.text)
file_page_2.close()
print("----------KODIKOS-PLAISIO SECTOR DONE----------")
##system("page1.txt")

class Kodikos_plaisio:
    def __init__(self, kodikos_plaisiou):
        self.kodikos_plaisiou = kodikos_plaisiou

LIST_OF_OBJ_KODIKOS_PLAISIOU = []

LIST_OF_OBJ_KODIKOS_PLAISIOU.append(Kodikos_plaisio(KODIKOS_PLAISIOU_LIST)) ## EISAGOGI ANTIKIMENON TIPOU Title STIN LIST ME TA OBJECT 

for obj in LIST_OF_OBJ_KODIKOS_PLAISIOU:
    print( obj.kodikos_plaisiou, sep =' ' )

##for plano doseon
products3 = driver.find_elements_by_class_name('installments')
file_page_2 = open("page1.txt", "a", encoding='utf-8')
for product3 in products3:
    file_page_2.write(product3.text)
    file_page_2.write("\n")
    ##print(product3.text)
    PLANO_DOSEON_LIST.append(product3.text)
file_page_2.close()
print("----------PLANO DOSEON SECTOR DONE----------")
##system("page1.txt")

class Plano_doseon:
    def __init__(self, plano_doseon):
        self.plano_doseon = plano_doseon

LIST_OF_OBJ_PLANO_DOSEON = []

LIST_OF_OBJ_PLANO_DOSEON.append(Plano_doseon(PLANO_DOSEON_LIST)) ## EISAGOGI ANTIKIMENON TIPOU Title STIN LIST ME TA OBJECT 

for obj in LIST_OF_OBJ_PLANO_DOSEON:
    print( obj.plano_doseon, sep =' ' )
