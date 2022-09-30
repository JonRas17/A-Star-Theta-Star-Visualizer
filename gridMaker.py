import random

file = open("Grid.txt", "w")
sx = str(random.randint(1,101))
sy = str(random.randint(1,51))

gx = str(random.randint(1,101))
gy = str(random.randint(1,51))

file.write(sx + " " + sy + "\n")
file.write(gx + " " + gy + "\n")
file.write("100 50 \n")
for i in range(1,101):
    for j in range(1,51):
        ge = random.uniform(0,1)
        fill = 0 if ge > 0.1 else 1
        file.write(str(i) + " " +str(j) + " " + str(fill) + " " + "\n")