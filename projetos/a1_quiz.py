print("Seja bem vindo ao jogo de adivinhação!")
answer_user = input("Quer começar? (S/N): ")

if answer_user != "s":
    quit()

score = 0

print("Vamos começar!")
print("Quem desenvolveu GTA? "
      "\n (A) Rockstar Games "
      "\n (B) Rockstar Studios "
      "\n (C) Rockstar Development "
      "\n (D) Rockstar Entertainment ")
anser_1 = input("Resposta: ")

if anser_1 == "A":
    print("Resposta correta!")
    score += 1
else:
    print("Resposta errada!")

print("--------------------")
print("score: ", score)
print("--------------------")

print("Quem é o protagônista de GTA San Andreas? "
      "\n (A) CJAY "
      "\n (B) Michael "
      "\n (C) Franklin "
      "\n (D) Trevor ")
anser_2 = input("Resposta: ")

if (anser_2 == "A"):
    print("Resposta correta!")
    score += 1
else:
    print("Resposta errada!")

print("--------------------")
print("score: ", score)
print("--------------------")
print(f"Quiz Finalizado! SCORE: {Score}")