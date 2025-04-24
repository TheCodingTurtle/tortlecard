import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import font as tkFont
from tkinter import colorchooser
#make sure to replace this with the location of the .hex file you want the A points to be outputed to.
output_folderA = ''

#make sure to replace this with the location of the .hex file you want the B points to be outputed to.
output_folderB = '' 

#make sure to replace this with the location of the .hex file you want the color values to be outputed to.
output_color = ''

vc = 0
cnt = 0
bcnt = 0

v = []
lines = [] 
colors = []

out1 = []
out2 = []

#v = [[31,31,0],[34,31,0],[31,32,0],[34,32,0],[31,33,0],[34,33,0],
     #[1,1,0],[4,1,0],[1,2,0],[4,2,0],[1,3,0],[4,3,0]]
#lines = [v[0],v[1],v[2],v[3],v[4],v[5],
         #v[6],v[7],v[8],v[9],v[10],v[11]]

#v = [[1,1,0],[9,1,0],[1,9,0],[9,9,0]]
#lines = [v[0],v[1],v[0],v[2],v[2],v[3],v[1],v[3]]

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
    #print("A: [" + str(x0) + "," + str(y0) + "," + str(z0) + "]")
    #print("B: [" + str(x1) + "," + str(y1) + "," + str(z1) + "]")
    x_zero = (x0*fov)/(fov+z0)
    y_zero = (y0*fov)/(fov+z0)
    x_one = (x1*fov)/(fov+z1)
    y_one = (y1*fov)/(fov+z1)
    plotLine(x_zero,y_zero,x_one,y_one,lis)




def shaded_plane(a,b,c,d,colorLight,colorDark):
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
    colors.append(1)
    lines.append(v[0+cnt+vc]) 
    lines.append(v[2+cnt+vc]) 
    colors.append(1)
    lines.append([v[2+cnt+vc][0]+1,v[2+cnt+vc][1],v[2+cnt+vc][2]]) 
    lines.append(v[3+cnt+vc]) 
    colors.append(1)
    lines.append(v[1+cnt+vc])
    lines.append(v[3+cnt+vc])
    colors.append(1)
    for i in range(len(out1)):
        if i == 0:
            bcnt += 1
            continue
        v.append([out1[bcnt][0],out1[bcnt][1],0])
        v.append([out2[bcnt][0],out2[bcnt][1],0])
        #print("First: ", out1[bcnt][0],out1[bcnt][1],0)
        #print("Second: ", out2[bcnt][0],out2[bcnt][1],0)
        lines.append(v[4+cnt+vc])
        lines.append(v[5+cnt+vc])
        colors.append(0)
        cnt += 2
        bcnt += 1
    vc += 4
    bcnt = 0
    #print("Output 1: ", out1)
    #print("Output 2: ", out2)
    out1.clear()
    out2.clear()
    

'''
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

'''
    
# code for UI

pointAX = 0
pointAY = 0
pointAset = False

pointBX = 0
pointBY = 0
pointBset = False

pointCX = 0
pointCY = 0
pointCset = False

pointDX = 0
pointDY = 0
pointDset = False

color_code = "ffffff"

pointsAB = []



window = tk.Tk()

window.minsize(705,675)
window.maxsize(705,675)

canvas = tk.Canvas()
window.title("Point Plotter (Preview may not always be accurate) (Shaded objects can be buggy)")

window.rowconfigure(0,weight=1)
window.columnconfigure(1,weight=1)

helv16 = tkFont.Font(family='Helvetica', size=16, weight='bold')
helv16_nobold = tkFont.Font(family='Helvetica', size=16)

def drawLine(a,b,c,d):
    global pointsAB
    plotLine(a, b, c, d, pointsAB)
    colors.append(color_code)
    for m in pointsAB:
        drawpixel(m[0],m[1])
    pointsAB = []

def pickColor():
    global color_code
    color_code = str((colorchooser.askcolor(title ="Choose color"))[1]).replace('#','')
    linfo['text'] = "Point A: (" + str(pointAX) + "," + str(pointAY) + ") \n Point B: ("  + str(pointBX) + "," + str(pointBY) + ") \n Point C: ("  + str(pointCX) + "," + str(pointCY) + ") \n Point D: ("  + str(pointDX) + "," + str(pointDY) + ") \n Color: " + color_code

