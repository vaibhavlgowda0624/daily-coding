import re

text = "Learning #Python and #CyberSecurity with #MCA"

hashtags = re.findall(r"#\w+", text)

print("Hashtags:", hashtags)
