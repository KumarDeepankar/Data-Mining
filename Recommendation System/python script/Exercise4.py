import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

pd_df = pd.read_csv('user-shows.txt', sep=" ", header = None)
pd_df2 = pd.read_csv('shows.txt', sep=' ', header=None)

user_show_matrix = np.asarray(pd_df,dtype=int)
shows_list = np.asarray(pd_df2,dtype=str)

watched_shows = []

for i in range(100):

    if user_show_matrix[19,i] == 1:
        show = shows_list[i]
        watched_shows.append(show[0])
        user_show_matrix[19, i] = 0


def user_user_matrix(matrix1,matrix2):
    cosine_similarity_mat = cosine_similarity(matrix1, matrix2)
    matrix_user_user = np.dot(cosine_similarity_mat, matrix2)

    sorted_index = np.argsort(matrix_user_user[19, :])

    reversed_sorted_index = sorted_index[::-1]
    top_100_shows = {}
    top_100_shows_list = []
    print("user-user")
    for j in range(100):
        rating = matrix_user_user[19, reversed_sorted_index[j]]

        show_name = shows_list[reversed_sorted_index[j]]
        top_100_shows[show_name[0]] = rating
        top_100_shows_list.append(show_name[0])

        print(show_name[0] + " Similarity score :" + str(rating))

    return top_100_shows_list



def item_item_matrix(matrix1,matrix2):
    cosine_similarity_mat = cosine_similarity(matrix1, matrix1)
    matrix_item_item = np.dot(matrix2,cosine_similarity_mat)

    sorted_index = np.argsort(matrix_item_item[19, :])

    reversed_sorted_index = sorted_index[::-1]
    top_100_shows = {}
    top_100_shows_list = []
    print("item-item")
    for j in range(100):
        rating = matrix_item_item[19, reversed_sorted_index[j]]

        show_name = shows_list[reversed_sorted_index[j]]
        top_100_shows[show_name[0]] = rating
        top_100_shows_list.append(show_name[0])

        print(show_name[0] + " Similarity score :" + str(rating))

    return top_100_shows_list




top100_shows_user_user = user_user_matrix(user_show_matrix, user_show_matrix)
top_k_true_positive_uu = []
total_shows_watched_top_100 = len(watched_shows)


def True_Positive_Rate_User_User(top_shows, tpr_list, k_show_top):
    num_shows_in_top_k_watched = 0
    shows_in_top_k = top_shows[0:k_show_top]
    #print (shows_in_top_k)
    for show in shows_in_top_k:
        if show in watched_shows:
            num_shows_in_top_k_watched += 1
    tpr = float(num_shows_in_top_k_watched) / total_shows_watched_top_100
    #print ("Matched# " + str(num_shows_in_top_k_watched))
    top_k_true_positive_uu.append(tpr)




top100_shows_item_item = item_item_matrix(user_show_matrix.transpose(), user_show_matrix)
top_k_true_positive_ii = []
total_shows_watched_top_100 = len(watched_shows)




def True_Positive_Rate_Item_Item(top_shows, tpr_list, k_show_top):
    num_shows_in_top_k_watched = 0
    shows_in_top_k = top_shows[0:k_show_top]
    #print (shows_in_top_k)
    for show in shows_in_top_k:
        if show in watched_shows:
            num_shows_in_top_k_watched += 1
    tpr = float(num_shows_in_top_k_watched) / total_shows_watched_top_100
   # print ("Matched# " + str(num_shows_in_top_k_watched))

    top_k_true_positive_ii.append(tpr)


for k in range(20):
    True_Positive_Rate_User_User(top100_shows_user_user, top_k_true_positive_uu, k)



for k in range(20):
    True_Positive_Rate_Item_Item(top100_shows_item_item, top_k_true_positive_ii, k)

k_values = np.arange(1, 21)
#Plot the graphs
#print(top_k_true_positive_uu)
#print(top_k_true_positive_ii)


plt.plot(k_values, top_k_true_positive_uu, label="User - user Collaborative Filtering")
plt.plot(k_values, top_k_true_positive_ii, label="Item - Item Collaborative Filtering")
plt.xlim(1, 20)
plt.xlabel("k")
plt.ylabel("True positive rate at top-k")
plt.legend(loc="upper right")
plt.show()