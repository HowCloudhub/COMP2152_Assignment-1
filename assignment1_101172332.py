"""
Author: <Munir Howlader>
Assignment: #1
"""

# Step b: Create 4 variables
# Created a variable called gym_member and then assigned
gym_member = "Alex the Malex"
# a string object called Alex the Malex
preferred_weight_kg = 20.5  # Created a varible called preferred_weight_kg and assigned
# assigned an float object 20.5
highest_reps = 25  # Created a variable called highest_reps and assinged an integer
# object 25 to it.
membership_active = True  # Created a variable called membership_active and assigned a
# bollean object True to it.

# Step c: Create a dictionary named workout_stats

# Created a dictionary called workout_stats. Within it, the keys are string objects
# and values are tuples of time spent on different workout activities.
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (31, 40, 25),
    "Taylor": (30, 44, 50)
}

print(workout_stats.items())

# Step d: Calculate total workout minutes using a loop and add to dictionary

# create an empty object of the dict() class
totals = {}

# for each name and time (Key Value pair in work_stats)--
for name, times in workout_stats.items():
    # add a new key valye pair in dictionary called total.
    # The key(of tatals) is called "name (keys in work_stats)+_Total" and value(of total)
    # is the sum of all vlaue items inside the dictionary called work_stats
    totals[name + "_Total"] = sum(times)

# Merged the dictionary called totals to the dictionary called work_stats
workout_stats.update(totals)

print(f"Workout stats: {workout_stats.items()}")

# Step e: Create a 2D nested list called workout_list
# workout_list is a 2-dimensional list where each row represents a friend and each column represents an activity
# created a new list containing only the tuples values in workout_stats
workout_list = [list(times)
                for times in workout_stats.values()
                if isinstance(times, tuple)]

print(workout_list)

# Step f: Slice the workout_list
# create new list with Yoga and Running times.
yoga_runnig = [items[:2] for items in workout_list]
print("Yoga and running for all friends", yoga_runnig)

# create new list with weightlifting times for the last two friends
weight_lifting = [items[2] for items in workout_list[-2:]]
print("Weightlifting times for last two friends:", weight_lifting)


# Step g: Check if any friend's total >= 120

# using if statement to get key (minus the _Total portion) and
# values more than 120
for key, value in workout_stats.items():
    if key.endswith("_Total"):
        friend_name = key[:-6]
        if value >= 120:
            print(f"Great job staying active, {friend_name}")

# Step h: User input to look up a friend

# promt the user the a friend name and store it the variable friend_input
friend_input = input("Enter a freind's name: ").strip()

# check the name exists in workout_stats and ensure it's value is a tuple ( not the _total value)
if friend_input in workout_stats and isinstance(workout_stats[friend_input], tuple):
    # Create a new variable 'activities' that references the friend's tuple of workout times
    activities = workout_stats[friend_input]
    # Create a key name to access the friend's total workout time
    total_key = friend_input + "_Total"
    # Retrieve the total workout minutes using the constructed key
    total_minute = workout_stats.get(total_key, 0)

    print(f"\nWorkout details for {friend_input}:")
    print(f"Yoga: {activities[0]} minutes")
    print(f"Running: {activities[1]} minutes")
    print(f"Weightlifting: {activities[2]} minutes")
    print(f"Total workout time is {total_minute} minutes")

else:
    print(f"Friend {friend_input} is not found in records")

# Step i: Friend with highest and lowest total workout minutes


# First I will create a new dictionary containing the total numbers only

total_only = {key: value for key, value in workout_stats.items()
              if key.endswith("_Total")}
print(total_only.keys())

# use the max()method to find the largest item based on its vlues.
highest_key = max(total_only, key=total_only.get)
highest_friend = highest_key[:-6]

# use the min()method to find the largest item based on its vlues.
lowest_key = min(total_only, key=total_only.get)
lowest_friend = lowest_key[:-6]

print(
    f"Highest total workout minutes: {highest_friend} ({total_only[highest_key]} minutes)")
print(
    f"Lowest total workout minutes: {lowest_friend} ({total_only[lowest_key]} minutes)")
