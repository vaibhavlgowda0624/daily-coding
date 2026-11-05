def student_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

student_profile(
    name="Vaibhav",
    course="MCA",
    specialization="Cyber Security"
)
