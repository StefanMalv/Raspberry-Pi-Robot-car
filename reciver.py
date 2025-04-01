# Protokoll for rasberry pi

farger = {
    "Blå": 1,
    "Rød": 2,
    "Grønn": 3,
    "Gul": 4,
}

retninger = {
    "Fram": 1,
    "Høyre": 2,
    "Venstre": 3,
}

def reciver(farge, retning, distanse):
    position = []
    
    for i, y in farger.items():
        if farge == i:
            position.append(y)
    
    for i, y in retninger.items():
        if retning == i:
            position.append(y)
            
    if distanse > 30:
        position.append("far")
    
    else:
        position.append("close")
    
    return position


def input_():
    color = input("What color do you see?: ")
    retning = input("What direction are you looking?:  ")
    distance = int(input("How far is it?: "))

    inputs = reciver(color, retning, distance)
    print(inputs)
    return inputs
