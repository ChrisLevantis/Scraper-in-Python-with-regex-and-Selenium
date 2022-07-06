## FINAL SCRIPT, HERE WE DOWNLOAD THE HTML CODES OF EACH PRODUCT AND WE THE CORECT REGEX WE SCRAP FOR THE INFORMATION WE NEED...  
## THE INFORMATION THAT WE GONNA FIND IS THE RAM OF EACH PRODUCT...
import urllib.request
import requests
import re

##### METATREPOUME OLA TA LINS (POU EINAI MISA) SE OLOKLIROMENA LINKS KAI
##### HERE WE PROCESS ALL THE LINKS, SO THEY CAN B IN THE CORREECT FROM, WE ADD IN THE START OF EACH LINK THE STRING --> --  https://www.plaisio.gr/  --
##### WE PUT THEM IN A NEW FILE links_html.html WE IS TYPE html...
FILE_LINKS_SCRAP_LVL_2_FINAL = open('FILE_LINKS_SCRAP_LVL_2_FINAL.txt', 'r', encoding='utf-8')
string_to_add = "https://www.plaisio.gr/"

lines = FILE_LINKS_SCRAP_LVL_2_FINAL.readlines()

links_html = open('links_html.html', 'w', encoding='utf-8')
for line in lines:
    links_html.write(string_to_add + str(line))

links_html.close()
FILE_LINKS_SCRAP_LVL_2_FINAL.close()


##### NOW WE TRY TO MAKE A REQUEST IN EACH LINK...
links_list = []
links_html_2 = open('links_html.html', 'r')
data = links_html_2.read()

links_list = data.split("\n") ## the split here we use it only beacause if you read from a file and put it a list, the items in the list will have in the end the newline symbol, and then the request doesent work...
##print(links_list)

## (SECOND LEVEL SCRAP) --> FOR THE LINKS, WE WILL FIND THE RAM ///
RAMS = [] ## list for RAMS 
RAMS_PROSORINO = [] ## IT IS JUST FOR HELP

## LOOP 12 TIMES BEACAUSE THE LINKS ARE 12, SO THE CLICK WE WILL DO THEORICALLY ARE 12, FOR EACH PRODUCT...
for i in range(12):
    RAMS_PROSORINO = []  ## EMPTY THE LIST, THIS LIST IS JUST FOR HELP...
    file_htmls_codes = open('htmls_codes.html', 'w', encoding='utf-8')  ## here we gonna write the html code for each product, each time we make the theorycall click... 
    html_1 = requests.get(links_list[i])  ## we make the request (the links are in the list links_lists)
    file_htmls_codes.write(html_1.text)  ## write the code in the file htmls_codes.html
    file_htmls_codes.close()
    ## REGEX FOR RAM // 2 LINK
    file_htmls_codes = open('htmls_codes.html', 'r', encoding='utf-8')
    lines = file_htmls_codes.readlines()
    RAMS_PROSORINO = re.findall('((<dt>Μέγεθος Μνήμης)(.*?)(</dd>))', str(lines)) ## we put the regex in the file to find ram (PUT IT WILL NEED A SECOND PROCCESS)
    ##print(RAMS_PROSORINO[0][0])

    PROSORINO_FILE = open('prosorino_file.txt', 'w', encoding='utf-8') ## in this file, the proccess it will done each time (here we write what we find from the up regex)
    PROSORINO_FILE.write(str(RAMS_PROSORINO[0][0])) 
    PROSORINO_FILE.close()

    PROSORINO_FILE = open('prosorino_file.txt', 'r', encoding='utf-8')
    lines = PROSORINO_FILE.readlines()
    RAMS.append(re.findall('\d', str(lines))) ## regex apla gia na bris ton teliko arithmo MONO TOU ## regex to just find the number only
    ## print(RAMS) ## EDO TO LIST ME TA RAMS THA EXI ENA STIXIO ME TIMI 8 /// morfi pou exi to list mexri edo einai ['8', ['1', '6']]... 
    file_htmls_codes.close()

##print("TELIKO LIST ME TA TELIKA RAMS --> ")
##print(RAMS)


## FTIAXNO MIA KLASI, GIA NA TO KANO LISTA ME ANTIKIMENA...
class Rams:
    def __init__(self, ram):
        self.ram = ram

LIST_OF_OBJECTS_OF_RAMS = [] ## LIST ME OBJECTS RAMS

for i in RAMS:
    LIST_OF_OBJECTS_OF_RAMS.append(Rams(i))

##for obj in LIST_OF_OBJECTS_OF_RAMS: --> TO BAZO SE SXOLIO GIATI STO SCRIPTAKI POU KALO TIN get_kodikos_plaisiou_list MOU TA TIPONI KAI DEN THELO 
    ##print(obj.ram, sep=' ')

def get_kodikos_plaisiou_list():
    return RAMS






