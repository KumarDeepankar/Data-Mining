import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Main program starts here
# read the data
user_shows_pd = pd.read_csv('user-shows.txt', sep=' ', header=None)

user_show_matrix = (np.asarray(user_shows_pd, dtype=int))
num_users, num_shows = user_show_matrix.shape

shows_pd = np.asarray(pd.read_csv('shows.txt', sep=' ', header=None))


with open('trng.txt', 'w') as f:
    for user in range(num_users):
        for item in range(num_shows):
            if user_show_matrix[user, item] == 1:
                f.write(str(user+1))
                f.write(',')
                f.write(str(item+1))
                f.write('\n')
show_ids = []


def user_user_item_item_matrix(matrix1, users_item_rating_mat, is_user_sim):
    cosine_similarity_mat = cosine_similarity(matrix1, matrix1)
    if is_user_sim:
        print ("User-User Filtering")
        tau_mat_u2u = np.dot(cosine_similarity_mat, users_item_rating_mat)
    else:
        print ("Item-Item Filtering")
        tau_mat_u2u = np.dot(users_item_rating_mat, cosine_similarity_mat)
    sorted_index = np.argsort(tau_mat_u2u[19, :])
    reversed_sorted_index = sorted_index[::-1]
    top_100_shows_list = []
    for i in range(10):
        index = reversed_sorted_index[i]
        rating = tau_mat_u2u[19, index]
        show_name = shows_pd[index]
        top_100_shows_list.append(show_name[0])
        print ("Show Id = " + str(index+1) + " " + show_name[0] + " rating :" + str(rating))

    return top_100_shows_list


top_shows_u2u = user_user_item_item_matrix(user_show_matrix, user_show_matrix, True)
top_shows_item2item = user_user_item_item_matrix(user_show_matrix.transpose(), user_show_matrix, False)
show_ids_list = [145, 97, 36,75,156,174,206,64,141,146, 97, 75, 141, 46, 61, 157, 69, 36, 138, 327,
            235, 49, 38, 544, 491, 478, 281, 554, 490, 223, 49, 78, 193, 209, 281, 196, 208, 223, 220, 490]
show_ids_sorted = show_ids_list.sort()
print ("==Sorted Ids==")
for item in show_ids_list:
    show_id = item -1
    print (str(item) + "," +  shows_pd[show_id][0])