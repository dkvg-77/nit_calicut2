import os
import feature_module as ft
import nltk
#nltk.download()
folderpath = str(os.getcwd())

file1 = open(folderpath + '/parameter/initial_filename.txt','r')
filename = file1.read().split("\n")

#print(filename)

print("Processing:",filename[0])
initial_filename = filename[0]
ft.feature_extract(initial_filename)


#print("Processing:",filename[1])
#initial_filename=filename[1]
#ft.feature_extract(initial_filename)

#print("Processing:",filename[2])
#initial_filename=filename[2]
#ft.feature_extract(initial_filename)

print("processing completed.....")

