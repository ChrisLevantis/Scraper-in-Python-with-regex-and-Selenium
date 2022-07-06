## DONE
## Here we find the price (1 LEVEL)
## FILES THAT THIS SCRIPT USE ARE --> html_code_2.html //// prices.txt //// prices_final.txt
from base64 import encode
import re

## FIRST PROCESSING --> proscces the html code 
filename = "html_code_2.html"
infile = open(filename, 'r', encoding='utf-8')
lines = infile.readlines()

prices = re.findall('((class="price")(.*?)\d(</div>))', str(lines))
##print(prices[0])

file_prices = open("prices.txt", 'w', encoding='utf-8')

counter = 0 ## this just counts how much the regex has found
for price in prices:
    ##print(price[0])
    file_prices.write(price[0] + '\n') ## here we write the result of the final regex in the new file
    counter += 1
##print(counter)

file_prices.close()
infile.close()


## SECOND PROCCES --> now we gonna procces the file (file_prices) to get ONLY the prices
file_prices = open("prices.txt", 'r', encoding='utf-8')

file_prices_final = open("prices_final.txt", 'w', encoding='utf-8') ## the file that you gonna write only the prices
lines = file_prices.readlines()

for line in lines:
    final_prices = re.search("((\d)(.*?)[0-9](?=<))", line)
    ##print(final_prices.group(1))
    file_prices_final.write(str(final_prices.group(1)) + "\n")

file_prices_final.close()

FINAL_PRICES_list = [] ## LIST WIT THE FINAL RESULTS...
file_prices_final = open("prices_final.txt", 'r', encoding='utf-8')

data = file_prices_final.read()

FINAL_PRICES_list = data.split("\n")
##print(FINAL_PRICES_list)
file_prices_final.close()


## HERE WE CREATE A CLASS Title TO CREATE A LIST OF OBJECTS...
class Prices:
    def __init__(self, price):
        self.price = price

LIST_OF_OBJECTS_PRICES = []

## iterate apo to kathe stixio tis listas FINAL_PRICES_list (tin exo dimiourgisi pio pano)
for i in FINAL_PRICES_list:
    LIST_OF_OBJECTS_PRICES.append(Prices(i))

## tiposi tou kathe stixiou tis listas me ta object --> TO BAZO SE SXOLIO GIATI STO SCRIPTAKI POU KALO TIN get_price_list MOU TA TIPONI KAI DEN THELO
##for obj in LIST_OF_OBJECTS_PRICES:
    ##print(obj.price, sep =' ')

def get_price_list():
    return FINAL_PRICES_list

