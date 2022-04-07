



def image_path(image, curr, oldColor,newColor):
        x,y = curr
        if 0<=x<len(image) and 0<=y<len(image[0]):
            if image[x][y] == oldColor :
                image[x][y] = newColor
                image_path(image, (x+1,y), oldColor, newColor)
                image_path(image, (x-1,y), oldColor, newColor)
                image_path(image, (x,y+1), oldColor, newColor)
                image_path(image, (x,y-1), oldColor, newColor)





image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2

image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
newColor = 2


image = [[0,0,0],[0,1,1]]
sr = 1
sc = 1
newColor = 1
oldColor = image[sr][sc]
image_path(image, (sr,sc), oldColor, newColor)

print(image)