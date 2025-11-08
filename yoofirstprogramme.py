maze =[
    [0,0,1,0,1,0,1,1],
    [1,0,1,0,1,0,1,1],
    [1,0,0,0,0,0,0,1],
    [0,1,1,1,0,0,0,0],
    [0,0,1,1,1,1,0,1],
    [1,1,1,0,0,0,0,0],
    [1,0,0,1,1,0,0,1],
    [1,1,1,1,1,0,0,0]
]

   

def printyoo(MAZE):
     for row in maze:
         yoo =" "
         for col in row:
             yoo+="□ " if col==0 else "■ "
         print(yoo)

printyoo(maze)

