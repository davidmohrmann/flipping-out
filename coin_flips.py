import math
import random


heads = 0
tails = 1


def flip_coin():
    return random.randint(0, 1)


def flipping_coin(number_of_flips=2 ** 16):  # =65536
    heads = 0
    tails = 0
    trial_count = 0  # increments starting at 2^0, 2^1, etc...
    results_list = []
    while trial_count <= 2 ** 16:
            if flip_coin():
                heads += 1
            else:
                tails += 1
            trial_count += 1
            #  log has an inverse relationship with exponents
            if math.log2(trial_count) % 1 == 0:
                results_list.append((heads, tails))

    return (results_list)

results_list = flipping_coin()

print("Each Tuple represents a 'Trial'. There were 16 trials altogether.")
print("The first number is the number of times the coin came up as Heads.")
print("The second number is the number of times the coin came up Tails.")
print(results_list)


# difference (use absolute value)
def get_difference_list(results_list):
    difference_list = [math.fabs(x[0]-x[1]) for x in results_list]
    print(difference_list)

difference_list = get_difference_list(results_list)

# ratio of heads to tails (or should it be heads: heads + tails?)
# def get_ratio(results_list):
#     ratio_dict = {}
#     for x in results_list:
