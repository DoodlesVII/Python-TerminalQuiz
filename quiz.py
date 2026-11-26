QUESTIONS_FILE = "questions.txt"
HIGHSCORES_FILE = "highscores.txt"

def load_questions(filename):
    questionAnswer = []
    with open(filename, "r") as qs:
        for x in qs:
            parts = x.strip().split("|")
            if len(parts) == 2:
                questionAnswer.append(parts)
    return questionAnswer
            
def runQuiz(questions):
    score = 0
    for question, answer in questions:
        print(question)
        userAnswer = input()
        if userAnswer.strip().lower() == answer.strip().lower():
            print("Correct!")
            score += 1   
        else:
            print("Incorrect.")
            yN = input("Would you like to see the correct answer? Enter Y or N: ")
            if yN.strip().lower() == "y":
                print("Correct answer: " + answer)
    print("Final score: " + str(score) + "/" + str(len(questions)))
    return score

def saveHighscore(filename2, playername, score):
    with open(filename2, "a") as f:
        f.write(playername + "|" + str(score) + "\n")

def showHighscores(filename2):
    try:
        with open(filename2, "r") as pu:
            for t in pu:   
                name, score = t.strip().split("|")
                print(name + ": " + score)
    except FileNotFoundError:
        print("No high scores yet!")

def main():
    theQuiz = load_questions(QUESTIONS_FILE)
    name = input("Enter your name!").strip() or "Anonymous"
    resultsQuiz = runQuiz(theQuiz)
    saveHighscore(HIGHSCORES_FILE, name, resultsQuiz)
    showHighscores(HIGHSCORES_FILE)

if __name__ == "__main__":
    main()

    

            