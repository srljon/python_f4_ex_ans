speeds = [5, 12, 8, 15, 9]
max_speed = 10
i = 0

while i < len(speeds):
    if speeds[i] > max_speed:
        speeds[i] = max_speed
    i += 1

print(speeds)
