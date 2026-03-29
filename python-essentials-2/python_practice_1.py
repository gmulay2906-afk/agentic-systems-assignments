class StudentPerformance:
    def __init__(self, scores):
        self.scores = scores


    def score_difference(self):
        try:
            if self.scores is None:
                raise ValueError("No scores available to calculate difference")
            
            last_score = self.scores[-1] if len(self.scores) >= 1 else None
            first_score = self.scores[0] if len(self.scores) >= 1 else None

            print (last_score)
            print (first_score)

            if last_score != None and first_score is not None:
                return abs(last_score - first_score)
            else:
                raise ValueError("Insufficient scores to calculate difference")

        except Exception as e:
            print (f"An error occurred: {e}")
            return None
        
# Example Usage:
scores_list = [45, 67, 89, 72]
student_performance = StudentPerformance(scores_list)  
difference = student_performance.score_difference()
print(f"The difference between the last and first scores is: {difference}")
