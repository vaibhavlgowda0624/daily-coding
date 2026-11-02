projects = [
    {"name": "Expense Tracker", "status": "Completed"},
    {"name": "Portfolio Website", "status": "In Progress"},
    {"name": "Password Checker", "status": "Completed"},
    {"name": "Weather App", "status": "Planned"}
]

completed = sum(
    project["status"] == "Completed"
    for project in projects
)

print("PROJECT SUMMARY")
print("----------------")

for project in projects:
    print(f'{project["name"]}: {project["status"]}')

print(f"\nTotal projects: {len(projects)}")
print(f"Completed projects: {completed}")
