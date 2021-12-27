import plotly.figure_factory as ff
import pandas as pd
import statistics
import random

np = input("whitch data you want(claps,reading_time): ")

df = pd.read_csv('medium_data.csv')
data = df[np].tolist()

def get_mean(counter):
    data_set=[]

    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value = data[random_index]
        data_set.append(value)

    mean = statistics.mean(data_set)

    return mean

def show_fig(mean_list):
    df=mean_list

    fig=ff.create_distplot([df],[np],show_hist=False)
    fig.show()     

def main():
    mean_list=[]
        
    for i in range(0,100):
        set_of_mean = get_mean(30)
        mean_list.append(set_of_mean)

    show_fig(mean_list)

main()