def CreateLine():
    global vc
    global pointAset
    global pointBset
    global pointAX
    global pointAY
    global pointBX
    global pointBY
    global pointsAB
    drawLine(pointAX,pointAY,pointBX,pointBY)
    v.append([pointAX, pointAY, 0])
    v.append([pointBX, pointBY, 0])
    lines.append(v[0+vc])
    lines.append(v[1+vc])
    vc+=2
    pointAX = 0
    pointAY = 0
    pointBX = 0
    pointBY = 0
    pointAset = False
    pointBset = False
    pointsAB = []
    linfo['text'] = "Point A: (0,0) \n Point B: (0,0) \n Point C: (0,0) \n Point D: (0,0) \n Color: " + color_code


def CreatePlane():
    global pointAset
    global pointBset
    global pointCset
    global pointDset
    global pointAX
    global pointAY
    global pointBX
    global pointBY
    global pointCX
    global pointCY
    global pointDX
    global pointDY
    global pointsAB
    shaded_plane([pointAX, pointAY,0],[pointBX, pointBY,0],[pointCX, pointCY,0],[pointDX, pointDY,0],str(color_code),"222222")
    for e in range(0,len(v),2):
        drawLine(v[e][0],v[e][1],v[e+1][0],v[e+1][1])
        print("draw line: " + str(v[e][0]) + "-" + str(v[e][1]) + " " + str(v[e+1][0]) + "-" + str(v[e+1][1]) + "")
    print(v)
    pointAX = 0
    pointAY = 0
    pointBX = 0
    pointBY = 0
    pointCX = 0
    pointCY = 0
    pointDX = 0
    pointDY = 0
    pointAset = False
    pointBset = False
    pointCset = False
    pointDset = False
    pointsAB = []
    linfo['text'] = "Point A: (0,0) \n Point B: (0,0) \n Point C: (0,0) \n Point D: (0,0) \n Color: " + color_code
'''
def CreateTriangle():
    global pointAset
    global pointBset
    global pointCset
    global pointDset
    global pointAX
    global pointAY
    global pointBX
    global pointBY
    global pointCX
    global pointCY
    global pointDX
    global pointDY
    global pointsAB
    shaded_triangle([pointAX, pointAY,0],[pointBX, pointBY,0],[pointCX, pointCY,0])
    for e in range(0,len(v),2):
        drawLine(v[e][0],v[e][1],v[e+1][0],v[e+1][1])
        print("draw line: " + str(v[e][0]) + "-" + str(v[e][1]) + " " + str(v[e+1][0]) + "-" + str(v[e+1][1]) + "")
    print(v)
    pointAX = 0
    pointAY = 0
    pointBX = 0
    pointBY = 0
    pointCX = 0
    pointCY = 0
    pointDX = 0
    pointDY = 0
    pointAset = False
    pointBset = False
    pointCset = False
    pointDset = False
    pointsAB = []
    linfo['text'] = "Point A: (0,0) \n Point B: (0,0) \n Point C: (0,0) \n Point D: (0,0) \n Color: " + color_code

'''

frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_1 = tk.Button(frm_buttons, text="Line", font=helv16, width=14,command=CreateLine)
btn_2 = tk.Button(frm_buttons, text="Shaded Plane", font=helv16, width=14,command=CreatePlane)
btn_3 = tk.Button(frm_buttons, text="Shaded Triangle", font=helv16, width=14,state="disabled")
btn_4 = tk.Button(frm_buttons, text="Color Picker", font=helv16, width=14,command=pickColor)




btn_1.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_2.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_3.grid(row=2, column=0, sticky="ew", padx=5,pady=5)
btn_4.grid(row=3, column=0, sticky="ew", padx=5,pady=5)


l2 = tk.Label(window, text = "X",font=helv16)
l2.grid(row=1,column=0,sticky="es", pady=5)
l3 = tk.Label(window, text = "Y",font=helv16)
l3.grid(row=2,column=0,sticky="en", pady=5)

linfo = tk.Label(window, text = "Point A: (0,0) \n Point B: (0,0) \n Point C: (0,0) \n Point D: (0,0) \n Color: #ffffff",font=helv16)
linfo.grid(row=2,column=1,sticky="se")

bkg = canvas.create_rectangle(0,0,500,500,outline="black",fill="black")
canvas.grid(row=0,column=1,sticky="nsew")

