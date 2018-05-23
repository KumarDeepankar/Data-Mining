import re


f = open('gate_default', 'r')
processed_list = []
line_count = 0
line_count_adv = 0
new_dic = {}
row_count = 0

aspect_pos = 0
aspect_pos_list = []
fo = open('fp_growth_input.txt', 'w')


for line in f:

    matchObj = re.split(r'\s', line, re.M | re.I)

    if(len(matchObj)) > 4:
            aspect_pos +=1

            if matchObj[5] =='category="NN"' or matchObj[5] =='category="NNP"' or matchObj[5] =='category="NNPS"' \
            or matchObj[5] =='category="NNS"':

                aspect_pos_dictionary = {}
                root_wrd2 = re.split(r'=', matchObj[4])
                root_wrd2 = root_wrd2[1][1:-1].lower()
                if root_wrd2 !='t':
                    aspect_pos_dictionary[root_wrd2] = aspect_pos
                    aspect_pos_list.append(aspect_pos_dictionary)

                    if root_wrd2 in new_dic:
                        new_dic[root_wrd2] += 1
                    else:
                        new_dic[root_wrd2] = 1

    if matchObj[2] == 'GATE_Sentence':
        #print (line_count)
        #print(aspect_pos_list)
        aspect_str = ""
        for dic in aspect_pos_list:
            for aspect in dic:
                aspect_str += aspect
                aspect_str += ','

        if len(aspect_str) !=0:
            print (aspect_str[0:-1])
            fo.write(aspect_str[0:-1])
            fo.write("\n")
            aspect_pos = 0
            aspect_pos_list = []
            aspect_pos_dictionary = {}
        line_count += 1

sorted_aspect = sorted(new_dic, key = lambda k: (-new_dic[k], k))

fo.close()







