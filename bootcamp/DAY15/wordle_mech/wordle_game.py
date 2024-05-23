def feedback(guess: str, correct_answer: str) -> dict:
    feedback = {}
    for i in range(len(guess)):
        if guess[i] == correct_answer[i]:
            feedback[guess[i]] = "Green"
        elif guess[i] in correct_answer:
            feedback[guess[i]] = "Yellow"
        else:
            feedback[guess[i]] = "Red"
    return feedback

print(feedback("GLORY", "GLORY"))
print(feedback("GRACE", "FLARE"))
