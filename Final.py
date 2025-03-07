# -*- coding: utf-8 -*-
"""
@author: Amanda Rivera
Project: Data Organization and Visualization of patient cases concerning Diabetes
Last updated: 3/08/2025
Course: IVY TECH SDEV 220

Using Windows command prompt, the following was applied:
    pip install pandas
    pip install numpy
    pip install scikit-learn
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
data = pd.read_csv("Dataset_of_Diabetes.csv")

#len() function to show many samples (rows) are in the dataset
#print(len(data))

#.sum() after isna() outputs the number of empty cells
#print(data.isna().sum())

class DataProcessor:
    def __init__(self, data):
        if isinstance(data, pd.DataFrame):
            self.df = data
        else:
             try:
                self.df = pd.read_csv("Dataset_of_Diabetes.csv")
             except:
                raise ValueError("Invalid data type. Provide a Pandas DataFrame or a valid file path.")
                

class Patient:
    def __init__(self, gender, age, BMI):
        self.gender = gender
        self.age = age
        self.BMI = BMI

class Labs:
    def __init__(self, lab_tests):
        self.lab_tests = lab_tests
        
class LabResults(Labs):
    def __init__(self, lab_tests, Urea_res, Cr_res, HbA1c_res, Chol_res, 
                 TG_res, HDL_res,LDL_res, VLDL_res):
        super().__init__(lab_tests)
        self.Urea = Urea_res
        self.Cr = Cr_res
        self.HbA1c = HbA1c_res
        self.Chol = Chol_res
        self.TG = TG_res
        self.HDL = HDL_res
        self.LDL = LDL_res
        self.VLDL = VLDL_res
   

#Define the shortner name for the dataframe, df
df = data

#Module to modify dataset
def tableFormat():
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

#Diifferent Graph types containg relevant info between Class and specific lab tests
def allGraphs():
#Create an object containg variables to analyze
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

#plot.show(sns) #this displays the plots


#Module for the user to enter variables in order to visualize specific data in a graph
def creategraph(): 
        variables = ["Gender", 'AGE', "Urea", "Cr", "HbA1c", "Chol",
                          "TG", "HDL", "LDL", "VLDL", "BMI", "CLASS"]
        
        print("The avaialble variables for this dataset are:", variables)
        
        #Get data types from user;
        #One input for horizontal x-axis data
        #One input for vertical y-axisi data
        #Include loop to account for invalid user inputs
        while True:
            user_x = str(input("Enter a variable for the x-axis (000 to quit): "))
            if user_x in variables:     
                variables.remove(user_x) #remove user_x so that user cannot choose the same variable again
                break
            elif user_x == "000":
                break
            else:
                print( "Invalid input. Try again.") 
        while True:
            user_y = str(input("Enter a variable for the y-axis (000 to quit): "))
            if user_y in variables:
                break
            else:
                print("Invalid input. Try again.") 
                
                
        #Get graph type from user
        #exception handling to account for unavaiable graph types
        graphstypes = ["LINE", "HISTOGRAM", "JOINT SCATTER", "BOX PLOT"]
        
        while True:
            user_graph = input("Enter graph type (Line, Histogram, Joint Scatter, Box Plot): ")
            user_graph = user_graph.upper()
            
            if user_graph in graphstypes:
                
                if user_graph == "LINE":
                #Line graph
                    return sns.lineplot(data=df, 
                        x = user_x,
                        y = user_y,
                        )
                
                if user_graph == "HISTOGRAM":
                # Histogram
                    return sns.displot(data = df, 
                        x = user_x, 
                        y = user_y,
                        ) 
                
                if user_graph == "JOINT SCATTER":
                #JointScatter Graph
                    return sns.jointplot(
                        x= user_x,
                        y= user_y,
                        kind = "scatter",
                        data = df)
                
                if user_graph == "BOX PLOT":
                #Box Plot Graph
                    return sns.boxplot(data = df,
                        x = user_x,
                        y = user_y
                        )
            else:
                print("Graph type is unavailable.")
                
    
#Module option 1 ; user inputs a single data type to display
def displaycategory():
    variables = ["Gender", 'AGE', "Urea", "Cr", "HbA1c", "Chol",
                      "TG", "HDL", "LDL", "VLDL", "BMI", "CLASS"]
    print("The avaialble variables for this dataset are:", variables)
    
    #Get user input for which category to output
    #exception handling for invalid inputs
    #case sensitive :c
    while True:
        userSearch = str(input("Display which category (000 to exit): "))
        if userSearch in variables:     
            print("\nHere is the data for", userSearch,":\n", (df[userSearch]))
        elif userSearch == "000":
            break
        else:
            print( "Invalid input. Try again.")     
    

#Main module 
if __name__ == '__main__':
    tableFormat()
    df = data
    print("Welcome!")
    print(f"The data variables for this Diabetes Dataset are: \n{df.dtypes}")
   
#Starts off user in main menu; piick from 3 options of data visualization
#exception handling to account for invalid inputs      
while True:
    try:
        choice = int(input(""""What would you like to do? 
                 1. Filter by data type
                 2. Create graph
                 3. Show pre-existing graphs
                 Enter either 1 or 2 or 3 (000 to exit): """))
         #Op 2        
        if choice == 2:
            graph = creategraph()
            plot.show()
        #Op 1
        elif choice == 1:
            displaycategory()
        #op 3
        elif choice == 3:
            allGraphs()
            plot.show()            
        #QUIT
        elif choice == 000:
            print("Exiting.")
            break
        else: #account for other integers
            print("Invalid option. Exiting program.")
    except ValueError: #accounts for characters and strings
        print("This was not a valid input; please try again.")
    else:
        print(":3c")
        break

print("Program completed :D")
            