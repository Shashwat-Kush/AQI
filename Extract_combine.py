from AQI import avg_data_2013, avg_data_2014, avg_data_2015, avg_data_2016,avg_data_2017,avg_data_2018
import requests
import sys
import os
import csv
import pandas as pd
from bs4 import BeautifulSoup

                                                                                                    
def met_data(month, year):                                                                           #It scraps the required data from the webpage

    file_html = open('Data/Html_Data/{}/{}.html'.format(year, month),'rb')
    plain_text = file_html.read()                                                                    #plain_text contains all the content that is there in the html file

    tempd = []
    finald = []

    #initialize the beautiful soup
    soup = BeautifulSoup(plain_text,'lxml')
    for table in soup.findAll('table',{'class':'medias mensuales numspan'}):                        #Finding the table
        for tbody in table:                                                                         #Finding the body of table 
            for tr in tbody:                                                                        #Finding the table row in body
                a = tr.get_text()
                # sprint(a)                                                                         #Getting the txt from the row
                tempd.append(a)
    print('{}: '.format(year)+' '+str(len(tempd)))
    rows = len(tempd) / 15
    
    for times in range(round(rows)):
        newtempd= []
        for i in range(15):
            newtempd.append(tempd[0])
            tempd.pop(0)
        finald.append(newtempd)

    length = len(finald)
    
    finald.pop(length-1)
    finald.pop(0)

    for i in range(len(finald)):                                                                    #Removing the columns which are not in use or have no value
        finald[i].pop(6)
        finald[i].pop(13)
        finald[i].pop(12)
        finald[i].pop(11)
        finald[i].pop(10)
        finald[i].pop(9)
        finald[i].pop(4)
        finald[i].pop(0)
    
    return finald


def data_combine(year , cs):                                                                        #We take the csv file, convert it into a dataframe and then into a list
    for i in pd.read_csv('Data/Real_Data/real_' + str(year)+ '.csv',chunksize=cs):
        df = pd.DataFrame(data=i)
        mylist = df.values.tolist()
    return mylist

if __name__ == '__main__':
    if not  os.path.exists('Data/Real_Data'):                                                       #Make the real data folder
        os.makedirs('Data/Real_Data')
    for year in range(2013,2019):
        final_data =[]
        with open('Data/Real_Data/real_' +str(year)+ '.csv','w') as csvfile:                        #create a new csv file with the looks of excel
            wr = csv.writer(csvfile, dialect='excel')
            wr.writerow(['T', 'TM', 'Tm', 'H', 'VV', 'V', 'VM', 'PM 2.5'])                          #Add the top row to the data
        for month in range(1,13):
            temp = met_data(month,year)
            final_data = final_data + temp

        pm = getattr(sys.modules[__name__], 'avg_data_{}'.format(year))()                           #fetch the avg pm2.5 value by fetching the value for each year

        if len(pm) == 364:                                                                          #If by mistake, any year has 364 entries, then it makes it 365 entries
            pm.insert(364,'-')

        for i in range(len(final_data)-1):                    
            final_data[i].insert(7,pm[i])                                                           #adding the pm2.5 value for each year
        
        with open('Data/Real_Data/real_' +str(year)+ '.csv','a') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            for row in final_data:
                flag=0
                for element in row:
                    if element == '' or element == '-':
                        flag=1
                if flag !=1 :
                    wr.writerow(row)

    data_2013 = data_combine(2013, 600)                                                             #calling the function to conert the year data into list
    data_2014 = data_combine(2014, 600)
    data_2015 = data_combine(2015, 600)
    data_2016 = data_combine(2016, 600)
    data_2017 = data_combine(2017, 600)
    data_2018 = data_combine(2018, 600)

    total=data_2013+data_2014+data_2015+data_2016+ data_2017+ data_2018                             #Combining all the years' data together
    
    with open('Data/Real_Data/Real_Combine.csv', 'w') as csvfile:                                   #creating a separate csv file with all the combined data
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(
            ['T', 'TM', 'Tm', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(total)




