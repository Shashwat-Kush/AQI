import pandas as pd
import matplotlib.pyplot as plt


    
def avg_data_2013():
    temp_i =0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2013.csv',chunksize =24):
        add_var =0
        avg = 0.0
        data = []
        df = pd.DataFrame(rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) == float or type(i) == int:
                add_var += i
            elif type(i) == str:
                if i != 'NoData' and i!= 'PwrFail' and i!= '---' and i!= 'InVld':
                    temp = float(i)
                    add_var +=temp
        
        avg = add_var /24
        temp_i +=1
        average.append(avg)
    return average
    
def avg_data_2014():
    temp_i =0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2014.csv',chunksize =24):
        add_var =0
        avg = 0.0
        data = []
        df = pd.DataFrame(rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) == float or type(i) == int:
                add_var += i
            elif type(i) == str:
                if i != 'NoData' and i!= 'PwrFail' and i!= '---' and i!= 'InVld':
                    temp = float(i)
                    add_var +=temp
        avg = add_var /24
        temp_i +=1
        average.append(avg)
    return average
    
def avg_data_2015():
    temp_i =0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2015.csv',chunksize =24):
        add_var =0
        avg = 0.0
        data = []
        df = pd.DataFrame(rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) == float or type(i) == int:
                add_var += i
            elif type(i) == str:
                if i != 'NoData' and i!= 'PwrFail' and i!= '---' and i!= 'InVld':
                    temp = float(i)
                    add_var +=temp
        
        avg = add_var /24
        temp_i +=1
        average.append(avg)
    return average
    
def avg_data_2016():
    temp_i =0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2016.csv',chunksize =24):
        add_var =0
        avg = 0.0
        data = []
        df = pd.DataFrame(rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) == float or type(i) == int:
                add_var += i
            elif type(i) == str:
                if i != 'NoData' and i!= 'PwrFail' and i!= '---' and i!= 'InVld':
                    temp = float(i)
                    add_var +=temp
        
        avg = add_var /24
        temp_i +=1
        average.append(avg)
    return average
    
def avg_data_2017():
    temp_i =0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2017.csv',chunksize =24):
        add_var =0
        avg = 0.0
        data = []
        df = pd.DataFrame(rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) == float or type(i) == int:
                add_var += i
            elif type(i) == str:
                if i != 'NoData' and i!= 'PwrFail' and i!= '---' and i!= 'InVld':
                    temp = float(i)
                    add_var +=temp
        
        avg = add_var /24
        temp_i +=1
        average.append(avg)
    return average
    
def avg_data_2018():
    temp_i =0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2018.csv',chunksize =24):
        add_var =0
        avg = 0.0
        data = []
        df = pd.DataFrame(rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) == float or type(i) == int:
                add_var += i
            elif type(i) == str:
                if i != 'NoData' and i!= 'PwrFail' and i!= '---' and i!= 'InVld':
                    temp = float(i)
                    add_var +=temp
        
        avg = add_var /24
        temp_i +=1
        average.append(avg)
    return average
    
if __name__ == '__main__':
    list2013 = avg_data_2013()
    list2014 = avg_data_2014()
    list2015 = avg_data_2015()
    list2016 = avg_data_2016()
    list2017 = avg_data_2017()
    list2018 = avg_data_2018()
    #for i in list(list2013):
     #   print(i)
    print(len(list2013))
    plt.plot(range(0,len(list2013)),list2013)
    plt.plot(range(0,len(list2014)),list2014)
    plt.plot(range(0,len(list2015)),list2015)
    # plt.plot(range(0,len(list2016)),list2016)
    # plt.plot(range(0,len(list2017)),list2017)
    # plt.plot(range(0,len(list2018)),list2018)
    plt.show()