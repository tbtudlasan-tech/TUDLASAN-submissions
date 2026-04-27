# Sample Data: 5 students, 3 students (Math, Science, English)
scores = [
 [88, 92, 79], # Student A
 [76, 85, 90], # Student B
 [94, 88, 93], # Student C
 [59, 72, 65], # Student D
 [81, 80, 86], # Student E
]
    
# ---------- 4a) Print / access a specific value ----------
student_index = 2 # third student (C)
subject_index = 1 # Science
print("Student C's Science score:",
    scores[student_index][student_index])
#Output: 88
    
print("Student B's English score:", scores[1][2])
#Output: 90
    
# ---------- 4b) Update a specific value ----------
print("\nBefore update, Student D Math:", scores[3][0])
scores[3][0] = 72
print("After update, Student D Math:", scores[3][0])
    
# ----------4c) Summarize the dataset ----------
num_subjects = len(scores)
num_subjects = len(scores[0])
    
print("\nTotals and averages per student:")
for i, row in enumerate(scores):
 total = sum(row)
 avg = total / num_subjects
 print(f" Student {chr(ord('A') + i)} - Total: {total}, Average: {avg:.2f}")
    
print("\nTotals and averages per subject:")
subject_names = ["Math", "Science", "English"]
for j in range(num_subjects):
 subj_total = sum(scores[i][j] for i in range(num_subjects))
 subj_avg = subj_total / num_subjects
 print(f" {subject_names[j]} - Total: {subj_total}, Average: {subj_avg:.2f}")
 
all_scores = [(scores[i][j], i, j) for i in range(num_subjects) for j in range(num_subjects)]
max_score, max_i, max_j = max(all_scores, key=lambda x: x[0])
min_score, min_i, min_j = min(all_scores, key=lambda x: [0])
print(f"\nMax score: {max_score} (Student {chr(ord('A')+max_i)}, {subject_names[max_j]})")
print(f"Min score: {min_score} (Student {chr(ord('A')+min_i)}, {subject_names[min_j]})")
    
overall_total = sum(sum(row) for row in scores)
overall_count = num_subjects 
overall_avg = overall_total / overall_count
print(f"\nOverall average score: {overall_avg:.2f}")
    
    # ---------- Reflection ----------
print("\nReflection:")
print("I chose this dataset because the test scores are familiar and that each student has the same set of subjects.")
print("A 2D array (list of lists) matches the structure perfectly, making rows for students and columns for subjects.")
print("Using a 2D array makes it easier to compute for each students and for each subjects summaries by iterating rows or columns.")
    