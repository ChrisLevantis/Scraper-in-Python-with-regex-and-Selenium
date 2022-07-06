## DONE
## Here we find the kodikosPlaisiou (1 LEVEL)
## FILES THAT THIS SCRIPT USE ARE --> html_code_2.html //// kodikes_Plaisiou.txt //// kodikes_Plaisiou_final.txt
from base64 import encode
import re

## FIRST PROCESSING --> proscces the html code
filename = "html_code_2.html"
infile = open(filename, 'r', encoding='utf-8')
lines = infile.readlines()

kodikes_Plaisiou = re.findall('((class="sku")(.*?)\d(</span>))', str(lines))
##print(kodikes_Plaisiou)

file_kodikes_Plaisiou = open("kodikes_Plaisiou.txt", 'w', encoding='utf-8')

counter = 0 ## this just counts how much the regex has found
for kodika_Plaisiou in kodikes_Plaisiou:
    ##print(kodika_Plaisiou[0])
    file_kodikes_Plaisiou.write(kodika_Plaisiou[0] + '\n') ## here we write the result of the final regex in the new file
    counter += 1
##print(counter)

file_kodikes_Plaisiou.close()
infile.close()

## SECOND PROCCES --> now we gonna procces the file (file_titles) to get ONLY the kodikes Plaisiou
file_kodikes_Plaisiou = open("kodikes_Plaisiou.txt", 'r', encoding='utf-8')

kodikes_Plaisiou_final = open("kodikes_Plaisiou_final.txt", 'w', encoding='utf-8') ## the file that you gonna write only the kodikes Plaisiou
lines = file_kodikes_Plaisiou.readlines()

for line in lines:
    final_kodikes_Plaisiou = re.search("((\d)(.*?)[0-9](?=<))", line)
    ##print(final_kodikes_Plaisiou.group(1))
    kodikes_Plaisiou_final.write(str(final_kodikes_Plaisiou.group(1)) + "\n")

file_kodikes_Plaisiou.close()

FINAL_KODIKES_PLAISIOU_list = [] ## LIST WIT THE FINAL RESULTS...
kodikes_Plaisiou_final = open("kodikes_Plaisiou_final.txt", 'r', encoding='utf-8')

data = kodikes_Plaisiou_final.read()

FINAL_KODIKES_PLAISIOU_list = data.split("\n")
##print(FINAL_KODIKES_PLAISIOU_list)
kodikes_Plaisiou_final.close()

## HERE WE CREATE A CLASS Title TO CREATE A LIST OF OBJECTS...
class KodikosPlaisiou:
    def __init__(self, kodikos_plaisiou):
        self.kodikos_plaisiou = kodikos_plaisiou

LIST_OF_OBJECTS_KODIKOI_PLAISIOU = []

## iterate apo to kathe stixio tis listas FINAL_KODIKES_PLAISIOU_list (tin exo dimiourgisi pio pano)
for i in FINAL_KODIKES_PLAISIOU_list:
    LIST_OF_OBJECTS_KODIKOI_PLAISIOU.append(KodikosPlaisiou(i))

## tiposi tou kathe stixiou tis listas me ta object --> TO BAZO SE SXOLIO GIATI STO SCRIPTAKI POU KALO TIN get_kodikos_plaisiou_list MOU TA TIPONI KAI DEN THELO
##for obj in LIST_OF_OBJECTS_KODIKOI_PLAISIOU:
    ##print(obj.kodikos_plaisiou, sep =' ')

def get_kodikos_plaisiou_list():
    return FINAL_KODIKES_PLAISIOU_list
