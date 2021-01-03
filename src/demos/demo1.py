"""
An `image` is represented by a 2-D array of integers, each integer representing
the pixel value of the image (from 0 to 65535).
Given a coordinate `(sr, sc)` representing the starting pixel (row and column)
of the flood fill, and a pixel value `newColor`, "flood fill" the image.
To perform a "flood fill", consider the starting pixel, plus any pixels
connected 4-directionally to the starting pixel of the same color as the
starting pixel, plus any pixels connected 4-directionally to those pixels (also
with the same color as the starting pixel), and so on. Replace the color of all
of the aforementioned pixels with the newColor.
At the end, return the modified image.
Example 1:
```plaintext
Input:
image = [[1,1,1],
         [1,1,0],
         [1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],
         [2,2,0],
         [2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels
connected by a path of the same color as the starting pixel are colored with
the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally
connected to the starting pixel.
```
Notes:
- The length of `image` and `image[0]` will be in the range `[1, 50]`.
- The given starting pixel will satisfy `0 <= sr < image.length` and
`0 <= sc < image[0].length`.
- The value of each color in `image[i][j]` and `newColor` will be an integer in
`[0, 65535]`.
"""
def flood_fill(image, sr, sc, new_color):
    """
    Inputs:
    image -> List[List[int]]
    sr -> int
    sc -> int
    new_color -> int
    Output:
    List[List[int]]
    """
     # Your code here
    # DFS recursive approach

    # set the row length to the len of the image
    row_length = len(image)
    # set col length to len of image[0]
    column_length = len(image[0])
    # extrapolate the color from the image at the staring row and staring col
    color = image[sr][sc]

    # check if the color is the same as the new color
    if color == new_color:
        # return the image
        return image

    # simple recursive DFS
    def dft(row, col):
        # check if the image at r and c is equal to color
        if image[row][col] == color:
            # set the image at r and c to the new color
            image[row][col] = newColor

            # do some recursive calls (get connections)
            # if the r is >= 1
            if row - 1 >= 1:
                # call dft passing in r-1, c
                dft(row-1, col)
            # if r+1 < row length
            if row + 1 < row_length:
                # call dft passing in r+1, c
                dft(row+1, col)
            # if the c is >=1
            if col - 1 >= 1:
                # call dft passing in r, c-1
                dft(row, col-1) 
            # if c+1 < col length
            if col + 1 < column_length:
                # call dft passing in r, c+1
                dft(row, col+1)

    # do an initial call to dft passing in sr and sc
    dft(sr, sc)
    # return image
    return image


image = [[1,1,1],
         [1,1,0],
         [1,0,1]]
sr = 1
sc = 1
newColor = 2

# Output: [[2,2,2],
#          [2,2,0],
#          [2,0,1]]

print("start image")
for row in image:
    print(row)

flood_fill(image, 0, 0, 2)

print("end image")
for row in image:
    print(row)