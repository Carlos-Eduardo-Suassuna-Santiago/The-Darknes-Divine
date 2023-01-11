import personagem

def xp_check(personagem):
    if personagem.LV == 1 and personagem.xp == 10:
        personagem.LV += 1
    elif personagem.LV == 2 and personagem.xp == 25:
        personagem.LV += 1
    elif personagem.LV == 3 and personagem.xp == 50:
        personagem.LV += 1
    elif personagem.LV == 4 and personagem.xp == 100:
        personagem.LV += 1
    elif personagem.LV == 5 and personagem.xp == 200:
        personagem.LV += 1
    elif personagem.LV == 6 and personagem.xp == 500:
        personagem.LV += 1
    elif personagem.LV == 7 and personagem.xp == 1000:
        personagem.LV += 1
    elif personagem.LV == 8 and personagem.xp == 2000:
        personagem.LV += 1
    else:
        print("Voce venceu")

        
        
    