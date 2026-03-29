# example input
""" [
  {'name': 'Alice', 'experience_years': 5, 'skills': ['Python', 'SQL'], 'has_degree': True},
  {'name': 'Bob', 'experience_years': -1, 'skills': ['Java'], 'has_degree': False},
  {'name': 'Carol', 'experience_years': 3, 'skills': [], 'has_degree': False},
  {'name': 'Dave', 'experience_years': 7, 'skills': ['Python', 'ML', 'SQL'], 'has_degree': False},
] """


input_list =  [
  {'name': 'Alice', 'experience_years': 5, 'skills': ['Python', 'SQL'], 'has_degree': True},
  {'name': 'Bob', 'experience_years': -1, 'skills': ['Java'], 'has_degree': False},
  {'name': 'Carol', 'experience_years': 3, 'skills': [], 'has_degree': False},
  {'name': 'Dave', 'experience_years': 7, 'skills': ['Python', 'ML', 'SQL'], 'has_degree': False},
] 


final_list = []
def validate_and_score_resumes(input_list):
    for list_data in input_list:
        skills_cnt = len(list_data.get("skills"))
        if list_data.get("experience_years") < 0 or list_data.get("name") :
            input_list.remove(list_data) 


    for final_data in input_list:
        base_score = final_data.get("experience_years") * 10
        base_score = base_score + ( 5 * len(list_data.get("skills")))
        if final_data.get("has_degree") == True:
            base_score = base_score + 20
        
        data = {final_data.get("name") : base_score }
        final_list.append(data)

    print (final_list)


validate_and_score_resumes(input_list)