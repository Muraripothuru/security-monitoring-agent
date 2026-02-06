import json
from datetime import datetime

INCIDENT_FILE = "data/incidents.json"

def respond(threat):
    incident = {
        "id": f"INC-{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "type": threat["type"],
        "severity": threat["severity"],
        "action": "IP Blocked & SOC Alerted",
        "time": str(datetime.now())
    }

    try:
        with open(INCIDENT_FILE, "r") as f:
            incidents = json.load(f)
    except:
        incidents = []

    incidents.append(incident)

    with open(INCIDENT_FILE, "w") as f:
        json.dump(incidents, f, indent=2)

    print(f"[RESPONSE] {incident['type']} handled automatically")
