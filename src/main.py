# Main Python script for analyzing logs
from elasticsearch import Elasticsearch
from anomaly_detection import detect_brute_force, detect_unusual_logins
from notifier import send_notification

# Connect to Elasticsearch
es = Elasticsearch("http://localhost:9200")

def main():
    # Query Elasticsearch for recent logs
    query = {
        "query": {
            "range": {
                "@timestamp": {
                    "gte": "now-1d/d",
                    "lt": "now/d"
                }
            }
        }
    }
    logs = es.search(index="server-logs-*", body=query)

    # Detect anomalies
    brute_force_ips = detect_brute_force(logs)
    unusual_logins = detect_unusual_logins(logs)

    # Notify if anomalies are found
    if brute_force_ips:
        send_notification("Brute Force Detected", brute_force_ips)
    if unusual_logins:
        send_notification("Unusual Logins Detected", unusual_logins)

if __name__ == "__main__":
    main()
