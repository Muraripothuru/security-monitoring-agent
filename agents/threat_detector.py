from collections import defaultdict

event_counter = defaultdict(int)

def detect_threat(event_type):
    event_counter[event_type] += 1

    if event_type == "AUTH_FAILURE" and event_counter[event_type] >= 3:
        return {
            "type": "Brute Force Attack",
            "severity": "High"
        }

    if event_type == "SQL_INJECTION":
        return {
            "type": "SQL Injection",
            "severity": "Critical"
        }

    return None

