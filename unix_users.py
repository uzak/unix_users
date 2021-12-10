USER_FILE_PATH = "/etc/passwd"

def read_users(human_only=False):
    """
    Read files from USER_FILE_PATH and return them
    parsed as a list of tokens.
    """
    users = []
    with open(USER_FILE_PATH) as f:      # context manager
        for line in f:
            line = line.strip()
            tokens = line.split(":")
            shell = tokens[-1]
            if not human_only:
                users.append(tokens)
            elif shell.endswith("sh"):
                users.append(tokens)
    return users
