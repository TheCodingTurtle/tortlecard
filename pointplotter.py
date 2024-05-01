#make sure to replace this with the location of the .hex file you want the A points to be outputed to.
output_folderA = ''

#make sure to replace this with the location of the .hex file you want the B points to be outputed to.
output_folderB = ''

#make sure to replace this with the location of the .hex file you want the type values to be outputed to.
output_types = ''

vc = 0
cnt = 0
bcnt = 0

v = []
lines = []
types = []

out1 = []
out2 = []

#pyramid 1
#v = [[4,6,0],[20,6,0],[4,54,0],[20,54,0],[48,30,12]]
#lines = [v[0],v[1],v[0],v[2],v[1],v[3],v[2],v[3],v[4],v[0],v[4],v[1],v[4],v[3],v[4],v[2]]

#pyramid 2
#v = [[32,32,0],[8,24,0],[56,24,0],[32,22,32],[32,8,16]]
#lines = [v[2],v[0],v[1],v[0],v[3],v[1],v[3],v[2],v[4],v[0],v[4],v[1],v[4],v[3],v[4],v[2]]

#cube 1
#v = [[32,44,0],[8,36,0],[56,36,0],[32,34,32],[32,14,0],[8,6,0],[56,6,0],[32,2,32]]
#lines = [v[2],v[0],v[1],v[0],v[3],v[1],v[3],v[2],v[6],v[4],v[5],v[4],v[7],v[5],v[7],v[6],
         #v[0],v[4],v[1],v[5],v[2],v[6],v[3],v[7]]

#v = [[5,56,0], [5,56,56], [56,56,0], [56,56,56]]
#lines = [v[0],v[1],v[1],v[3],v[2],v[3],v[2],v[0]]

#room
#v = [[5,5,0],[16,16,35]] WIP
#lines = [v[0], v[1]] WIP

#v = [[0,0,0],[128,128,0]]
#lines = [v[0],v[1]]

def plotLineLow(x0,y0,x1,y1,lis):
    x0 = int(x0)
    y0 = int(y0)
    x1 = int(x1)
    y1 = int(y1)
    dx = x1-x0
    dy = y1-y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    D = (2*dy)-dx
    y = y0

    for x in range(x0,x1):
        lis.append([x,y])
        if D > 0:
            y = y + yi
            D = D + (2*(dy-dx))
        else:
            D = D + 2*dy

def plotLineHigh(x0,y0,x1,y1,lis):
    x0 = int(x0)
    y0 = int(y0)
    x1 = int(x1)
    y1 = int(y1)
    dx = x1-x0
    dy = y1-y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    D = (2*dx)-dy
    x = x0

    for y in range(y0,y1):
        lis.append([x,y])
        if D > 0:
            x = x + xi
            D = D + (2*(dx-dy))
        else:
            D = D + 2*dx

def plotLine(x0,y0,x1,y1,lis):
    if abs(y1-y0) < abs(x1-x0):
        if x0 > x1:
            plotLineLow(x1,y1,x0,y0,lis)
        else:
            plotLineLow(x0,y0,x1,y1,lis)
    else:
        if y0 > y1:
            plotLineHigh(x1,y1,x0,y0,lis)
        else:
            plotLineHigh(x0,y0,x1,y1,lis)

def Line(x0,y0,z0,x1,y1,z1,lis,fov):
    print("A: [" + str(x0) + "," + str(y0) + "," + str(z0) + "]")
    print("B: [" + str(x1) + "," + str(y1) + "," + str(z1) + "]")
    x_zero = (x0*fov)/(fov+z0)
    y_zero = (y0*fov)/(fov+z0)
    x_one = (x1*fov)/(fov+z1)
    y_one = (y1*fov)/(fov+z1)
    plotLine(x_zero,y_zero,x_one,y_one,lis)




