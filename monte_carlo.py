#!/usr/bin/env python3

#Write a Python script to calculate the probability of a trader being profitable after 100 trades, given a
#40% win rate with winners 2x the size of losers. Include Monte Carlo simulation with 10,000 iterations and
#visualize the distribution of outcomes. Output should include both the probability of profitability and
#expected value.

import random
import matplotlib.pyplot as plt


def flip_biased_coin():
    return random.random() < 0.4

def run():
    capital = [10000]
    for each in range(100):
        coinflip = flip_biased_coin()
        if coinflip == True:
            capital.append(capital[-1] * 1.1)
        elif coinflip == False:
            capital.append(capital[-1] * 0.95)

    return capital


runs = [run() for each in range(10000)]

count = sum(1 for lst in runs if lst[-1] > 10000)

print(f"Profitability Probability: {count/len(runs)}")
expectation = 0.4 * 100 - 0.6 * 50
print(expectation)
for each in runs:
    plt.plot(each)

#plt.show()
plt.savefig("monte_carlo.png")
