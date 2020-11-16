# #Ploygon Area
#Assuming Irregular Polygons
#I am going to implement shoelace method of finding area of polygons
#Following Instructions in this vid for shoelace method
#https://www.youtube.com/watch?v=FSWPX0XB7a0

def shoelace(list):
    #input in clockwise direction
    
    list.append(list[0])
    n = len(list)
    t1 = 0
    t2 = 0
    for i in range(n-1):
        t1+=int(list[i][0])*int(list[i+1][1])
        t2+=int(list[i][1])*int(list[i+1][0])

    return abs(t1-t2)*0.5




if __name__ == '__main__':
    # list = [(4,10), (9,7), (11,2), (2,2)]
    list =[]

    #Specify the size of the list
    #then input the (x,y) coords for the list
    #Example
    # 4
    # 4 10
    # 9 7
    # 11 2
    # 2 2

    n = int(input())

    for i in range(n):
        x, y = input().split()
        list.append((x,y))

    print(shoelace(list))   
