students_score = {150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000}

highest_score = max(students_score)

print("The highest score in the class is:", highest_score)

high = 0
for score in students_score:
    if score > high:
        high = score

print("The highest score in the class is:", high)