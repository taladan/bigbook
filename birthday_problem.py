#! bin/python
#
# birthday_problem.py
#
"""
This program runs a monte carlo style simulation of #{SIMULATIONS} of 
the [Birthday Problem/Paradox](https://en.wikipedia.org/wiki/Birthday_problem).

The original code is by Al Sweigart, from his 
[Big Book of Small Python Projects](https://inventwithpython.com/bigbookpython/project2.html)
"""

import pyinputplus as pyip
import datetime
import random

# CONSTANTS
SIMULATIONS = 100000


def generate_bdays(bdays: int) -> list:
    """
    Generate {bdays} number of birthday datetime objects
    returns a list of datetime objects
    """
    start_day = datetime.datetime(2022, 1, 1, 0, 0)
    days = []
    for day in range(bdays):
        day = datetime.timedelta(random.randint(0, 364))
        days.append(start_day + day)
    return days


def find_matching_bdays(day_list: list) -> list:
    """
    Return a list of matching days
    """
    return [day for day in day_list if day_list.count(day) > 1]


def format_days(datetime_list: list) -> list:
    """
    Return list of string formatted datetime objects in "Mon day" format
    """
    return [day.strftime("%b %d") for day in datetime_list]


def list_format(lst: list) -> str:
    """
    Return a list of strings formatted such that each item is separated
    by a comma with the second to last item in the list having ', and' appended to it.
    Example:

    foo, bar, baz, bang, and bam
    """
    lst.sort()
    response = ""
    for index, value in enumerate(lst):
        if index == 0:
            response = value
        elif index < len(lst) - 2:
            response = f"{response}, {value}"
        elif index == len(lst) - 2:
            response = f"{response}, {value}, and"
        else:
            response = f"{response} {value}"
    return response


def run_simulation(sims, num_of_bdays):
    """
    Run {sims} number of simulations and return a
    total count of times a simulation had matching days
    """
    counter = 0
    matches = 0
    while counter < sims:
        if counter % 10000 == 0:
            print(f"{counter} simulations run.  {SIMULATIONS - counter} remaining.")
        bdays = generate_bdays(num_of_bdays)
        if len(find_matching_bdays(bdays)) > 0:
            matches += 1
        counter += 1
    return matches


num_of_bdays = pyip.inputInt(
    "How many birthdays shall I generate? (Max 100)", min=1, max=100
)


# Generate and print inital run of birthdays and matches
birthdays_generated = sorted(generate_bdays(num_of_bdays))
formatted_days = format_days(birthdays_generated)
 # Need a unique set to print
 matching_birthdays = set(
    find_matching_bdays(birthdays_generated)
) 

print(f"Here are {num_of_bdays} birthdays.")
print(", ".join(formatted_days))
if len(matching_birthdays) > 0:  # Only print matches if we have matches
    print("\n")
    print(
        f" In this simulation multiple people have matching birthdays on {list_format(format_days(matching_birthdays))}"
    )
print("\n")

# Simulation run section
print(f"Running simulation of {SIMULATIONS} birthdays.")
total_matches = run_simulation(SIMULATIONS, num_of_bdays)
print(f" There were [{total_matches}] matches in this simulation")
print(
    f"That means there is a probability of {round(total_matches/SIMULATIONS * 100, 2)}% of a group of {num_of_bdays} people having a matching birthday."
)
print("\nDone.")
