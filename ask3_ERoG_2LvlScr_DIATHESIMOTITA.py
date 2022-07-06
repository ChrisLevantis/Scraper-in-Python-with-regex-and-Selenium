## HERE WE DO 2 LEVEL SCRAP FOR THE INFORMATION AVAILABILITY IN EACH PRODUCT...
from selenium import webdriver
from lib2to3.pgen2 import driver

driver = webdriver.Firefox(executable_path="C:\\Program Files\\geckodriver\\geckodriver.exe")

file = open('links_html.txt', 'r') ## ANIGOUME TO ARXIO POU EXOUME DIMIOURGISI APO TO MEROS A, TO OPOIO PERIEXI OLA TA LINK GIA TO KATHE PROION, TO XRISIMOPOIOUME KAI STO KATHENA ZAXNOUME GIA TIN DIATHESIMOTITA

## kanoume driver.get to kathe link pou einai sto arxio links_html 
LIST_OF_DIATHESIMOTITA = []
for line in file: 
    ##print(line)
    driver.get(line)
    driver.implicitly_wait(5) ## to bazoume gia na perimeni ligo na fortosi ti kathe selida
    num_of_ratings = driver.find_element_by_class_name('pdp-stock__line')
    LIST_OF_DIATHESIMOTITA.append(num_of_ratings.text) ## to bazoume stin lista

##print("PRINT LIST OF NOT OBJ --> ")
##print(LIST_OF_DIATHESIMOTITA)

## DIMIOURGIA KLASIS GIA TIN DIATHESIMOTITA 
class Diathesimotita:
    def __init__(self, diathesimotita):
        self.diathesimotita = diathesimotita
    
LIST_OF_OBJ_DIATHESIMOTITA = [] ## LIST ANTIKIMENON DIATHESIMOTITA

for i in LIST_OF_DIATHESIMOTITA:
    LIST_OF_OBJ_DIATHESIMOTITA.append(Diathesimotita(i))

print("PRINT OF OBJ LIST --> ")
for obj in LIST_OF_OBJ_DIATHESIMOTITA: ## tiposi listas of obj 
    print(obj.diathesimotita, sep =' ')
