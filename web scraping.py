import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.iplt20.com/auction/2022"
r = requests.get(url) #it give the total optput or responce
# print(r)

soup = BeautifulSoup(r.text,"lxml") # it give the total output as html code
#print(soup)

table = soup.find("table" , class_ ="ih-td-tab auction-tbl") #it gives the calling table-class data in html code
#print(table)
title = table.find_all("th") #it gives the all table-header or <th></th> data in html code and it extract from table
#print (title)

header = [] #it is a list that store data of 0-index that is only header

# here use for loop to exract header as text from html code
for i in title:
    name=i.text
    header.append(name)  
#print(header)

df = pd.DataFrame(columns=header) #it gives the output as table like excel sheet
#print(df)

rows = table.find_all("tr") #it gives the all table-row or <tr></tr> data in html code and it extract from table
#print(row)

#here use for loop to extarct data in the rows as text from html code
for i in rows[1:]: #here data extract from 1-index in rows , 0-index is the header
    first_td = i.find_all("td")[0].find("div", class_ = "ih-pt-ic").text.strip() #without this the logo come on output as /n . so this use to remove
    data = i.find_all("td")[1:]
    #print(data)
    
    row=[tr.text for tr in data] #it is the list that store data from 1-index in the row
    #print(row) 
    
    row.insert(0,first_td) #it insert in every row to remove /n
    #below 2 line help to data-frame to give output in a row and clearly
    l = len(df) 
    df.loc[l] = row
print(df) #it give the data in a data-frame

#collect all data and stored in excel sheet 
df.to_csv("ipl aucton stats.csv")
