class StudyPlanner:

    def __init__(self, ranked_subjects, total_days):
        self.ranked_subjects = ranked_subjects
        self.total_days = total_days

    def generate_plan(self):

        schedule = []
        index = 0
        n = len(self.ranked_subjects)

        for day in range(1, self.total_days + 1):

            subject = self.ranked_subjects[index][0]

            schedule.append((day, subject))

            index = (index + 1) % n

        return schedule