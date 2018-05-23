import re



f = open('gate_default', 'r')
processed_list = []
line_count = 0
line_count_adv = 0
new_dic = {}
row_count = 0
for line in f:

    matchObj = re.split(r'\s', line, re.M | re.I)

    if(len(matchObj)) > 4:
            if matchObj[5] =='category="NN"' or matchObj[5] =='category="NNP"' or matchObj[5] =='category="NNPS"'\
            or matchObj[5] == 'category="NNS"':

                root_wrd2 = re.split(r'=', matchObj[4])
                root_wrd2 = root_wrd2[1][1:-1].lower()
                if root_wrd2 != 't':
                    if root_wrd2 in new_dic:
                        new_dic[root_wrd2] += 1
                    else:
                        new_dic[root_wrd2] = 1

sorted_aspect = sorted(new_dic, key = lambda k: (-new_dic[k], k))

fo = open('ex_2_noun.txt', 'w')

for i in sorted_aspect:
    print(i+" : "+str(new_dic[i]))
    fo.write(i+" : "+str(new_dic[i]))
    fo.write("\n")
fo.close()







