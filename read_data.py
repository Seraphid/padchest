# Load the Pandas libraries with alias 'pd' 
import math
import pandas as pd 
import ast
import matplotlib.pyplot as plt

LABELS_COL=31 #Column number of the column with labels
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
data = pd.read_csv("data/PADCHEST_chest_x_ray_images_labels_160K_01.02.19.csv", low_memory=False)  #Read CSV

#Lets put a dictionary to extract the frequencies

label_freq = dict()
col = data.columns[LABELS_COL]
images_labels = data[col]
for image in images_labels:
    if isinstance(image, float) : #Sometimes, instead of a list of labels this csv has NaN. We use this to get rid of that
        continue
    for label in ast.literal_eval(image):
        label = label.strip()
        if label == '':           #Sometimes, we have an empty list of labels, but this method returns an empty label, so we get rid of that
            continue
        if label in label_freq:
            label_freq[label] = label_freq[label]+1
        else:
            label_freq[label] = 1

ordered_list = list(sorted(label_freq.items(), key=lambda item: item[1], reverse=True))

for k, v in ordered_list:
    print(k + " : " + str(v))

labels, freqs = zip(*ordered_list)

plt.plot(range(1,len(freqs)+1), freqs)
plt.show()

plt.plot(range(10,len(freqs)+1), freqs[9:])
plt.show()

plt.plot(range(100,len(freqs)+1), freqs[99:])
plt.show()
