
import math


# finding sequence span for signal
def get_signal(cl_seq, cl_dict):
    signal = []
    #m = cl_seq[0]
    start=0
    i=0
    j=0
    while i<len(cl_seq):
        m = cl_seq[i]
        #print(m)
        while j<len(cl_seq) and m == cl_dict[j]:
            #print("hi",cl_dict[j],j)
            j=j+1
        temp = [m,start,j-1]
        #print(temp)
        signal.append(temp)        
        start=j
        i=j   
    return signal


def get_mcl(cl_seq):
    max_cl = max(cl_seq)
    return max_cl

def get_nmcl(cl_seq, cl_signal):
    nmcl = []
    cl_set = set()
    for i in range(len(cl_signal)):
        cl_set.add(cl_signal[i][0])
    cl_list = list(cl_set)
    cl_list.sort(reverse=True)
    mcl = max(cl_seq)
    count = 0
    for i in range(len(cl_list)):
        if cl_list[i]==mcl:
            continue
        temp = 0
        for s in range(len(cl_signal)):
            if cl_signal[s][0]==cl_list[i]:
                temp += 1
        #temp = cl_signal.count(cl_list[i])
        if temp>5 and count!=0:
            break
        for j in range(temp):
            nmcl.append(cl_list[i])
        count += 1
    return nmcl

def get_mcl_location(cl_seq, cl_signal):
    mcl_loc = []
    cl_len = len(cl_signal)
    mcl = get_mcl(cl_seq)
    print("length of cl_siqnal=",len(cl_signal))
    
    for i in range(cl_len):
        if cl_signal[i][0] == mcl:
            loc=math.ceil((cl_signal[i][1]+cl_signal[i][2])/2)
            mcl_loc.append(loc)
    return mcl_loc

def get_nmcl_location(cl_seq, nmcl, cl_signal):
    #print("nmcl values :", nmcl)
    nmcl_loc = []
    cl_len = len(cl_signal)
    nmcl_set = set(nmcl)
    nmcl_list = list(nmcl_set)
    mcl = get_mcl(cl_seq)
    for i in range(cl_len):
        if cl_signal[i][0] != mcl:
            if cl_signal[i][0] in nmcl_list:
                loc=math.ceil((cl_signal[i][1]+cl_signal[i][2])/2)
                nmcl_loc.append(loc)
    return nmcl_loc


def cl_sequence_extractor(cl_row):
    cl_string = cl_row['cl_data']
    cl_sequence = [int(x) for x in cl_string.split(',')]
    return cl_sequence


def get_minus_5_flag(cl_seq):
    cl_len = len(cl_seq)
    for i in range(cl_len):
        if cl_seq[i] == -5:
            return True
    return False


def get_mcl_count(cl_seq, mcl,cl_signal):
    count = 0
    for i in range(len(cl_signal)):
        if cl_signal[i][0]==mcl:
            count += 1
    return count

def get_mcl_range(cl_seq, mcl):
    ind = [i for i,x in enumerate(cl_seq) if x == mcl]
    return len(ind)

def get_lsf_rsf(cl_seq,mcl,cl_signal):
     ret = [0]*4
     mcl_signals = [x for i, x in enumerate(cl_signal) if x[0] == mcl]
     print("mcl_signals:",mcl_signals)  
     print("mcl_signals length:",len(mcl_signals))
     # finding LSF and LSS
     flag1=0
     flag2=0
     flag3=0
     flag4=0
     cl_count=0
     loc = []
     #k=0
     
     for i in range(len(mcl_signals)):
          
         for s in range(len(cl_signal)):
             if cl_signal[s] == mcl_signals[i]:   
                 print("cl signal index", cl_signal.index(cl_signal[s]))
                 loc.append(cl_signal.index(cl_signal[s]))
         
         print("hi", loc)
         for j in range(loc[i]-1,loc[i]-6,-1) :   
             if j>=0:
                 print("cl",cl_signal[j])
                 if cl_signal[j][0]==1:
                     break
                 elif cl_signal[j][0]!=1 and cl_signal[j][0]!=mcl_signals[i][0]: 
                                
                    if cl_signal[j][1]==cl_signal[j][2]:
                        flag1=1
                        cl_count=cl_count+1
                    elif cl_signal[j][1]!=cl_signal[j][2]:
                        flag2=1 
                        cl_count=cl_count+1
 
         for j in range(loc[i]+1,loc[i]+6,1) :   
             if j<len(cl_signal):
                 print("cl",cl_signal[j])
                 if cl_signal[j][0]==1:
                     break
                 elif cl_signal[j][0]!=1 and cl_signal[j][0]!=mcl_signals[i][0]: 
                                
                    if cl_signal[j][1]==cl_signal[j][2]:
                        flag3=1
                        cl_count=cl_count+1
                    elif cl_signal[j][1]!=cl_signal[j][2]:
                        flag4=1 
                        cl_count=cl_count+1

    #print("cl signal total count",cl_count)                       
     if flag1==0:
         ret[0]=0 #lsf
     elif flag1==1:
        ret[0]=1
     if flag2==0:#lss
         ret[1]=0
     elif flag2==1:
        ret[1]=1
     if flag3==0:#rsf
         ret[2]=0
     elif flag3==1:
        ret[2]=1
     if flag4==0:#rss
         ret[3]=0
     elif flag4==1:
        ret[3]=1
     return ret[0], ret[1], ret[2], ret[3]      



