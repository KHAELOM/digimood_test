"""
You are taking your fleet, made up of an equal number of offensive and support ships, to
your assigned deployment point when you are ambushed by enemy forces. Your defense
tactic is to pair each support ship with one offensive ship in order to share the offensive
ship's shield.
Assuming a two-dimensional layout with a maximum size of 100x100, write some code that
is able to represent your fleet location data and populate it with your 50 ships in random
positions. Then, implement an algorithm that generates 25 pairs of ships, and issues the
commands to make the pairs occupy adjacent positions on the grid by moving one or both
ships. Your vessels need to assume this defensive formation as quickly as possible, so you
will need to find an algorithm that gives an optimized set of pairs, but that is also quick to
generate them.

"""


import random
import math
import matplotlib.pyplot as plt
from Vessel import SupportCraft, OffensiveCraft


# Step 1: Create and Position the Fleet
fleet = []

for _ in range(25):
    x = random.randint(0, 99)
    y = random.randint(0, 99)
    support_ship = SupportCraft(f"Support{_}", 100, (x, y), random.choice(SupportCraft.SUPPORT_TYPES))
    x = random.randint(0, 99)
    y = random.randint(0, 99)
    offensive_type = random.choice(list(OffensiveCraft.VALID_TYPES.keys()))
    offensive_ship = OffensiveCraft(f"Offensive{_}", 100, (x, y), offensive_type)
    fleet.append(support_ship)
    fleet.append(offensive_ship)

# Step 2: Generate Pairing and Positioning
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

pairs = []
support_ships = [ship for ship in fleet if isinstance(ship, SupportCraft)]
offensive_ships = [ship for ship in fleet if isinstance(ship, OffensiveCraft)]

for offensive_ship in offensive_ships:
    nearest_support_ship = min(support_ships, key=lambda x: euclidean_distance(offensive_ship.coordinates, x.coordinates))
    pairs.append((offensive_ship, nearest_support_ship))

# Step 3: Move Ships into Defensive Formation and Create Visualization
plt.figure(figsize=(10, 10))

for offensive_ship, support_ship in pairs:
    midpoint = ((offensive_ship.coordinates[0] + support_ship.coordinates[0]) / 2,
                (offensive_ship.coordinates[1] + support_ship.coordinates[1]) / 2)
    offensive_ship.move(midpoint)
    support_ship.move(midpoint)

    plt.plot([offensive_ship.coordinates[0], support_ship.coordinates[0]],
             [offensive_ship.coordinates[1], support_ship.coordinates[1]], 'bo-')

    plt.text(offensive_ship.coordinates[0], offensive_ship.coordinates[1], offensive_ship.name, fontsize=8)
    plt.text(support_ship.coordinates[0], support_ship.coordinates[1], support_ship.name, fontsize=8)

plt.xlim(0, 100)
plt.ylim(0, 100)
plt.gca().invert_yaxis()  # Invert Y-axis to match the coordinate system
plt.title("Fleet Defensive Formation")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.grid()
plt.show()

