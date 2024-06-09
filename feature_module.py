import os
import pandas as pd
import mod3Module as m3m


# import matplotlib.pyplot as plt


def convert(lst):
    dct = {i: lst[i] for i in range(0, len(lst))}
    return dct


def df_colname_dict_creator(df):
    colname_list = list(df.columns)
    colname_dict = {}
    for i in range(2):
        colname_dict[i] = colname_list[i]
    return colname_dict


def feature_extract(initial_filename):
    folderpath = str(os.getcwd())
    # file1 = open(folderpath + '/parameter/initial_filename.txt','r')
    # initial_filename = file1.read()

    file2 = open(folderpath + '/parameter/datapos.txt', 'r')
    datapos = int(file2.read())

    cl_fileName = "cl_all.csv"

    inidata = pd.read_csv(folderpath + '/output_csv/' + cl_fileName)
    cl_data = pd.read_csv(folderpath + "/output_csv/" + cl_fileName)
    destination = folderpath + "/output_csv/" + "parameters_" + 'train.xlsx'
    parameters = []
    text = []
    label = []

    for index, row in inidata.iterrows():
        label.append(row[1])

    # print(label)
    # print(text[0])

    counter = 1

    # for i in range(len(cl_data)):
    for index, row in cl_data.iterrows():
        row = row.values.tolist()
        cl_sequence = row[2].split(',')

        print("\nInput Number " + str(counter))
        print("cl_sequence:", cl_sequence)

        for i in range(0, len(cl_sequence)):
            cl_sequence[i] = int(cl_sequence[i])

        counter += 1
        cl_dict = convert(cl_sequence)

        print("Dictionary =", cl_dict)
        print("length of cl_siquence=", len(cl_sequence))
        print("length of dictionary=", len(cl_dict))

        cl_size = len(cl_sequence)
        # mcl1=max(cl_sequence)
        mcl = m3m.get_mcl(cl_sequence)
        print("Mcl value is: " + str(mcl))

        cl_signal = m3m.get_signal(cl_sequence, cl_dict)
        print(cl_signal)

        nmcl = m3m.get_nmcl(cl_sequence, cl_signal)
        print("Nmcl list is: " + str(nmcl))

        max_nmcl = max(nmcl, default=0)

        cl_minus_5_flag = m3m.get_minus_5_flag(cl_sequence)
        # print("Cl minus 5 flag is: "+str(cl_minus_5_flag))

        #####################################################################################
        mcl_location = m3m.get_mcl_location(cl_sequence, cl_signal)
        # print("Mcl location vector is: "+str(mcl_location))

        mcl_count = m3m.get_mcl_count(cl_sequence, mcl, cl_signal)
        # print("Mcl count is: "+str(mcl_count))

        unique_cl_count = len(set(cl_sequence))
        print("unique_cl_count", unique_cl_count)

        #############################################################################
        nmcl_location = m3m.get_nmcl_location(cl_sequence, nmcl, cl_signal)
        # print("Nmcl location vector is: "+str(nmcl_location))
        #####################################################################################
        nmcl_count = len(nmcl_location)
        group_val = m3m.get_Group_val(mcl, mcl_count, max_nmcl)
        # print("Group val is: "+str(group_val))
        mcl_group = m3m.getMclGroup(mcl)

        signal_location_vector = m3m.get_signal_location_vector(cl_sequence, mcl_location, nmcl_location)
        # print("Signal location vector is: " + str(signal_location_vector))

        signal_distance_vector = m3m.get_signal_distance_vector(cl_sequence, mcl_location, signal_location_vector)
        # print("Signal Distance vector is: " + str(signal_distance_vector))

        lsdv = m3m.get_lsdv(signal_distance_vector, signal_location_vector, mcl_location)
        # print("LSDV is: " + str(lsdv))

        rsdv = m3m.get_rsdv(signal_distance_vector, signal_location_vector, mcl_location)
        # total number of mcl in cl sequence
        mcl_range = m3m.get_mcl_range(cl_sequence, mcl)

        # left signal fork and left signal step
        lsf, lss, rsf, rss = m3m.get_lsf_rsf(cl_sequence, mcl, cl_signal)

        final_list = []
        final_list = [str(index)] + row[2:] + [mcl_location] + [str(mcl)] + [str(mcl_count)] + [str(cl_minus_5_flag)] + [
            nmcl] + [nmcl_location] + [signal_location_vector] + [signal_distance_vector] + [lsdv] + [rsdv] + [
                         str(group_val)] + [str(mcl_group)] + [str(mcl_range)] + [str(lsf)] + [str(rsf)] + [
                         str(lss)] + [str(rss)] + [cl_size] + [label[index]] + [unique_cl_count]
        print(final_list)
        # print("RSDV is: " + str(rsdv))
        parameters.append(final_list)

        # print("******************************************************")
    # plt.plot(cl_sequence)
    # plt.show()

    params_df = pd.DataFrame(parameters)
    col_dict = df_colname_dict_creator(cl_data)
    print(params_df)
    col_dict[0] = 'id'
    col_dict[1] = 'cl_data'
    col_dict[2] = 'mcl_locations'
    col_dict[3] = 'mcl_value'
    col_dict[4] = 'mcl_count'
    col_dict[5] = 'cLminus5'
    col_dict[6] = 'nmcl_values'
    col_dict[7] = 'nmcl_locations'
    col_dict[8] = 'slv'
    col_dict[9] = 'sdv'
    col_dict[10] = 'LSDV'
    col_dict[11] = 'RSDV'
    col_dict[12] = 'Group'
    col_dict[13] = 'mclgroup'
    # col_dict[15] = 'Region'
    col_dict[14] = 'MCL Range'
    col_dict[15] = 'LSF'
    col_dict[16] = 'RSF'
    col_dict[17] = 'LSS'
    col_dict[18] = 'RSS'
    col_dict[19] = 'cl_size'
    col_dict[20] = 'label'
    col_dict[21] = 'unique_cl_count'

    # col_dict[21] = 'Sentiment'
    # col_dict[21] = 'Pronoun Class'
    params_df.rename(columns=col_dict, inplace=True)
    params_df.to_excel(destination, index=False)
    params_df.to_csv(folderpath + "/output_csv/" + "parameters_" + 'train.csv',index=False)
    return 1