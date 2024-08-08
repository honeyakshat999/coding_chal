import itertools
from collections import Counter
import random

def calculate_sum_probabilities(die1, die2):
    sums = []
    for a, b in itertools.product(die1, die2):
        sums.append(a + b)
    count = Counter(sums)
    total = len(sums)
    prob_dict = {}
    for final_sum, no_of_times in count.items():
        prob_dict[final_sum] = no_of_times / total
    return prob_dict

def dice_generate():
    die_a = []
    for i in range(2):
        die_a.append(random.randint(2, 4))
    for i in range(1,5):    
        die_a.append(i)
    

    standard_die = [1, 2, 3, 4, 5, 6]
    standard_probs = calculate_sum_probabilities(standard_die, standard_die)
    
    max_b = 12 - max(die_a)
    die_b = []
    for _ in range(4):
        die_b.append(random.randint(2, max_b-1))
    die_b.append(1)
    die_b.append(max_b)
    
    return die_a, die_b
def dice_are_valid(die_a, die_b, standard_probs, change=1e-6):
    special_probs = calculate_sum_probabilities(die_a, die_b)
    for k in range(2, 13):
        std_prob = standard_probs.get(k, 0)
        spc_prob = special_probs.get(k, 0)
        if abs(std_prob - spc_prob) >= change:
            return False
    return True
standard_die = [1, 2, 3, 4, 5, 6]
standard_probs = calculate_sum_probabilities(standard_die, standard_die)



found_valid_dice = False
while True:
    die_a, die_b = dice_generate()
    if dice_are_valid(die_a, die_b, standard_probs):
        print("Die A:", die_a)
        print("Die B:", die_b)
        
        found_valid_dice = True
        break


if not found_valid_dice:
    print("Could not find valid dice.")