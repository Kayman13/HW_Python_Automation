
experience = 10
threshold = 15
reward = 10

new_lvl = experience + reward
is_promoted = new_lvl >= threshold
if is_promoted:
    result = True
else:
    result = False
print("Reached a new level?", result)

