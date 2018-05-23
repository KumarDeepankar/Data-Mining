import re


f = open('CanonG3_tagged.txt', 'r')
ground_truth_set= set()

for line in f:
    matchObj = re.split(r'##', line, re.M | re.I)
    #print matchObj[0]
    matchObj2 = re.split(r',', matchObj[0], re.M | re.I)
    #print matchObj2
    if matchObj2 != []:
        #print matchObj2
        freq_asp = ""
        for el in matchObj2:

            if re.match(r'.*\[.*\]$', el):
                #print el
                if re.match(r'.*\[[a-z].*\]$', el):
                    el = el[0:-7]
                else:
                    el = el[0:-4]
                el = el.strip()
                #print el
                freq_asp += el +","
        #print freq_asp[0:-1]
        ground_truth_set.add(freq_asp[0:-1])
        freq_asp =""
#print ground_truth_set
#print len(ground_truth_set)
f2 = open('aspect_dictionary.txt', 'r')
dictionary_set= set()
for line2 in f2:
    dic_matchObj = re.split(r':', line2, re.M | re.I)

    dic_matchObj[0] = dic_matchObj[0].replace(",", " ")
    #print dic_matchObj[0]
    dictionary_set.add(dic_matchObj[0])
#print dictionary_set
#print len(dictionary_set)

intersection = ground_truth_set & dictionary_set
TP = len(intersection)
print "True Positive: " + str(TP)

FN = len(ground_truth_set) - TP
print "False Negative: " + str(FN)

FP = len(dictionary_set) - TP
print "False Positive: " + str(FP)

Precision = TP /float(len(dictionary_set))
print "Precision: " +str(Precision)

rc = TP/ float(FN + TP)
print "Recall: " +str( rc)

F1 = 2 * ((Precision * rc) /(Precision +rc ))

print "F1 score: "+ str(F1)