def drawpixel(x,y):
    canvas.create_rectangle(int(x)*7.8125,int(y)*7.8125,(int(x)*7.8125)+7.8125,(int(y)*7.8125)+7.8125,outline="#"+color_code,fill="#"+color_code)
    

def plot():
    global pointAset
    global pointBset
    global pointCset
    global pointDset
    global pointAX
    global pointAY
    global pointBX
    global pointBY
    global pointCX
    global pointCY
    global pointDX
    global pointDY
    global color_code
    if cordx.get() == "" or cordy.get() == "":
        messagebox.showerror("Error","There needs to be an X and Y value set.")
    if int(cordx.get()) < 0 or int(cordx.get()) > 63:
        messagebox.showerror("Error","X value needs to be an integer between 0 and 63.")
    if int(cordy.get()) < 0 or int(cordy.get()) > 63:
        messagebox.showerror("Error","Y value needs to be an integer between 0 and 63.")
    drawpixel(int(cordx.get()), int(cordy.get()))
    if pointCset == True:
        pointDX = int(cordx.get())
        pointDY = int(cordy.get())
        pointDset = True
        linfo['text'] = "Point A: (" + str(pointAX) + "," + str(pointAY) + ") \n Point B: ("  + str(pointBX) + "," + str(pointBY) + ") \n Point C: ("  + str(pointCX) + "," + str(pointCY) + ") \n Point D: ("  + str(pointDX) + "," + str(pointDY) + ") \n Color: " + color_code
        return
    if pointBset == True:
        pointCX = int(cordx.get())
        pointCY = int(cordy.get())
        pointCset = True
        linfo['text'] = "Point A: (" + str(pointAX) + "," + str(pointAY) + ") \n Point B: ("  + str(pointBX) + "," + str(pointBY) + ") \n Point C: ("  + str(pointCX) + "," + str(pointCY) + ") \n Point D: (0,0) \n Color: " + color_code
        return
    if pointAset == True:
        pointBX = int(cordx.get())
        pointBY = int(cordy.get())
        pointBset = True
        linfo['text'] = "Point A: (" + str(pointAX) + "," + str(pointAY) + ") \n Point B: ("  + str(pointBX) + "," + str(pointBY) + ") \n Point C: (0,0) \n Point D: (0,0) \n Color: " + color_code
        return
    if pointAset == False:
        pointAX = int(cordx.get())
        pointAY = int(cordy.get())
        pointAset = True
        linfo['text'] = "Point A: (" + str(pointAX) + "," + str(pointAY) + ") \n Point B: (0,0) \n Point C: (0,0) \n Point D: (0,0) \n Color: " + color_code
        return
    
    
    



btn_plot = tk.Button(window, text="Plot", font=helv16, width=6,command=plot)
btn_plot.grid(row=1,column=1,sticky="ws",padx=100)


cordx = tk.Entry(window,font=helv16_nobold,width=5)
cordx.grid(row=1,column=1,sticky="ws", pady=5)

cordy = tk.Entry(window,font=helv16_nobold,width=5)
cordy.grid(row=2,column=1,sticky="wn", pady=5)



frm_buttons.grid(row=0, column=0, sticky="ns")





window.mainloop()

#shaded_plane([5,45,64],[37,45,64],[5,52,0],[37,52,0])
#shaded_plane([0,0,0],[64,0,0],[0,64,0],[64,64,0])

#shaded_plane([8,6,0],[32,14,0],[8,36,0],[32,44,0])
#shaded_plane([8,6,0],[32,2,32],[32,14,0],[56,6,0])




#shaded_plane([16,24,0],[48,24,0],[8,40,0],[56,40,0],"red")

#shaded_plane([8,40,0],[56,40,0],[10,63,0],[54,63,0],"red")


#shaded_plane([30,30,0],[34,30,0],[30,34,0],[34,34,0], "")




#shaded_triangle([0,32,0],[16,0,0],[32,32,0])

#shaded_triangle([0,12,0],[8,0,0],[16,12,0])

#shaded_plane([2,2,0],[7,2,0],[2,7,0],[7,7,0], "")



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


    

with open(output_folderA, 'w') as f:
    for e in outputA:
        f.write(e + "\n")
    f.close()

with open(output_folderB, 'w') as f:
    for e in outputB:
        f.write(e + "\n")
    f.close()

with open(output_color, 'w') as f:
    for e in colors:
        f.write(str(e) + "\n")
    f.close()


print(outputA)
print(outputB)
print(colors)



    


