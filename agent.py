class StudyAgent:

    def __init__(self, subjects):
        self.subjects = subjects

    def calculate_priority(self, subject):
        difficulty = subject["difficulty"]
        topics = subject["topics_left"]
        days = subject["days_left"]

        priority = (difficulty * topics) / days
        return priority

    def rank_subjects(self):
        ranked = []

        for subject in self.subjects:
            score = self.calculate_priority(subject)
            ranked.append((subject["name"], score))

        ranked.sort(key=lambda x: x[1], reverse=True)

        return ranked

    def choose_next_subject(self):
        ranked = self.rank_subjects()
        return ranked[0]
    