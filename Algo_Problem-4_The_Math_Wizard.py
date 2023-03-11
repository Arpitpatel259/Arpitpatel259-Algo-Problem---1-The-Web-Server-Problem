
file = open('input.txt', 'r')
file1 = open("output.txt","w")
a = int(file.readline())
a =a + 1
z = 0
for x in range(a):
    if z == 0:
        z=z+1
        pass
    else:
        a=""
        l = file.readline() 
        l = l.split()
        for i in l:
                if i == "one" or i=="1":
                    a = a + "1"
                
                elif i == "two" or i=="2":
                    a = a + "2"
                
                elif i == "three" or i=="3":
                    a = a + "3"
                
                elif i == "four" or i=="4":
                    a = a + "4"
                
                elif i == "five" or i=="5":
                    a = a + "5"
                
                elif i == "six" or i=="6":
                    a = a + "6"
                
                elif i == "seven" or i=="7":
                    a = a + "7"
                
                elif i == "eight" or i=="8":
                    a = a + "8"
                
                elif i == "nine" or i=="9":
                    a = a + "9"
                    
                elif i == "plus" or i=="+":
                    a = a + "+"
                    
                elif i == "subtract" or i=="-":
                    a = a + "-"
                    
                elif i == "multiple" or i=="*":
                    a = a + "*"
                    
                elif i == "division" or i=="/":
                    a = a + "/"
                
        b = eval(a)         
        if str(b) == l[len(l)-1]:
                file1.write("Case #"+str(z)+" true \n")
                z=z+1
                
        else :
            file1.write("Case #"+str(z)+" false \n")
            z=z+1
            
file1.close()             
file.close()             

