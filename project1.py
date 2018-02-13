d=1
list1=[' ' , '1' , ' ' ,'|',' ','2',' ','|',' ','3',' ']
list2=[' ' , '4' , ' ' ,'|',' ','5',' ','|',' ','6',' ']
list3=[' ' , '7' , ' ' ,'|',' ','8',' ','|',' ','9',' ']

while True:
        for i in list1:
            print(i, end="")
        print()
        for k in list2:
            print(k, end="")
        print()
        for j in list3:
            print(j, end="")
        print()

        while True:
            print("player1 :")
            cell = input("enter the number of the cell")
            if(cell in list1):
                 in_cell=list1.index(cell)
                 list1[in_cell]="X"
                 break
            if(cell in list2):
                in_cell=list2.index(cell)
                list2[in_cell]="X"
                break
            if(cell in list3):
                in_cell=list3.index(cell)
                list3[in_cell]="X"
                break
            print("write another number")
        print(" ")    
        

        if(list1[1]=='X' and list1[5]=='X' and list1[9]=='X') or (list1[1]=='X' and list2[1]=='X' and list3[1]=='X') or (list2[1]=='X' and list2[5]=='X' and list2[9]=='X') or (list1[5]=='X' and list2[5]=='X' and list3[5]=='X') or (list3[1]=='X' and list3[5]=='X' and list3[9]=='X') or (list1[9]=='X' and list2[9]=='X' and list3[9]=='X') or (list1[1]=='X' and list2[5]=='X' and list3[9]=='X') or (list1[9]=='X' and list2[5]=='X' and list3[1]=='X'):
            print ("player1 is the winner")
            break
        if(d==9):
            print("Draw ")
            break
        d=d+1
        
        #if(list1[1] in range(10))

        for i in list1:
            print(i, end="")
        print()
        for k in list2:
            print(k, end="")
        print()
        for j in list3:
            print(j, end="")
        print()

   
        while True:
            print("player2 :")
            cell =input("enter the number of the cell")
            if(cell in list1):
                 in_cell=list1.index(cell)
                 list1[in_cell]="O"
                 break
            if(cell in list2):
                in_cell=list2.index(cell)
                list2[in_cell]="O"
                break
            if(cell in list3):
                in_cell=list3.index(cell)
                list3[in_cell]="O"
                break
            print("write another number")
        print(" ")

        if(list1[1]=='O' and list1[5]=='O' and list1[9]=='O') or (list1[1]=='O' and list2[1]=='O' and list3[1]=='O') or (list2[1]=='O' and list2[5]=='O' and list2[9]=='O') or (list1[5]=='O' and list2[5]=='O' and list3[5]=='O') or (list3[1]=='O' and list3[5]=='O' and list3[9]=='O') or (list1[9]=='O' and list2[9]=='O' and list3[9]=='O') or (list1[1]=='O' and list2[5]=='O' and list3[9]=='O') or (list1[9]=='O' and list2[5]=='O' and list3[1]=='O'):
            print("player2 is the winner")
            break
        if(d==9):
            print("Draw ")
            break
        d=d+1    
