# Import the rquired libaries
import requests
import pandas as pd
from bs4 import BeautifulSoup as BS


base_url = 'http://www.ngtradeonline.com/'
search_url = 'http://www.ngtradeonline.com/Home/PriceHistory?page=1&stockName=ACCESS'

#b_sup = []
#c_data = []

# defines a function  that loops through a web pages
def multi_P_Scrapper():
    # Get data from a specified webpage
    f_page = requests.get(search_url)
    #create a BeautifulSoup obejects
    sup = BS(f_page.content, parser='lxml', features= 'lxml')
    #print(sup)
   
    r_sup = []

    for items in sup.find_all('tr'):
        c_data = []
        for fig in items.find_all('td'):
            c_obj = fig.text
            c_data.append(c_obj.replace('\n', ''))
        r_sup.append(c_data)
    print(r_sup)
#def parse_to_DF()
    

print(multi_P_Scrapper())

