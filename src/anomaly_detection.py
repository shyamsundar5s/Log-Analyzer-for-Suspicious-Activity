# Module for anomaly detection
import re

def detect_brute_force(logs):
    brute_force_ips = {}
    for log in logs["hits"]["hits"]:
        message = log["_source"]["message"]
        match = re.search(r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)", message)
        if match:
            ip = match.group(1)
            brute_force_ips[ip] = brute_force_ips.get(ip, 0) + 1

    # Return IPs with more than 5 failed attempts
    return {ip: count for ip, count in brute_force_ips.items() if count > 5}

def detect_unusual_logins(logs):
    unusual_logins = []
    for log in logs["hits"]["hits"]:
        # Example: Check for logins at odd hours
        timestamp = log["_source"]["@timestamp"]
        hour = int(timestamp.split("T")[1].split(":")[0])  # Extract hour
        if hour < 6 or hour > 22:  # Unusual time range
            unusual_logins.append(log["_source"])
    return unusual_logins
