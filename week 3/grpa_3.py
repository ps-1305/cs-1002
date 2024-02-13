"""
Problem statement:
Manhattan distance
"""
commands = []
while True:
    x = input()
    if x != "STOP":
        commands.append(x)
    else:
        break

x , y = 0 , 0
for i in range(1, len(commands)):
    if commands[i] == "UP": y += 1
    elif commands[i] == "DOWN": y -= 1
    elif commands[i] == "RIGHT": x += 1
    else: x -= 1

print(abs(x) + abs(y))

#code by 23f202268
