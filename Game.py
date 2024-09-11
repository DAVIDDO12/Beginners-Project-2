import random
def foresttreasurehunt():
    print("Welcome to the Forest Treasure Hunt!")
    print("You are being randomly generated into one of two scenarios...")
    scenario = random.choice(["forest", "quiz"])
    if scenario == "forest":
        print("You have entered a forest and must play a series of games to survive.")
        fruits = ["banana", "apple", "strawberry", "blueberry", "orange"]
        guessedfruits = []
        while set(guessedfruits) != set(fruits):
            guessedfruits = input("Guess five fruits: ").split()
            correctfruits = [fruit for fruit in guessedfruits if fruit in fruits]
            if set(correctfruits) == set(fruits):
                print("You guessed all the fruits correctly! You may pass.")
            else:
                print("Correct fruits so far: " + str(correctfruits) + ". Try again.")
        height = int(input("Enter your height in cm to cross the river: "))
        if height <= 160:
            print("You are too short and drown. Game over.")
            return
        elif height > 180:
            print("You are too tall and the tiger spots you. Game over.")
            return
        else:
            print("You crossed the river safely.")
        attempts = 10
        password = [1, 2, 3, 4]  
        while attempts > 0:
            try:
                guess = list(map(int, input("Enter a 4-digit password: ")))
                if len(guess) != 4:
                    print("Please enter exactly 4 digits.")
                    continue
            except ValueError:
                print("Invalid input. Please enter digits only.")
                continue
            correctnumbers = sum([1 for i in range(4) if guess[i] == password[i]])
            if correctnumbers == 4:
                print("You guessed the password correctly! You win!")
                retry = input("Would you like to try the other game? (yes/no): ").lower()
                if retry == "yes":
                    pythonquiz()
                else:
                    print("Thank you for playing!")
                    break
            else:
                print(str(correctnumbers) + " numbers are correct. Try again.")
                attempts -= 1
            if attempts == 0:
                print("You ran out of attempts. Game over.")
    elif scenario == "quiz":
        pythonquiz()

def pythonquiz():
    print("Welcome to the Python Quiz!")
    questions = [
        {"question": "What is the output of print(2 ** 3)?", "options": ["6", "8", "9", "12"], "answer": "8"},
        {"question": "Which of the following is a mutable data type?", "options": ["tuple", "string", "list", "int"], "answer": "list"},
        {"question": "What does the 'len' function do?", "options": ["Returns the length of an object", "Returns the type of an object", "Returns the value of an object", "Returns the id of an object"], "answer": "Returns the length of an object"},
        {"question": "Which keyword is used to define a function in Python?", "options": ["func", "def", "function", "define"], "answer": "def"},
        {"question": "What is the correct file extension for Python files?", "options": [".py", ".python", ".pt", ".pyt"], "answer": ".py"},
        {"question": "How do you insert COMMENTS in Python code?", "options": ["//", "/*", "#", "<!--"], "answer": "#"}
    ]
    correctanswers = 0
    for q in questions:
        print(q["question"])
        for i, option in enumerate(q["options"], 1):
            print(str(i) + ". " + option)
        answer = input("Your answer: ")
        if q["options"][int(answer) - 1] == q["answer"]:
            correctanswers += 1
    incorrectanswers = len(questions) - correctanswers
    percentage = (correctanswers / len(questions)) * 100
    print("\nYou answered " + str(correctanswers) + " questions correctly.")
    print("You answered " + str(incorrectanswers) + " questions incorrectly.")
    print("Your score: " + str(percentage) + "%")
    if correctanswers == 6:
        print("Congratulations! You got all the answers right!")
    elif correctanswers >= 4:
        print("Great job! You did well.")
    elif correctanswers >= 2:
        print("Not bad, but you can do better.")
    else:
        print("You need to brush up on your Python knowledge.")
    retry = input("Would you like to try the other game? (yes/no): ").lower()
    if retry == "yes":
        foresttreasurehunt()
    else:
        print("Thank you for playing!")
foresttreasurehunt()
