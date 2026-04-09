# ============================================================
# Monty Hall Problem — Monte Carlo Simulation
# Engineering Mathematics Assignment
# ============================================================

import random

def monty_hall_simulation(num_trials=100000):
    """Simulate the Monty Hall problem for a given number of trials.
    Returns win rates for both staying and switching strategies."""

    stay_wins = 0
    switch_wins = 0
    doors = [1, 2, 3]

    for _ in range(num_trials):

        # Step 1: Place the car behind a random door
        car_door = random.choice(doors)

        # Step 2: Contestant picks a door at random
        player_choice = random.choice(doors)

        # Step 3: Host opens a goat door (not player's, not car's)
        possible_opens = [d for d in doors if d != player_choice and d != car_door]
        monty_opens = random.choice(possible_opens)

        # Step 4: Identify the switch door
        switch_door = [d for d in doors if d != player_choice and d != monty_opens][0]

        # Step 5: Evaluate both strategies
        if player_choice == car_door:
            stay_wins += 1

        if switch_door == car_door:
            switch_wins += 1

    stay_rate = stay_wins / num_trials
    switch_rate = switch_wins / num_trials

    return stay_rate, switch_rate


# ── Run the simulation ─────────────────────────────────────────

N = 100000
stay_rate, switch_rate = monty_hall_simulation(N)

print('=' * 50)
print(f' Monty Hall Simulation (N = {N:,})')
print('=' * 50)
print(f' Stay win rate   : {stay_rate:.4f} (theory = 0.3333)')
print(f' Switch win rate : {switch_rate:.4f} (theory = 0.6667)')
print('=' * 50)