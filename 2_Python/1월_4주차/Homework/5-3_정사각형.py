def only_square_area(width,height):
    square = []
    for i in width:
        for j in height:
            if i == j :
                square.append(i*j)
    return square

print(only_square_area([32,55,63],[13,32,40,55]))