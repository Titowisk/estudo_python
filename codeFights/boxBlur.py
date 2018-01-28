image = [[1, 1, 1], [1, 7, 1], [1, 1, 1]]

def sum_of_surroundings(row, column, matrix):
    try:
        s = 0
        for r in range(row-1, row+2):
            for c in range(column-1, column+2):
                s += matrix[r][c]
    except IndexError:
        return False
    
    return s/9

def boxBlur(image):
    image_blur = []
    new_array = []
    
    for i in range(len(image)): # row

        if new_array: 
            image_blur.append(new_array) 
        new_array = []
            
        for j in range(len(image[0])): # column
            if sum_of_surroundings(i, j, image):
                n = sum_of_surroundings(i, j, image)
                new_array.append(int(n))
        
    return image_blur

boxBlur(image)