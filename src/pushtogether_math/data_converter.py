# Vote stream input should be a list with the following format
# [('choice', 'user_id', 'comment_id'), ...]

import pandas as pd

def populate_dataframe(dataframe, votes):
    for vote, user, comment in votes:
        dataframe.loc[user].loc[comment] = vote

def get_comments_set(votes):
    comments = sorted({comment for _, _, comment in votes})
    return comments

def get_users_set(votes):
    users = sorted({user for _, user, _ in votes})
    return users

def convert_to_dataframe(votes):
    comments = get_comments_set(votes)
    users = get_users_set(votes)
    votes_dataframe = pd.DataFrame(index=users, columns=comments)
    populate_dataframe(votes_dataframe, votes)
    return votes_dataframe