def get_Group_val(mcl_value,mcl_count,max_nmcl):
    if mcl_value-max_nmcl < 0.2 * mcl_value:
        return 0
    if mcl_count==1:
        return 1
    if mcl_count>1:
        return 2    

"""
def get_group_val(cl_seq, mcl, nmcl, cl_signal):
    max_nmcl = max(nmcl, default=0)   #change
    mcl=int(mcl)
    mcl_20 = 0.2* mcl
    if (mcl-int(max_nmcl)) < mcl_20:
        return 0
    elif get_mcl_count(cl_seq, mcl, cl_signal) == 1:
        return 1
    elif get_mcl_count(cl_seq, mcl, cl_signal) > 1:
        return 2


def get_Group_val(mcl_count,nmcl_count):
    if mcl_count==1:
        if nmcl_count >= 0 and nmcl_count<=3:
            return 0
        if nmcl_count >= 4 and nmcl_count<=9:
            return 1
        if nmcl_count > 9:
            return 2
    if mcl_count==2:
        return 3
    if mcl_count>=3:
        return 4
    
"""
    
def getMclGroup(val):
    val=int(val)
    if val <=6 :
        return 0
    if val >= 7 and val <=10 :
        return 1
    if val >= 11 and val <=13 :
        return 2
    if val >= 14 and val <=16 :
        return 3
    if val >= 17 and val <=20 :
        return 4
    if val >= 21 and val <=25 :
        return 5
    if val >= 26 and val <=34 :
        return 6
    if val >= 35 and val <=45 :
        return 7
    if val >= 45 :
        return 8


def get_signal_location_vector(cl_seq, mcl_loc, nmcl_loc):
    mcl_len = len(mcl_loc)
    signal_loc_vector = []
    for i in range(mcl_len):
        temp = []
        for ele in nmcl_loc:
            temp.append(ele)
        for j in range(mcl_len):
            if i!=j:
                temp.append(mcl_loc[j])
        temp.sort()
        #temp.remove(mcl_loc[i])
        signal_loc_vector.append(temp)
    return signal_loc_vector

def get_signal_distance_vector(cl_seq, mcl_loc, signal_loc_vector):
    mcl_len = len(mcl_loc)
    signal_dis_vector = []
    for i in range(mcl_len):
        temp = signal_loc_vector[i]
        mcl = mcl_loc[i]
        temp_dist = []
        for ele in temp:
            temp2 = abs(ele-mcl)
            temp_dist.append(temp2)
        #temp_dist.remove(0)
        signal_dis_vector.append(temp_dist)
    return signal_dis_vector
    

def get_lsdv(signal_dis_vector, signal_loc_vector, mcl_loc):
    length = len(signal_dis_vector)
    lsdv = []
    for i in range(length):
        temp = []
        temp_dis = signal_dis_vector[i]
        mcl = mcl_loc[i]
        temp_loc = signal_loc_vector[i]
        for j in range(len(temp_loc)):
            if temp_loc[j] < mcl:
                temp.append(temp_dis[j])
        lsdv.append(temp)
    return lsdv


def get_rsdv(signal_dis_vector, signal_loc_vector, mcl_loc):
    length = len(signal_dis_vector)
    lsdv = []
    for i in range(length):
        temp = []
        temp_dis = signal_dis_vector[i]
        mcl = mcl_loc[i]
        temp_loc = signal_loc_vector[i]
        #temp_loc.remove(mcl)
        for j in range(len(temp_loc)):
            if temp_loc[j] > mcl:
                temp.append(temp_dis[j])
        lsdv.append(temp)
    return lsdv        

def get_adjectives(text):
    blob = TextBlob(str(text))
    return [ word for (word,tag) in blob.tags if tag.startswith("JJ")]
    #inidata['adjectives'] = inidata['Review'].apply(get_adjectives)
"""
def get_senti_value(pol):
    if(pol<0):
        return "negative"
    elif(pol==0):
        return "neutral"
    elif(pol>0):
        return "positive"
"""