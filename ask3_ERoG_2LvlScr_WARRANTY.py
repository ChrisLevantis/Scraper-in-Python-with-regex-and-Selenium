## HERE WE DO SCRAP LEVEL 2 IN THE INFORMATION WARRANTY OF EACH PRODUCT...
from selenium import webdriver
from lib2to3.pgen2 import driver

driver = webdriver.Firefox(executable_path="C:\\Program Files\\geckodriver\\geckodriver.exe")

file = open('links_html.txt', 'r') ## ANIGOUME TO ARXIO POU EXOUME DIMIOURGISI APO TO MEROS A, TO OPOIO PERIEXI OLA TA LINK GIA TO KATHE PROION, TO XRISIMOPOIOUME KAI STO KATHENA ZAXNOUME GIA WARRANTY

LIST_WARRANTY = []
for line in file: 
    ##print(line)
    driver.get(line)
    driver.implicitly_wait(5) ## to bazoume gia na perimeni ligo na fortosi ti kathe selida
    num_of_ratings = driver.find_element_by_class_name('pdp-warranty')
    LIST_WARRANTY.append(num_of_ratings.text) ## to bazoume stin lista

##print(LIST_WARRANTY)

## DIMIOURGIA KLASIS GIA TO Warranty 
class Warranty:
    def __init__(self, warnt):
        self.warnt = warnt
    
LIST_OF_OBJ_WARRANTY = [] ## LIST ANTIKIMENON WARRANTY

for i in LIST_WARRANTY:
    LIST_OF_OBJ_WARRANTY.append(Warranty(i))

print("PRINT OF OBJ LIST --> ")
for obj in LIST_OF_OBJ_WARRANTY: ## tiposi listas of obj 
    print(obj.warnt, sep =' ')