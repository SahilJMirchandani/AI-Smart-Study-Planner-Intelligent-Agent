from agents.study_planner import create_study_plan, track_progress, generate_weekly_schedule

print("🤖 AI Smart Study Planner Agent")
print("--------------------------------")

num_subjects = int(input("Enter number of subjects: "))

subjects = []

for i in range(num_subjects):
    subject = input(f"Enter subject {i+1}: ")
    subjects.append(subject)

hours = float(input("Enter study hours per day: "))

create_study_plan(subjects, hours)

print("\nTrack your study progress")

total_topics = int(input("Enter total topics: "))
completed_topics = int(input("Enter completed topics: "))

track_progress(completed_topics, total_topics)

generate_weekly_schedule(subjects)