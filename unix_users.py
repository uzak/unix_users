def read_users(human_only=False):
    users = []
    with open("/etc/passwd") as f:      # context manager
        for line in f:
            line = line.strip()
            tokens = line.split(":")
            shell = tokens[-1]
            if not human_only:
                users.append(tokens)
            elif shell.endswith('sh'):
                users.append(tokens)
    return users

def summary():
    all_users = read_users()
    print(f"We've got total of {len(all_users)} users")
    humans = read_users(human_only=True)
    usernames = set()
    for user in humans:
        usernames.add(user[0])
    print(f"Human users are: {', '.join(usernames)}")

summary()
