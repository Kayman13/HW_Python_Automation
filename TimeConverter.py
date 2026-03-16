
time24 = "17:09"

hours_str, minutes = time24.split(":")
hours = int(hours_str)

if hours == 0:
    hours_12 = 12
    period = "a.m."
elif hours < 12:
    hours_12 = hours
    period = "a.m."
elif hours == 12:
    hours_12 = 12
    period = "p.m."
else:
    hours_12 = hours - 12
    period = "p.m."
time12 = f"{hours_12}:{minutes} {period}"
print(time12)
