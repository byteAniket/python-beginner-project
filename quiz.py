# -------------------------> This is a simple quiz game <-------------------------
def quiz():
    print("Welcome to the quiz game!")
    score = 0

    # Question 1
    answer1 = input("What is the capital of France? ")
    if answer1.lower() == "paris":
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is Paris.")

    # Question 2
    answer2 = input("What is the largest planet in our solar system? ")
    if answer2.lower() == "jupiter":
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is Jupiter.")

    # Question 3
    answer3 = input("Who wrote 'To Kill a Mockingbird'? ")
    if answer3.lower() == "harper lee":
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is Harper Lee.")

    # Final Score
    print(f"Your final score is: {score}/3")