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
    for k, v in count.items():
        prob_dict[k] = v / total
    return prob_dict

def dice_generate():
    die_a = []
    for _ in range(5):
        die_a.append(random.randint(2, 4))
    die_a.append(1)

    standard_die = [1, 2, 3, 4, 5, 6]
    standard_probs = calculate_sum_probabilities(standard_die, standard_die)
    
    max_b = 12 - max(die_a)
    die_b = []
    for _ in range(4):
        die_b.append(random.randint(2, max_b-1))
    die_b.append(1)
    die_b.append(max_b)
    
    return die_a, die_b

def dice_are_valid(die_a, die_b, standard_probs, tolerance=1e-6):
    special_probs = calculate_sum_probabilities(die_a, die_b)
    for k in range(2, 13):
        std_prob = standard_probs.get(k, 0)
        spc_prob = special_probs.get(k, 0)
        if abs(std_prob - spc_prob) >= tolerance:
            return False
    return True

standard_die = [1, 2, 3, 4, 5, 6]
standard_probs = calculate_sum_probabilities(standard_die, standard_die)

attempts = 0
max_attempts = 10000

found_valid_dice = False
while attempts < max_attempts:
    die_a, die_b = dice_generate()
    if dice_are_valid(die_a, die_b, standard_probs):
        print("Found valid dice after", attempts + 1, "attempts:")
        print("Die A:", die_a)
        print("Die B:", die_b)
        
        special_probs = calculate_sum_probabilities(die_a, die_b)
        print("\nSum | Standard | Special")
        print("----|----------|--------")
        for sum_value in range(2, 13):
            std_prob = standard_probs.get(sum_value, 0)
            spc_prob = special_probs.get(sum_value, 0)
            print(f"{sum_value:3d} | {std_prob:.4f}   | {spc_prob:.4f}")
        
        found_valid_dice = True
        break
    attempts += 1

if not found_valid_dice:
    print("Could not find valid dice within the maximum number of attempts.")
