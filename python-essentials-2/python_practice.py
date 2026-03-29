class StudentScores:
    def __init__(self, scores):
        self.scores = scores

    def highest_last_two(self):
        try:
            # Using negative indexing to access the last two elements
            last_score = self.scores[-1]
            second_last_score = self.scores[-2]
            
            # Finding the highest of the two
            highest = max(last_score, second_last_score)
            print(f"Highest score among last two is: {highest}")
            
        except IndexError:
            # Handled if the list has fewer than 2 elements
            print("Not enough scores to find highest value")

    def last_three_avg(self):
        try:
            # Using negative indexing to access the last three elements
            last_three_scores = self.scores[-3:]
            
            # Calculating the average of the last three scores
            average = sum(last_three_scores) / len(last_three_scores)
            print(f"Average of the last three scores is: {average}")
            
        except IndexError:
            # Handled if the list has fewer than 3 elements
            print("Not enough scores to calculate average")

# Example Usage:
scores_list = [45, 67, 89, 72]
student = StudentScores(scores_list)
student.highest_last_two()
student.last_three_avg()