import unix_users


def detail(username):
    all_users = unix_users.read_users()
    for user in all_users:
        if user[0] == username:
            print(user)
            return
    print(f'Could not find user {username}')


if __name__ == '__main__':
    detail('markus')
