#make sure to replace this with the location of the .hex file you want the A points to be outputed to.
output_folderA = ''

#make sure to replace this with the location of the .hex file you want the B points to be outputed to.
output_folderB = ''


#pyramid 1
#v = [[4,6,0],[20,6,0],[4,54,0],[20,54,0],[48,30,12]]
#lines = [v[0],v[1],v[0],v[2],v[1],v[3],v[2],v[3],v[4],v[0],v[4],v[1],v[4],v[3],v[4],v[2]]

#pyramid 2
#v = [[32,32,0],[8,24,0],[56,24,0],[32,22,32],[32,8,16]]
#lines = [v[2],v[0],v[1],v[0],v[3],v[1],v[3],v[2],v[4],v[0],v[4],v[1],v[4],v[3],v[4],v[2]]

#cube 1
v = [[32,44,0],[8,36,0],[56,36,0],[32,34,32],[32,14,0],[8,6,0],[56,6,0],[32,2,32]]
lines = [v[2],v[0],v[1],v[0],v[3],v[1],v[3],v[2],v[6],v[4],v[5],v[4],v[7],v[5],v[7],v[6],
         v[0],v[4],v[1],v[5],v[2],v[6],v[3],v[7]]

program = []

side = "B"

num = 1

for o in lines:
    eee = str(o[0]) + "-" + str(o[1]) + "-" + str(o[2])
    if num >= 2:
        program.append(eee)
        program.append("0-0-0")
        program.append("0-0-0")
        num = 1
    else:
        program.append(eee)
        num += 1


        


outputA = []
outputB = []
    
for i in program:
    nums = []
    e = i.split("-")
    for k in e:
        l = bin(int(k))[2:]
        if len(l) < 16:
            l = "0"*(16-len(l)) + l
        nums.append(l)
    x = nums[0]
    y = nums[1]
    z = nums[2]
    if side == "B":
        side = "A"
        outputA.append(hex(int(str(z)+str(y)+str(x), 2)))
    elif side == "A":
        side = "B"
        outputB.append(hex(int(str(z)+str(y)+str(x), 2)))


print(program)
    

with open(output_folderA, 'w') as f:
    for e in outputA:
        f.write(e + "\n")
    print(outputA)
    f.close()

with open(output_folderB, 'w') as f:
    for e in outputB:
        f.write(e + "\n")
    print(outputB)
    f.close()


    


