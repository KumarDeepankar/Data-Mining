import re

f1 = open('negative-words.txt', 'r')
f2 = open('positive-words.txt', 'r')
positive_set = set()
negative_set = set()

for line1 in f1:
    n_wrd = line1.strip()
    negative_set.add(n_wrd)
for line2 in f2:
    p_wrd = line2.strip()
    positive_set.add(p_wrd)

op_wrd = open('opinion_wrd.txt', 'r')
po_op_wrd = 0
ne_op_wrd = 0
ne_wrd_lst = []
po_wrd_lst = []
for line in op_wrd:
    matchObj = re.split(r':', line, re.M | re.I)
    opinion_word = matchObj[0]
    if opinion_word in positive_set:
        po_op_wrd += 1
        po_wrd_lst.append(opinion_word)
    if opinion_word in negative_set:
        ne_op_wrd += 1
        ne_wrd_lst.append(opinion_word)

print "Positive opinion words: " + str(po_op_wrd)
print "Negative  opinion words: " + str(ne_op_wrd)
print "Negative words list:"
print ne_wrd_lst
print "Positive words list:"
print po_wrd_lst
