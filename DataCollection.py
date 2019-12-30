# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 16:57:00 2019
@author: PSK
"""
import os
import time
import requests
import sys

def get_Html():
    for year in range(2013,2019):
        for month in range(1,13):
            if(month < 10):
                #the Zero is appended to accomodate first 9 months
                url = 'http://en.tutiempo.net/climate/0{}-{}/ws-421820.html'.format(month,year)
                    
            else:
                url = 'http://en.tutiempo.net/climate/{}-{}/ws-421820.html'.format(month,year)
            #getting the pages monthwise    
            source_text = requests.get(url)
            text_utf = source_text.text.encode('utf=8')
            
            if not os.path.exists("DataCollection/Html_Data/{}".format(year)):
                os.makedirs("DataCollection/Html_Data/{}".format(year))
            with open("DataCollection/Html_Data/{}/{}.html".format(year,month),"wb") as output:
                output.write(text_utf)
            #it will write everything in the buffer to the terminal, even if normally it would wait before doing so    
            sys.stdout.flush()
            
if __name__=="__main__":
    start_time=time.time()
    get_Html()
    stop_time=time.time()
    print("Time taken {}".format(stop_time-start_time))