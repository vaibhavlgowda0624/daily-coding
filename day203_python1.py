import re

text = """
Contact us at support@example.com
or admin@company.in
"""

emails = re.findall(
    r'\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b',
    text
)

print("Emails:", emails)
