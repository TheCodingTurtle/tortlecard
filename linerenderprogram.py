#make sure to replace this with the location of the .hex file you want the program to be outputed to.
output_folder = ''


#Control Bits
# 1 - Pulse yi
# 2 - yi CLR
# 3 - DY < 0 yi--
# 4 - DY STR
# 5 - DY < 0 invert
# 6 - D IN
# 7 - X CLR
# 8 - X UP 
# 9 - X LD
# 10 - PLT
# 11 - RST screen
# 12 - Y IN
# 13 - Y y1/yi
# 14 - Y sub IN
# 15 - D sub IN
# 16 - D sub/d2
# 17 - D+(2*(dy-dx))/D+2*dy
# 18 - Comparator WE

#
#
#
#
#00000000000000000

program = ["CLR","YIUP","YI--CHK","0","YI--CHK","-DY","DIN","DSUB","YIN","YSUB","LDX","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP","PLT",
           "D>0yi","YSUB","D>0d1","D>0d2","DSUB","XUP"]


output = []
    
for i in program:
    if i == "CLR":
        output.append(hex(int("000110110001100010", 2)))
    elif i == "YIUP":
        output.append(hex(int("00000000000000001", 2)))
    elif i == "YI--CHK":
        output.append(hex(int("00000000000000100", 2)))
    elif i == "0":
        output.append(hex(int("00000000000000000", 2)))
    elif i == "-DY":
        output.append(hex(int("00000000000011000", 2)))
    elif i == "DSUB":
        output.append(hex(int("00100000000000000", 2)))
    elif i == "YSUB":
        output.append(hex(int("00010000000000000", 2)))
    elif i == "DIN":
        output.append(hex(int("00000000000100000", 2)))
    elif i == "YIN":
        output.append(hex(int("00000100000000000", 2)))
    elif i == "LDX":
        output.append(hex(int("00000000110000000", 2)))
    elif i == "PLT":
        output.append(hex(int("00000001000000000", 2)))
    elif i == "D>0yi":
        output.append(hex(int("00001100000000000", 2)))
    elif i == "D>0d1":
        output.append(hex(int("01000000000100000", 2)))
    elif i == "D>0d2":
        output.append(hex(int("11000000000100000", 2)))
    elif i == "XUP":
        output.append(hex(int("00000000010000000", 2)))



    

with open(output_folder, 'w') as f:
    for e in output:
        f.write(e + "\n")
    print(output)
    f.close()