class GitHubApiRateLimitExceedeError(Exception):

    """
    Raises when the GitHub API rate limit has been exceeded. The GitHub API
    has a rate limit that restricts the number of requests that can be made
    in a given period of time. If this limit is exceeded, this exception is
    raised.
    """

    # pass
