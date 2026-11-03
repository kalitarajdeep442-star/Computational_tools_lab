import matplotlib.pyplot as plt
import numpy as np

# Set seed for reproducibility and generate mock data
np.random.seed(42)
num_students = 100

# Synthetic Data: Study hours (normally distributed around 5 hours)
study_hours = np.random.normal(loc=5.0, scale=2.0, size=num_students)
study_hours = np.clip(study_hours, 0, 12) # Ensure realistic hours (0-12)

# Synthetic Data: Exam scores (positively correlated with study hours)
# Base score + (hours * weight) + random noise
exam_scores = 40 + (study_hours * 4.5) + np.random.normal(loc=0, scale=8.0, size=num_students)
exam_scores = np.clip(exam_scores, 0, 100) # Cap at 100

# Create the figure setup
fig = plt.figure(figsize=(14, 10))

# 1. Histogram for Study Hours
ax1 = fig.add_subplot(2, 2, 1)
ax1.hist(study_hours, bins=10, color='purple', alpha=0.7, edgecolor='black')
ax1.set_title('Distribution of Study Hours')
ax1.set_xlabel('Study Hours')
ax1.set_ylabel('Number of Students')

# 2. Histogram for Exam Scores
ax2 = fig.add_subplot(2, 2, 2)
ax2.hist(exam_scores, bins=10, color='teal', alpha=0.7, edgecolor='black')
ax2.set_title('Distribution of Exam Scores')
ax2.set_xlabel('Exam Scores')
ax2.set_ylabel('Number of Students')

# 3. Scatter Plot for Relationship
ax3 = fig.add_subplot(2, 1, 2)
ax3.scatter(study_hours, exam_scores, color='darkorange', alpha=0.8, edgecolors='black')
ax3.set_title('Relationship between Study Hours and Examination Scores')
ax3.set_xlabel('Study Hours')
ax3.set_ylabel('Examination Score (0-100)')
ax3.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
