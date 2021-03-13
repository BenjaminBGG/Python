#! python3

from random import randint
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

EQ_VOLS = 1000 # number of civilized locations
MAX_CIVS = 5000 # max number of civs
RUNS = 1000 # number of models/civ
STEP_SIZE = 100 # civ count step size

x = [] # x val for poly fit
y = [] # y val for poly fit

for civs in range(2, MAX_CIVS + 2, STEP_SIZE):
    civs_per_vol = civs/EQ_VOLS
    num_single_civs = 0
    for trial in range(RUNS):
        loc = [] # vols containing civ
        while len(loc) < civs:
            location = randint(1, EQ_VOLS)
            loc.append(location)
        overlap_count = Counter(loc)
        overlap_rollup = Counter(overlap_count.values())
        num_single_civs += overlap_rollup[1]

p = 1 - (num_single_civs/(civs*RUNS))

print("{:.4f}  {:.4f}".format(civs_per_vol, p))
x.append(civs_per_vol)
y.append(p)
