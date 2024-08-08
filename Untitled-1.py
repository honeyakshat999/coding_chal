import random
def dice_generate():
    die_a = []
    for i in range(2):
        print(i)
        die_a.append(random.randint(2, 4))
    for i in range(1,5):    
        die_a.append(i)

    print(die_a)

dice_generate()