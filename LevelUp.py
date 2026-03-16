
experience = 10
threshold = 15
reward = 4

new_lvl = experience + reward
is_promoted = new_lvl >= threshold
result = is_promoted
print("Reached a new level?", result)
