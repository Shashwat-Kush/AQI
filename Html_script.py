import os
import time
import requests #help us download that particular page in form of html
import sys # system argument



def retrieve_html():
    for year in range(2013,2019):
        for month in range(1,13):
            if month<10:
                url = 'https://en.tutiempo.net/climate/0{}-{}/ws-432950.html'.format(month,year)  #creating a dynamic url to visit through every webpage containg AQI information
            else:
                url = 'https://en.tutiempo.net/climate/{}-{}/ws-432950.html'.format(month,year)
        
            texts = requests.get(url) #download the  html file
            text_utf = texts.text.encode('utf-8') #encoding is done because there would be some unknown characters in the html file 

    #CREATING THE FOLDER STRUCTURE FOR THE HTML FILES        
            
            if not os.path.exists('Data/Html_Data/{}'.format(year)):                      #Checks whether there is a a folder with the given name
                os.makedirs('Data/Html_Data/{}'.format(year))                              #If not...make it
            with open('Data/Html_Data/{}/{}.html'.format(year,month),"wb") as output:     #creates the html file
                output.write(text_utf)                                                      #writes the html code in thst output file

        sys.stdout.flush()

if __name__ == '__main__':
    start_time = time.time()
    retrieve_html()
    stop_time = time.time()
    print('Time taken is {}'.format(stop_time - start_time))


        
        