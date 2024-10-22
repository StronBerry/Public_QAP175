import warnings

warnings.filterwarnings('ignore')


def sort_users_by_activity(user_activity):
    return sorted(user_activity, key=lambda user: user_activity[user], reverse=True)


print(sort_users_by_activity({'Alice': 5, 'Bob': 2, 'Charlie': 10, 'David': 7}))