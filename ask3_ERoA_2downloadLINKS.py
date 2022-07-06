## Here we take only the links of the html_code_2.html
## FILES THAT WE USE --> html_code_2.html //// FILE_LINKS_SCRAP_LVL_2.txt ///// FILE_LINKS_SCRAP_LVL_2_FINAL.txt
## SCRAP LEVEL 2
from base64 import encode
import re

## FIRST PROCESS --> WE WILL TRY TO TAKE ONLY THE LINKS OF EACH PRODUCT...
filename = "html_code_2.html"
infile = open(filename, 'r', encoding='utf-8')
lines = infile.readlines()

links = re.findall('((<span class="product-title">)(.*?)(?=">))', str(lines))

FILE_LINKS_SCRAP_LVL_2 = open("FILE_LINKS_SCRAP_LVL_2.txt", 'w', encoding='utf-8')

counter = 0 ## this just counts how much the regex has found
for link in links:
    ##print(price[0])
    FILE_LINKS_SCRAP_LVL_2.write(link[0] + '\n') ## here we write the result of the final regex in the new file
    counter += 1
    if counter == 12:
        break
print(counter)

FILE_LINKS_SCRAP_LVL_2.close()
infile.close()

## SECOND PROCCESS --> now we gonna take only the link of each MacBook, so in the future we make a request in each of them
FILE_LINKS_SCRAP_LVL_2 = open("FILE_LINKS_SCRAP_LVL_2.txt", 'r', encoding='utf-8')

FILE_LINKS_SCRAP_LVL_2_FINAL = open("FILE_LINKS_SCRAP_LVL_2_FINAL.txt", 'w', encoding='utf-8')  ## the file that we gonna write only the links...
lines = FILE_LINKS_SCRAP_LVL_2.readlines()

for line in lines:
    final_links = re.search("((.pc-)(.*?).*)", line)
    ##print(final_prices.group(1))
    FILE_LINKS_SCRAP_LVL_2_FINAL.write(str(final_links.group(1)) + "\n")

FILE_LINKS_SCRAP_LVL_2_FINAL.close()

## FINALY THE LINKS THAT WE SCRAP AND PUT THEM IN THE FILE --FILE_LINKS_SCRAP_LVL2_FINAL-- ARE NOT IN THE CORECT FORM, SO THEY NEED A EXTRA PROCESS... --> IN THE NEXT SCRIPT WE GONNA FIX THEM... (in the script ask3_ERoA_2downloadHTML_CODE_OF_LINKS)

