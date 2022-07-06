## DONE
## Here we find the title (1 LEVEL)
## FILES THAT THIS SCRIPT USE ARE --> html_code_2.html //// titles.txt //// titles_final.txt

from base64 import encode
import re
 
## FIRST PROCESSING --> proscces the html code
filename = "html_code_2.html"
infile = open(filename, 'r', encoding='utf-8')
lines = infile.readlines()

titles = re.findall('((<span class="product-title">)(.*?)(</span>))', str(lines))
##print(titles)

file_titles = open("titles.txt", 'w', encoding='utf-8')

counter = 0 ## this just counts how much the regex has found
for title in titles:
    ##print(title[0])
    file_titles.write(title[0] + '\n') ## here we write the result of the final regex in the new file
    counter += 1
    if counter == 12:
        break
##print(counter)

file_titles.close()
infile.close()

## SECOND PROCCES --> now we gonna procces the file (file_titles) to get ONLY the title
file_titles = open("titles.txt", 'r', encoding='utf-8')

titles_final = open("titles_final.txt", 'w', encoding='utf-8') ## the file that you gonna write only the titles
lines = file_titles.readlines()

for line in lines:
    final_titles = re.search("((Apple)(.*?)(?=</span>))", line)
    ##print(final_titles.group(1))
    titles_final.write(str(final_titles.group(1)) + "\n")

file_titles.close()

FINAL_TITLES_list = []  ## LIST WIT THE FINAL RESULTS...
titles_final = open("titles_final.txt", 'r', encoding='utf-8')

data = titles_final.read()

FINAL_TITLES_list = data.split("\n")
##print(FINAL_TITLES_list)
titles_final.close()


## HERE WE CREATE A CLASS Title TO CREATE A LIST OF OBJECTS...
class Titles:
    def __init__(self, title):
        self.title = title
    

LIST_OF_OBJECTS_TITLES = []

for i in range(12):
    LIST_OF_OBJECTS_TITLES.append(Titles(FINAL_TITLES_list[i]))

## tiposi ton antikimenon tis listas antikimenon --> TO BAZO SE SXOLIO GIATI STO SCRIPTAKI POU KALO TIN get_title_list MOU TA TIPONI KAI DEN THELO
##for obj in LIST_OF_OBJECTS_TITLES:
    ##print( obj.title, sep =' ' )

## kanoume return tin lista FINAL_TITLES_list gia to 2 erotima
def get_title_list():
    return FINAL_TITLES_list

