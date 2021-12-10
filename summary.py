from unix_users import read_users

def summary():
    all_users = read_users()
    print(f"We've got total of {len(all_users)} users")
    humans = read_users(human_only=True)
    usernames = set()
    for user in humans:
        usernames.add(user[0])
    print(f"Human users are: {', '.join(usernames)}")


if __name__ == '__main__':
    summary()
