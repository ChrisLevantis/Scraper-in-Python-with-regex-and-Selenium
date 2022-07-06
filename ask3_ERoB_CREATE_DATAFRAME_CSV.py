## HERE WE CREATE THE DATAFRAME AND WE CREATE THE CSV FILE
import ask3_ERoA_titles_1scrap
import ask3_ERoA_prices_1scrap
import ask3_ERoA_kodikosPlaisiou_1scrap
import ask3_ERoA_2downloadHTML_CODE_OF_LINKS

import pandas as pd
import random
import uuid

mydataset = {}

## SCRAP 1
list_titles = []
list_titles = ask3_ERoA_titles_1scrap.get_title_list() ## we call get_title_list from file ask3_ERoA_titles_1scrap to get all the titles of the MacBooks
## SCRAP 1
list_prices = []
list_prices = ask3_ERoA_prices_1scrap.get_price_list() ## we call ask3_ERoA_prices_1scrap from the file ask3_ERoA_prices_1scrap to get all the prices of the MacBooks
## SCRAP 1
kodikes_plaisiou_list = []
kodikes_plaisiou_list = ask3_ERoA_kodikosPlaisiou_1scrap.get_kodikos_plaisiou_list() ## we call get_kodikos_plaisiou_list from the file ask3_ERoA_kodikosPlaisiou_1scrap to get all the prices of the MacBooks
## SCRAP 2
list_rams = []
prosorino = []
prosorino = ask3_ERoA_2downloadHTML_CODE_OF_LINKS.get_kodikos_plaisiou_list()
list_rams = prosorino[0]
list_rams.append(prosorino[1][0] + prosorino[1][1])    ## --> ZERO OTI AUTOS O TROPOS DEN EINAI KOMZOS ALLA ENTAZI, O LOGOS POU EGINE EINAI GIATI TO LIST POU "ERXETAI" APO TO ALLO FILE EINAI ETSI ## NOW WE HAVE TO CONVERT THE LIST TO A MOST NICE LIST...
list_rams.extend(prosorino[2])                         ## [['8'], ['1', '6'], ['8'], ['8'], ['8'], ['1', '6'], ['8'], ['8'], ['8'], ['8'], ['1', '6'], ['3', '2']] KAI GO THELO NA TO KANI ETSI 
list_rams.extend(prosorino[3])                         ## ['8', '16', '8', '8', '8', '16', '8', '8', '8', '8', '16', '32'] 
list_rams.extend(prosorino[4])
list_rams.append(prosorino[5][0] + prosorino[5][1])
list_rams.extend(prosorino[6])
list_rams.extend(prosorino[7])
list_rams.extend(prosorino[8])
list_rams.extend(prosorino[9])
list_rams.append(prosorino[10][0] + prosorino[10][1])
list_rams.append(prosorino[11][0] + prosorino[11][1])
##print(list_rams)




mydataset = {
    'ID': [i for i in range(12)], ## UNIQUE INTENTIFIER
    'Title': [list_titles[0], list_titles[1], list_titles[2], list_titles[3], list_titles[4], list_titles[5], list_titles[6], list_titles[7], list_titles[8], list_titles[9], list_titles[10], list_titles[11]],
    'Price': [list_prices[0], list_prices[1], list_prices[2], list_prices[3], list_prices[4], list_prices[5], list_prices[6], list_prices[7], list_prices[8], list_prices[9], list_prices[10], list_prices[11]],
    'Kodikos Plaisio': [kodikes_plaisiou_list[0], kodikes_plaisiou_list[1], kodikes_plaisiou_list[2], kodikes_plaisiou_list[3], kodikes_plaisiou_list[4], kodikes_plaisiou_list[5], kodikes_plaisiou_list[6], kodikes_plaisiou_list[7], kodikes_plaisiou_list[8], kodikes_plaisiou_list[9], kodikes_plaisiou_list[10], kodikes_plaisiou_list[11]],
    'RAM': [list_rams[0], list_rams[1], list_rams[2], list_rams[3], list_rams[4], list_rams[5], list_rams[6], list_rams[7], list_rams[8], list_rams[9], list_rams[10], list_rams[11]]
}

dataframe = pd.DataFrame(mydataset)
##print(dataframe.to_string(index=False)) 
dataframe.to_csv('DATA_CSV.csv', index=False)