def shaded_plane(a,b,c,d,color):
    Line(a[0]+1,a[1],a[2],c[0]+1,c[1],c[2],out1,256) 
    Line(b[0],b[1],b[2],d[0],d[1],d[2],out2,256) 
    global vc 
    global cnt 
    global bcnt 
    v.append(a) #0 
    v.append(b) #1
    v.append(c) #2 
    v.append(d) #3 
    lines.append(v[0+cnt+vc]) 
    lines.append(v[1+cnt+vc]) 
    types.append(1)
    lines.append(v[0+cnt+vc]) 
    lines.append(v[2+cnt+vc]) 
    types.append(1)
    lines.append([v[2+cnt+vc][0]+1,v[2+cnt+vc][1],v[2+cnt+vc][2]]) 
    lines.append(v[3+cnt+vc]) 
    types.append(1)
    lines.append(v[1+cnt+vc])
    lines.append(v[3+cnt+vc])
    types.append(1)
    for i in range(len(out1)):
        if i == 0:
            bcnt += 1
            continue
        v.append([out1[bcnt][0],out1[bcnt][1],0])
        v.append([out2[bcnt][0],out2[bcnt][1],0])
        print("First: ", out1[bcnt][0],out1[bcnt][1],0)
        print("Second: ", out2[bcnt][0],out2[bcnt][1],0)
        lines.append(v[4+cnt+vc])
        lines.append(v[5+cnt+vc])
        types.append(0)
        cnt += 2
        bcnt += 1
    vc += 4
    bcnt = 0
    print("Output 1: ", out1)
    print("Output 2: ", out2)
    out1.clear()
    out2.clear()
    


def shaded_triangle(a,b,c):
    global vc
    global cnt
    bcnt = 0
    v.append(a) #0
    v.append(b) #1
    v.append(c) #2
    lines.append(v[0+vc])
    types.append(1)
    lines.append(v[1+vc])
    types.append(1)
    lines.append([v[0+vc][0]+1,v[0+vc][1],v[0+vc][2]])
    types.append(1)
    lines.append(v[2+vc])
    types.append(1)
    lines.append(v[1+vc])
    types.append(1)
    lines.append(v[2+vc])
    types.append(1)
    Line(b[0]+1,b[1],b[2],a[0]+1,a[1],a[2],out1,256)
    Line(b[0],b[1],b[2],c[0],c[1],c[2],out2,256)
    for i in out1:
        v.append([out1[bcnt][0],out1[bcnt][1],0])
        v.append([out2[bcnt][0],out2[bcnt][1],0])
        lines.append(v[3+cnt])
        types.append(0)
        lines.append(v[4+cnt])
        types.append(0)
        cnt += 2
        bcnt += 1
    vc += 4
    out1.clear()
    out2.clear()



#shaded_plane([5,45,64],[37,45,64],[5,52,0],[37,52,0])
#shaded_plane([0,0,0],[64,0,0],[0,64,0],[64,64,0])

#shaded_plane([8,6,0],[32,14,0],[8,36,0],[32,44,0])
#shaded_plane([8,6,0],[32,2,32],[32,14,0],[56,6,0])

shaded_plane([16,24,0],[48,24,0],[8,40,0],[56,40,0],"red")

shaded_plane([8,40,0],[56,40,0],[10,63,0],[54,63,0],"red")


#shaded_triangle([0,32,0],[16,0,0],[32,32,0])



program = []

side = "B"

num = 1

for o in lines:
    eee = str(o[0]) + "-" + str(o[1]) + "-" + str(o[2])
    if num >= 2:
        program.append(eee)
        #program.append("0-0-0")
        #program.append("0-0-0")
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

with open(output_types, 'w') as f:
    for e in types:
        f.write(hex(int(e)) + "\n")
    print(types)
    f.close()


program = []

side = "B"

num = 1

for o in lines:
    eee = str(o[0]) + "-" + str(o[1]) + "-" + str(o[2])
    if num >= 2:
        program.append(eee)
        #program.append("0-0-0")
        #program.append("0-0-0")
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

with open(output_types, 'w') as f:
    for e in types:
        f.write(hex(int(e)) + "\n")
    print(types)
    f.close()




    


