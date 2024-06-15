
import os
import pandas as pd
import R_Value_Module as rvm
folderpath = str(os.getcwd())

file1 = open(folderpath + '/parameter/initial_filename.txt','r')
filename = file1.read().split("\n")
initial_filename=filename[0]
#test_filename=filename[1]

testing = folderpath + "/output_csv/" +"test_30_train.csv"
#testing = folderpath + "/output_csv/" + "/test_sst.csv"
test = pd.read_csv(testing)

training = folderpath + "/output_csv/" +"train_70_train.csv"
#training= folderpath + "/output_csv/" + "/train_sst.csv"
train = pd.read_csv(training)

test_id = []
train_id = []
train_lsdv = []
test_lsdv = []
train_rsdv = []
test_rsdv = []

# extracting all LSDV (Signal Distance Vector= MCL-location - SLV location)values from test and train datatset.
for index,row in train.iterrows():
    
    row = row.values.tolist()
    #print("row: ",row)
    #idx.append(row[0])
    #print(row)
    row[10] = str(row[10]).replace(" ","")   
    row[10] = row[10].replace("],","]")
    row[10] = row[10][1:len(row[10])-1]
    #print("row[9]: ",row[9])
    lis = []
    num = ""
    for ch in row[10]:
        if ch == "[":
            lis2 = []
        elif ch == "]":
            if num == "":
                lis.append(lis2)
            else:
                lis2.append(int(num))
                num = ""
                lis.append(lis2)
        elif ch ==" ":
            continue
        elif ch == ",":
            lis2.append(int(num))
            num = ""
        else:
            num += ch
    if(len(lis)!=1):
        lis = [ele for ele in lis if ele != []]
    #print("list_trainsdv:",lis)
    train_lsdv.append(lis)
    #print("train_lsdv:",train_lsdv)
    #break
#%%    
for index,row in train.iterrows():
    
    row = row.values.tolist()
    #print("row: ",row)
    #idx.append(row[0])
    row[11] = str(row[11]).replace(" ","")
    row[11] = row[11].replace("],","]")
    row[11] = row[11][1:len(row[11])-1]
    #print("row[9]: ",row[9])
    lis = []
    num = ""
    for ch in row[11]:
        if ch == "[":
            lis2 = []
        elif ch == "]":
            if num == "":
                lis.append(lis2)
            else:
                lis2.append(int(num))
                num = ""
                lis.append(lis2)
        elif ch ==" ":
            continue
        elif ch == ",":
            lis2.append(int(num))
            num = ""
        else:
            num += ch
    if(len(lis)!=1):
        lis = [ele for ele in lis if ele != []]
    #print("list_trainsdv:",lis)
    train_rsdv.append(lis)
    #print("train_rsdv:",train_rsdv)
    #break
#%%  
for index,row in test.iterrows():
    row = row.values.tolist()
    #idx.append(row[0])
    row[10] = str(row[10]).replace(" ","")
    row[10] = row[10].replace("],","]")
    row[10] = row[10][1:len(row[10])-1]
    lis = []
    num = ""
    for ch in row[10]:
        if ch == "[":
            lis2 = []
        elif ch == "]":
            if num == "":
                lis.append(lis2)
            else:
                lis2.append(int(num))
                num = ""
                lis.append(lis2)
        elif ch ==" ":
            continue
        elif ch == ",":
            lis2.append(int(num))
            num = ""
        else:
            num += ch
    if(len(lis)!=1):
        lis = [ele for ele in lis if ele != []]
    test_lsdv.append(lis)


for index,row in test.iterrows():
    row = row.values.tolist()
    #idx.append(row[0])
    row[11] = str(row[11]).replace(" ","")
    row[11] = row[11].replace("],","]")
    row[11] = row[11][1:len(row[11])-1]
    lis = []
    num = ""
    for ch in row[11]:
        if ch == "[":
            lis2 = []
        elif ch == "]":
            if num == "":
                lis.append(lis2)
            else:
                lis2.append(int(num))
                num = ""
                lis.append(lis2)
        elif ch ==" ":
            continue
        elif ch == ",":
            lis2.append(int(num))
            num = ""
        else:
            num += ch
    if(len(lis)!=1):
        lis = [ele for ele in lis if ele != []]
    test_rsdv.append(lis)
    
    
#%%
#print("hi calculating .......")
#print("train_sdv: ",train_sdv)
#temp=sdvsim.similarity(test_sdv,train_sdv)
#print("OKKKKKK")
test_data = []
train_data = []
           
for index,row in train.iterrows():
    row = row.values.tolist()
    train_id.append(row[0])
    train_data.append(row)
    
for index,row in test.iterrows():
    row = row.values.tolist()
    test_id.append(row[0])
    test_data.append(row) 

#print('len(test_id)=', len(test_id))
final=[]
for ab in range(len(test_id)):
#for ab in range(1): 
    testname = str(test_id[ab])
    print("test id:",ab)
    train_final = []
    #train_final.append(testname) 
    for index,row in train.iterrows():
        row = row.values.tolist()
        test_lsdv1 = test_lsdv[ab]           # SDV values ab=2000
        train_lsdv1 = train_lsdv[index]
        test_rsdv1 = test_rsdv[ab]           # SDV values ab=2000
        train_rsdv1 = train_rsdv[index]
        #print("\n\ntest id:",ab,"train id",row[0])
        
        #print("test_lsdv:",test_lsdv1,"\ntrain_lsdv:",train_lsdv1)
        #print("Lengths are:",len(test_lsdv1), len(train_lsdv1))
        msp1,mmc1 = rvm.fun(test_lsdv1,train_lsdv1)
        #print("msp1=",msp1,"mmc1=",mmc1)
              
        #print("\ntest_rsdv:",test_rsdv1,"\ntrain_rsdv:",train_rsdv1)        
        #print("Lengths are:",len(test_rsdv1),len(train_rsdv1))
        msp2,mmc2 = rvm.fun(test_rsdv1,train_rsdv1)
        #print("msp2=",msp2,"mmc2=",mmc2)
        
        msp=msp1+msp2
        mmc=mmc1+mmc2
        #print("\nmsp=",msp,"mmc=",mmc)
        r_value=rvm.find_rvalue(msp,mmc)
        #print("R=",r_value)
        #row += [str(r_value)]
        train_final.append(r_value)  # r-value
        #train_final.append(str(max_sim[ab]))
    final.append(train_final)
        
dest = folderpath + "/output_csv/" + "R_value.csv"
params_df = pd.DataFrame(final)
#col_dict = {}
#col_dict[0] = 'ID' 
#col_dict[19] = 'R-Value'
#col_dict[20] = 'Similarity'
#col_dict[21] = 'Distance'
#params_df.rename(columns=col_dict, inplace=True)
params_df.to_csv(dest, index = True)
#print("dataframe",params_df)
train_final = []
   
