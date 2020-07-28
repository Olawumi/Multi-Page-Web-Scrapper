"""
The first step imports libararies need to perform the task efficiently
an empty list is created to serve as storage for the retrieved data
All could have been done using a for loop but for re-usability a fuction is used
""" 

import requests
import pandas as pd
from bs4 import BeautifulSoup as BS
import mysql.connector
from sqlalchemy import create_engine


###############################################################################################
####                        EXTRACT THE DATA                                               ####
###############################################################################################
#creates an empty list for storage later
all_data  = [] 
def m_webscrapper():
    #a range specify a start and stop point
    for fd in range(1,108):
        #the next step get the base url and stores it in search_url variable
        search_url = 'http://www.ngtradeonline.com/Home/PriceHistory?page='
        #the next step gets search_url and concatenate all other components to make it a functional webpage
        # it store process in a req variable
        req = requests.get(search_url + str(fd) + '&stockName=ACCESS')
        #BeautifulSoup is used to get the content in lxml

        sup = BS(req.content, parser='lxml', features= 'lxml')
        #print(sup)

        #a for loop nested in another for loop to get the required data
        for dat in sup.find_all('tr'):
            cell_dat = []
            #fdat loops through dat
            for fdat in dat.find_all('td'):
                #stores financial data in cell financial data(cell_fdat)
                cell_fdat = fdat.text
                #appends cell_fdat to cell data(cell_dat)
                cell_dat.append(cell_fdat.replace('\n', ''))
            #appends the cell data to the empty list created earlier
            all_data.append(cell_dat)
        #print(all_data)
    #creates a DataFrame for the table display
    multi_web_scrapper = pd.DataFrame(all_data[1:], columns=['Symbol', 'Low', 'Open', 'Price', 'Volume', 'High', 'Change', 'Date'])
    return multi_web_scrapper
    #multi_web_scrapper.to_csv('Multi-Page Web Scrapper.csv', index= False)


    ###############################################################################################
    ####                        DATA TRANSFORMATION                                            ####
    ###############################################################################################
    #multi_web_scrapper['High_low_value'] = multi_web_scrapper['High'].astype(int) * multi_web_scrapper['Low'].astype(int)



scrape_data = m_webscrapper()

    #print(multi_web_scrapper.head(30))
    #creates a csv file from the generated data
   

#calls the function

###############################################################################################
####                        LOADING DATA TO A DATABASE                                     ####
###############################################################################################



# Using SQLAlchemy
# Create a connection to our database

connection = mysql.connector.connect(host = 'localhost', user = 'root', password = 'root', database = 'ng_trade')

cur = connection.cursor()
connect_engine = create_engine('mysql://root:root@localhost/ng_trade')


 #Load data from pandas dataframe to sql
scrape_data.to_sql('trade_data', con = connect_engine, if_exists = 'append',  index = False)


"""
# Using mysql connector
connection = mysql.connector.connect(host = 'localhost', user = 'root', password = 'root', database = 'ng_trade')
cur = connection.cursor()
with open('Multi-Page Web Scrapper.csv', 'r') as data:
    next(data)
    cur.copy_from(data, trading_data, sep = ',')

"""


