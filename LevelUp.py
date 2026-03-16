
experience = 10
threshold = 15
reward = 6

new_lvl = experience + reward
is_promoted = new_lvl >= threshold
print("Reached a new level?", is_promoted)
