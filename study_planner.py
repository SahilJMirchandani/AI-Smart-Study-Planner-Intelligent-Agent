def create_study_plan(subjects, hours_per_day):

    print("\nEnter difficulty for each subject (easy / medium / hard)\n")

    weights = []

    for subject in subjects:

        difficulty = input(f"Difficulty of {subject}: ").lower()

        if difficulty == "easy":
            weight = 1
        elif difficulty == "medium":
            weight = 2
        elif difficulty == "hard":
            weight = 3
        else:
            weight = 2

        weights.append(weight)

    total_weight = sum(weights)

    print("\n📚 AI Optimized Study Plan")
    print("----------------------------")

    for i in range(len(subjects)):

        hours = (weights[i] / total_weight) * hours_per_day

        print(f"{subjects[i]} : {round(hours,2)} hours")


def track_progress(completed, total):

    progress = (completed / total) * 100

    print("\n📊 Study Progress")
    print("----------------------------")
    print(f"Completed Topics : {completed}")
    print(f"Total Topics : {total}")
    print(f"Progress : {round(progress,2)}%")

    print("\n🤖 AI Recommendation")

    if progress < 40:
        print("You are behind schedule. Increase study hours.")

    elif progress < 70:
        print("Good progress. Maintain consistency.")

    else:
        print("Excellent work! Focus on revision.")


def generate_weekly_schedule(subjects):

    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    print("\n📅 AI Weekly Study Schedule")
    print("----------------------------")

    for i in range(len(days)):

        if i < len(subjects):
            print(f"{days[i]} : {subjects[i]}")

        elif i < 6:
            subject = subjects[i % len(subjects)]
            print(f"{days[i]} : {subject}")

        else:
            print("Sunday : Revision")