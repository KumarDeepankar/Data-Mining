import re

opinion_word_count_dict = {}
def opinion_wrd_count(freq_opinion):
    lemma_pos = 0
    aspect_pos_list = {}
    opinion_wrd_pos_list = {}

    ga_f = open('gate_default', 'r')
    for line in ga_f:

        matchObj = re.split(r'\s', line, re.M | re.I)

        if (len(matchObj)) > 4:
            lemma_pos += 1

            if matchObj[5] == 'category="NN"' or matchObj[5] == 'category="NNP"' or matchObj[5] == 'category="NNPS"' \
            or matchObj[5] == 'category="NNS"':

                aspect_pos_dictionary = {}
                root_wrd = re.split(r'=', matchObj[4])
                root_wrd2 = root_wrd[1][1:-1].lower()
                if root_wrd2 != 't':
                    aspect_pos_dictionary[root_wrd2] = lemma_pos
                    aspect_pos_list[root_wrd2]= aspect_pos_dictionary


            if matchObj[5] == 'category="JJ"' or matchObj[5] == 'category="JJS"'or matchObj[5] == 'category="JJR"' \
            or matchObj[5] == 'category="RBR"' or matchObj[5] == 'category="RBS"' or matchObj[5] == 'category="RB"':
                opinion_pos_dictionary = {}
                root_wrd = re.split(r'=', matchObj[4])
                root_wrd2 = root_wrd[1][1:-1].lower()
                opinion_pos_dictionary[root_wrd2] = lemma_pos
                opinion_wrd_pos_list [root_wrd2] = opinion_pos_dictionary


        if matchObj[2] == 'GATE_Sentence':

            if (len(aspect_pos_list) != 0)& (len(opinion_wrd_pos_list) != 0):
                opinion_line_set = set()
               # print aspect_pos_list
                #print opinion_wrd_pos_list

                fre_as_noun = re.split(r',', freq_opinion, re.M | re.I)

                for i in fre_as_noun:

                    if i in aspect_pos_list:
                        c_noun = i
                        c_noun_position = aspect_pos_list[i][i]
                        #print c_noun +" "+ str(c_noun_position)
                        for op_ps in opinion_wrd_pos_list:
                            op_dst = opinion_wrd_pos_list[op_ps][op_ps]
                            diff = abs(op_dst- c_noun_position)
                            #print c_noun + " " + op_ps + " " + str(diff)
                            if diff <= 5:

                                opinion_line_set.add(op_ps)


                for val in opinion_line_set:
                    if val in opinion_word_count_dict:
                        opinion_word_count_dict[val] += 1
                    else:
                        opinion_word_count_dict[val] = 1
                #print opinion_line_set
                opinion_line_set = []




            lemma_pos = 0
            aspect_pos_list = {}
            opinion_wrd_pos_list = {}


f = open('aspect_dictionary.txt', 'r')
fq_set = set()
for line in f:
    matchObj = re.split(r':', line, re.M | re.I)
    fq_aspect = matchObj[0]
    fre_as_noun_1 = re.split(r',', fq_aspect, re.M | re.I)

    for i in fre_as_noun_1:
        fq_set.add(i)
for ff in fq_set:
    opinion_wrd_count(ff)

sorted_aspect = sorted(opinion_word_count_dict, key = lambda k: (-opinion_word_count_dict[k], k))
print sorted_aspect

i=0
last_c = sorted_aspect[0]
for top_k in sorted_aspect:
    if i < 10:
        if opinion_word_count_dict[top_k] < last_c:
            print top_k +" : "+ str(opinion_word_count_dict[top_k])
            last_c  = opinion_word_count_dict[top_k]
            i += 1

fo = open('opinion_wrd.txt', 'w')
for i in sorted_aspect:

    fo.write(i)
    fo.write(":")
    fo.write(str(opinion_word_count_dict[i]))
    fo.write("\n")
fo.close()