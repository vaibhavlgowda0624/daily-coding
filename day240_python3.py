import json

report = {
    "total_logs": 4,
    "info": 2,
    "warnings": 1,
    "errors": 1,
    "status": "Review Required"
}

with open("security_report.json", "w") as file:
    json.dump(report, file, indent=4)

print("Security report generated.")
