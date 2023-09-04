class Regexps:
    JWT_PATTERN = (
        r"((?:[A-Za-z0-9\-_]+\.){2}"
        r"[A-Za-z0-9\-_]+)'|((?:[A-Za-z0-9\-_]+\.){2}"
        r"[A-Za-z0-9\-_]+)"
    )
