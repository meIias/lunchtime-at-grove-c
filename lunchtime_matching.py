"""
lunchtime_matching.py

- contains utility functions for matching user with coffee/lunch mates
- store schema:
{
    USER_LIST: [...],
    <user>: {
        lunch_matches: [...],
        coffee_matches: [...]
    },
    ...
}
"""
from random import randint

USER_LIST_FIELD = "USER_LIST"


def check_init_data_store(store):
    """
    initialize some fake data for initial startup
    """
    if USER_LIST_FIELD not in store:
        store[USER_LIST_FIELD] = [
            "john", "dave", "test", "gary", "ron", "mark", "jenny", "jessica", "christina",
            "tessa", "billy", "sophie", "dotty", "walrus", "sonny bono", "fred"
        ]


def find_coffeemate(store, user):
    """
    implements the coffee user matching algorithm
    - match with one other user
    - user cannot have been matched before
    """
    u = user.lower()
    _init_user_store(store, u)

    matched_user = ""
    invalid_indices = []
    available_users = store.get(USER_LIST_FIELD, [])
    num_available_users = len(available_users)

    # iterate over users randomly until an appropriate match is found
    while True:
        # all users already had coffee with this user
        if len(invalid_indices) == num_available_users:
            break

        i = _get_rand_from_range(0, num_available_users - 1)
        if i in invalid_indices:
            continue
        else:
            invalid_indices.append(i)

        matched_user = available_users[i]

        # end on valid user found
        if matched_user not in store[u].get("coffee_matches") and matched_user.lower() != u:
            store[u].get("coffee_matches").append(matched_user)
            break
        else:
            matched_user = ""

    return matched_user


def find_lunchmates(store, user):
    """
    implements the lunch group matching algorithm
    - between 3 to 5 users
    - prioritize unmatched users
    """

    def find_lunchmates_recursive(store, user, remaining=-1, already_matched=[]):
        """
        recursive function to match users for lunch while maintaining new user priority
        """
        u = user.lower()
        _init_user_store(store, u)

        available_users = store.get(USER_LIST_FIELD)
        num_available_users = len(available_users)

        if num_available_users < 3:
            # not enough users to get lunch
            return []
        elif num_available_users == len(store[u]["lunch_matches"]):
            # reset when full (different from coffee matching)
            store[u]["lunch_matches"] = []

        matched_users = []

        # random group size between 3, 5
        # recursively add remaining number of users required
        if remaining == -1:
            target_group_size = _get_rand_from_range(3, 5)
        else:
            target_group_size = remaining

        # get n users based on target group size
        invalid_indices = []
        while len(matched_users) < target_group_size:
            if len(invalid_indices) == num_available_users:
                break

            i = _get_rand_from_range(0, num_available_users - 1)

            if i in invalid_indices:
                continue

            matched_users.append(
                available_users[i]
            )

            invalid_indices.append(i)

        # prepare recursive call by sanctioning off valid matched users vs repeated users
        if len(already_matched) < num_available_users:
            matched_users = [
                mu for mu in matched_users if
                mu not in store[u].get("lunch_matches") and
                mu.lower() != u and
                mu not in already_matched
            ]

            already_matched_users = already_matched + [
                mu for mu in matched_users if
                mu in store[u].get("lunch_matches") or
                mu.lower() == u and
                mu not in already_matched
            ]

        # recursively add more unmatched users if group size is less than desired
        if len(matched_users) < target_group_size:
            return list(set(matched_users + find_lunchmates_recursive(
                store,
                user,
                remaining=target_group_size - len(matched_users),
                already_matched=already_matched_users
            )))

        return matched_users

    matched_users = list(set(find_lunchmates_recursive(store, user)))
    store[user.lower()]["lunch_matches"] = store[user.lower()]["lunch_matches"] + matched_users

    return matched_users


def _init_user_store(store, user):
    """
    adds the user to the data store if not already added, initialize match lists
    """
    if user not in store:
        store[user] = {
            "lunch_matches": [],
            "coffee_matches": []
        }
        store[USER_LIST_FIELD].append(user)


def _get_rand_from_range(start, end):
    """
    random number range utility
    """
    return randint(start, end)
