import datetime
import json
import os
import random

def update_pulse():
    os.makedirs("data", exist_ok=True)
    pulse_file = os.path.join("data", "activity_pulse.json")
    
    now = datetime.datetime.now(datetime.timezone.utc)
    date_str = now.strftime("%Y-%m-%d")
    timestamp_str = now.isoformat()
    
    pulse_data = {
        "last_updated_utc": timestamp_str,
        "status": "ONLINE",
        "node": "ABSOLUTE-01",
        "environment": "Null.Simulation.-01",
        "pulse_count": 1,
        "history": []
    }
    
    if os.path.exists(pulse_file):
        try:
            with open(pulse_file, "r", encoding="utf-8") as f:
                pulse_data = json.load(f)
        except Exception:
            pass
            
    pulse_data["last_updated_utc"] = timestamp_str
    pulse_data["pulse_count"] = pulse_data.get("pulse_count", 0) + 1
    
    # Keep last 100 pulse history records
    history = pulse_data.get("history", [])
    history.append({
        "timestamp": timestamp_str,
        "heartbeat_id": f"hb_{random.randint(100000, 999999)}",
        "metric_score": round(random.uniform(98.5, 100.0), 2)
    })
    pulse_data["history"] = history[-100:]
    
    with open(pulse_file, "w", encoding="utf-8") as f:
        json.dump(pulse_data, f, indent=2, ensure_ascii=False)
        
    print(f"Updated pulse: {timestamp_str} (Total Pulses: {pulse_data['pulse_count']})")

if __name__ == "__main__":
    update_pulse()
