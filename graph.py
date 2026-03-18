import matplotlib.pyplot as plt

def show_priority_graph(ranked_subjects):

    subjects = [item[0] for item in ranked_subjects]
    scores = [item[1] for item in ranked_subjects]

    plt.bar(subjects, scores)

    plt.title("Subject Priority Scores")
    plt.xlabel("Subjects")
    plt.ylabel("Priority Score")

    plt.show()