# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 21:33:24 2020

@author: saile
"""
def check_msp(d1,d2):
    if d2==0:
        q=d1
    else:  
        q=d1/d2
    a=(d1+d2)/2
    if a<=30 and q>=0.8:
        return 1
    if a<=60 and q>=0.82:
        return 1
    if d2<100 and q>=0.8:
        return 1
    if d2>=100 and d2<=199 and q>0.88:
        return 1
    if d2>=200 and d2<=299 and q>0.9:
        return 1
    if d2>=300 and d2<=399 and q>0.92:
        return 1
    if d2>=400 and d2<=499 and q>0.94:
        return 1
    if d2>=500 and d2<=609 and q>0.96:
        return 1
    if d2>=600 and q>0.98:
        return 1
    return 0


"""
def find_rvalue(msp,mmc):
    rows = len(msp)
    print("rows",rows)    
    cols = len(msp[0])
    print("cols",cols)
    r_value = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        #print("R-value-test-entry",i)
        for j in range(cols):
            if mmc[i][j] == 0 :
                r_value[i][j] = msp[i][j]
            else :
                r_value[i][j]=round(msp[i][j]/mmc[i][j],2)
    return r_value
"""
            
def find_rvalue(msp,mmc):
    total_msp=0
    total_mmc=0
    r_value=0
    flat_msp = [ item for elem in msp for item in elem]
    flat_mmc = [ item for elem in mmc for item in elem]
    for ele in range(0, len(flat_msp)):
        total_msp = total_msp + flat_msp[ele]
    for ele in range(0, len(flat_mmc)):
        total_mmc = total_mmc + flat_mmc[ele]
    
    if total_mmc==0:
        r_value=total_msp
    else:
        r_value=round(total_msp/total_mmc,2)
    #print("R_value=",r_value, total_msp, total_mmc, flat_msp,flat_mmc)
    return r_value

def getNumberOfZeroesInMarkers(markers) :
    count = 0
    for i in markers :
        if i == 0 :
            count+= 1
    return count  

def msp_mmc(test,train):
    msp=0
    mmc=0
    if len(train)>len(test):
        markers = [0 for i in range(len(train))]
    else:
        markers = [0 for i in range(len(test))]
    for j in range(len(test)):
        for l in range(len(train)):
            x=check_msp( test[j] , train[l])
            if x==1:
                markers[l] = 1
                msp+=1
    mmc += getNumberOfZeroesInMarkers(markers)
    return msp,mmc


def fun(test_lsdv,train_lsdv):           # SDV values
    msp = [[0 for i in train_lsdv] for j in test_lsdv]
    mmc = [[0 for i in train_lsdv] for j in test_lsdv]
    
    for i in range(len(test_lsdv)):
        for j in range(len(train_lsdv)):
            
            if len(test_lsdv) == 1 and len(train_lsdv)== 1:
                if len(test_lsdv[0]) == 0 and len(train_lsdv[0]) == 0:
                    msp[i][j]=0
                    mmc[i][j]=0
                elif len(test_lsdv[0]) == 0 or len(train_lsdv[0]) == 0:
                    msp[i][j]=0
                    mmc[i][j]=len(test_lsdv[0])+len(train_lsdv[0])
                else:
                    msp_,mmc_= msp_mmc(test_lsdv[0],train_lsdv[0])
                    msp[i][j] += msp_
                    mmc[i][j] += mmc_
            else:
                msp_,mmc_ = msp_mmc(test_lsdv[i],train_lsdv[j])
                msp[i][j] += msp_
                mmc[i][j] += mmc_
                
    return msp,mmc                
