#importing pandas to aid in plotting our data
import pandas as pd
import os
#making targets in sequential data
SEQ_LEN = 60 #sequential length (using the last 60 munites of the data collected)
FUTURE_PERIOD_PREDICT = 5 #predicting 5 minutes ahead
RATIO_TO_PREDICT = "" #one of the inputs in line 13

#creating targets
def classify(current,future):
    if float(future) > float(current):
        return 1
    else:
        return 0
#i wanna train the network based that 1 is good


df = pd.read_csv("",names = ["",""]) 
#include the name of the path of the csv file (best if its in same folder)
#also include the names of targeted scopes ("time", "low","high","open","close")
main_df = pd.Dataframe() # a pandas' function 
ratios = ["",""]#btc-kes, ltc-kes, eth-kes
#include the names of csv file targeted titles
for ratio in ratios:
    #using an f string
    dataset = f"path{ratio}.csv" #ref sentdex sep 15 2018
    # to read into the datasets and what is in them
    df = pd.read_csv(dataset, names=["",""]) #delete line 4
    #renaming columns using pandas
    df.rename(columns={"oldname": f"{ratio}_name","anothername": f"{ratio}_name2"}, inplace=True)
    #setting the index
    df.set_index("", inplace=True)
    #to specicy that the dataframe is the specific two columns in line 16
    df = df[[f"{ratio}_name",f"{ratio}_name2" ]]
    # to merge all collumns together
    if len(main_df) == 0:
        main_df =df   
    else:
        main_df =main_df.join(df)#.join function #yk where name came from
main_df['future'] = main_df[f"{RATIO_TO_PREDICT}_name"].shift(-FUTURE_PERIOD_PREDICT)
#making predictions based on past data

#mapping the functions to a new column called target
main_df['target'] = list(map(classify, main_df[f"{RATIO_TO_PREDICT}_name"], main_df["future"]))
print (main_df[[f"{RATIO_TO_PREDICT}_name", "future", "target"]].head())
