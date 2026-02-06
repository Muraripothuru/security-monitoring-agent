
def analyze_log(log_line):
    log_line = log_line.lower()

    if "failed login" in log_line:
        return "AUTH_FAILURE"
    elif "sql injection" in log_line:
        return "SQL_INJECTION"
    elif "xss" in log_line:
        return "XSS_ATTACK"
    elif "normal login" in log_line:
        return "NORMAL_LOGIN"
    else:
        return "UNKNOWN"
