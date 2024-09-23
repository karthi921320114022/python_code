questions=("How many planets in Solar system?",
           "which animal lays largest eag?",
           "Which is the hottest planet in Solar system?",
           "which is the largest continent in Earth?",
           "What is the most abontant gas in the Earth's atmosphere?")

options=(("A.6 ", "B.8 " , "C.9" , "D.10 "),
         ("A.Chiicken ", "B.Osctrich " , "C.whale " , "D.Elephsnt "),
         ("A.Mercury", "B.Earth " , "C.Venus " , "D. Mars "),
         ("A.Africa ", "B.Asia" , "C.Europe " , "D.Antartica "),
         ("A.Oxygen ", "B.Helium" , "C.Carbon-Dioxide " , "D.Nitrogen "))

answers=("B","B","C","A","D")
guesses=[]
question_num=0
score=0

for question in questions:
    print("-----------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess=input("Enter your answer (A,B,C,D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("CORRECT!")
        score+=1
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer ")
    question_num+=1

percentage=(score/len(questions))*100
    
print("--------------------------------")
print("-------------RESULT-------------")
print("--------------------------------")

print(f"The correct answers{answers}")
print(f"Your guesses       {guesses}")
print("--------------------------------")
print(f"Your score {percentage}%")
print("--------------------------------")