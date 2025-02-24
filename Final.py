# -*- coding: utf-8 -*-
"""
@author: AmaRi

Using Windows command prompt, the following was applied:
    pip install pandas
    pip install numpy
    pip install matplotlib
    pip install seaborn
"""
import pandas as pd
import numpy as np
from sklearn import datasets
import matplotlib
import matplotlib.pyplot as plot
import seaborn as sns

#read csv files
data = pd.read_csv(r"C:\Users\AmaRi\SDEVFINAL\Diabetes Dataset\Dataset of Diabetes .csv")

#len() function to show many samples (rows) are in the dataset
print(len(data))

#.sum() after isna() outputs the number of empty cells
print(data.isna().sum())

#Define the shortner name for the dataframe, df
df = data
#remove unwanted columns
df = df.drop(['ID', 'No_Pation'], axis = 1)
df = df[df["CLASS"].str.contains("P") == False] #"P" represented predicted diabetes cases; we don't want to count these under real cases

#Group by gender;  transpose to have a prettier table
df = df.replace('f','F', regex = True) #Fix 'F' and 'f' into same category
dtable1 = df.groupby(['Gender']).describe()
dtable1 = dtable1.transpose() 
#Group by class and see if there are any invalid classes in CLASS
df["CLASS"] = df["CLASS"].str.strip() #Fix invalid spaces
dtable2 = df.groupby(["CLASS"]).describe()
dtable2 = dtable2.transpose()

table_final = df.groupby(["Gender", "CLASS"]).describe()
table_final = table_final.transpose()

#Create an object containg 4 variables to analyze
variables = ["TG", "LDL", "HDL", "HbA1c"]
#Evaluate distributiion plot for HbA1c Controls and Diabetes
sns.displot(data=df[variables], x = "HbA1c", hue = df["CLASS"], kind = "kde") #this creates the plot for HgbA1c
sns.displot(data = df[variables], x = "TG", hue = df["CLASS"], kind = "kde") #creates plot for TG
sns.displot(data = df[variables], x = "LDL", hue = df["CLASS"], kind = "kde") #creates plot for LDL
sns.displot(data = df[variables], x = "HDL", hue = df["CLASS"], kind = "kde") #creates plot for HDL

sns.displot(data = df[variables], x = "HbA1c", hue = df["CLASS"],
    multiple = "stack") #creates the histogram for HgbA1c
sns.displot(data = df[variables], x = "TG", hue = df["CLASS"],
    multiple = "stack") #creates the histogram for TG
sns.displot(data = df[variables], x = "LDL", hue = df["CLASS"],
    multiple = "stack") #creates the histogram for LDL
sns.displot(data = df[variables], x = "HDL", hue = df["CLASS"],
    multiple = "stack") #creates the histogram for HDL

#Scatterplot, BUT I CANT GET IT TO LOOK RIGHT
sns.scatterplot(data = df,
                x= "BMI",
                y= "HbA1c",
                hue= "CLASS")

#Make the jointplot visualization and separate scatter points by class
sns.jointplot(x=df["BMI"], y= df["HbA1c"], hue=df["CLASS"])

#Make boxplot of HbA1C versus CLASS
sns.boxplot(x = df["Gender"], y = df["HbA1c"], hue = df["CLASS"])

plot.show(sns) #this displays the plots