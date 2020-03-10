# Load the Pandas libraries with alias 'pd' 
import math
import pandas as pd 
import ast

LABELS_COL=31 #Column number of the column with labels
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
data = pd.read_csv("PADCHEST_chest_x_ray_images_labels_160K_01.02.19.csv", low_memory=False)  #Read CSV

# Preview the first 5 lines of the loaded data 
#print(data.head())

#for col in data.columns:
col = data.columns[LABELS_COL] #Column with labels
series = data[col]
#for i in range(10):
#    print("Start patient")
#    print(series[i])
#    #for label in series[i].split(", "): #Not good enough
#    #for label in ast.literal_eval(series[i]): #Good results, we take those
#    #    print("----" + label)
#    print("End patient")

#Lets put a dictionary to extract the frequencies

label_freq = dict()
col = data.columns[LABELS_COL]
images_labels = data[col]
for image in images_labels:
    if isinstance(image, float) :
        #print("found nan")
        continue
    for label in ast.literal_eval(image):
        label = label.strip()
        if label in label_freq:
            label_freq[label] = label_freq[label]+1
        else:
            label_freq[label] = 1

ordered_list = list(sorted(label_freq.items(), key=lambda item: item[1], reverse=True))

for k, v in ordered_list:
    print(k + " : " + str(v))
