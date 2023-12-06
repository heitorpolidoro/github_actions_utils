# @lru_cache
# def get_github(token: str = None) -> GithubPlus:
#     """
#     Returns an logged instance of Github.
#     If token is not provided, it will try to get the token from the environment.
#     If the token is not found, it will return an unlogged instance of Github.
#     If the token is found, it will return an logged instance of Github.
#     :param token: The token to use to log in. If not provided, it will try to get the token from the environment.
#     :return: An instance of Github.
#     """
#     token = token or github_envs.token
#     token = Token(token) if token else None
#     gh = GithubPlus(auth=token)
#     return gh
#
#
# def get_commit_message_command(repo: Repository, command_prefix: str) -> str | None:
#     """
#     Retrieve the command from the last commit message.
#     The command in the commit message must be in the format [command_prefix: command]
#
#     :param repo: The repository object.
#     :param command_prefix: The command prefix to look for in the commit message.
#     :return: The extracted command or None if there is no command.
#     :raises: ValueError if the command is not valid.
#     """
#     commit_message = repo.get_commits()[0].commit.message
#     command_pattern = rf"\[{command_prefix}:(.+?)\]"
#     commands_found = re.findall(command_pattern, commit_message)
#     if commands_found:
#         return commands_found[-1].strip()
#     return None
