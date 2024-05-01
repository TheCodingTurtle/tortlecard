import math

output_folder = ''

output = []

for i in range(8192):
    output.append(hex(round(math.sqrt(i))))


with open(output_folder, 'w') as f:
    for e in output:
        f.write(e + "\n")
    print(output)
    f.close()



