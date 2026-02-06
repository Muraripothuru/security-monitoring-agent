
from agents.log_analyzer import analyze_log
from agents.threat_detector import detect_threat
from agents.response_coordinator import respond

RAW_LOGS = "data/raw_logs.txt"
SCALEDOWN_LOGS = "data/scaledown_logs.txt"

summary = {}

with open(RAW_LOGS, "r") as logs:
    for line in logs:
        event = analyze_log(line)
        summary[event] = summary.get(event, 0) + 1

        threat = detect_threat(event)
        if threat:
            respond(threat)

with open(SCALEDOWN_LOGS, "w") as out:
    for event, count in summary.items():
        out.write(f"{event} → {count}\n")

print("✅ Log processing complete")
print("📉 ScaleDown compression applied")
