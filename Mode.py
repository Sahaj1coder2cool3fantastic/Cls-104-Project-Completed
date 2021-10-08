from collections import Counter
import csv

with open('SOCR-HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
    n_num= file_data[i][1]
    new_data.append((n_num))
data = Counter(new_data)
mode_data_for_range = {"80-90":0, "90-100":0, "100-110":0}
for height,occurance in data.items():
    if 80<float(height)<90:
        mode_data_for_range["80-90"]=mode_data_for_range["80-90"] + occurence
    elif 90<float(height)<100:
        mode_data_for_range["90-100"]=mode_data_for_range["90-100"] + occurence
    elif 100<float(height)<110:
        mode_data_for_range["100-110"]=mode_data_for_range["100-110"] + occurence
