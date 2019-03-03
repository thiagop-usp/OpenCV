import cv2
import numpy as np

#reading the images
full_img = cv2.imread('level.png', 0)
tmp = cv2.imread('body.png', 0)

h, w = tmp.shape

#obtaining the match matrix
match_mat = cv2.matchTemplate(full_img, tmp, cv2.TM_CCOEFF_NORMED)

#we'll use this threshold for possible matches
threshold = 0.8;

#looking for values in the match matrix which match at least 80%
pat = np.where(match_mat >= threshold)

# zip(*pat[::-1]) will make pairs with formatting (w, h)
# the [::-1] inverts the lists (h, w) -> (w,h)
# the * makes the intern values from lists form an outer bigger list
# for instance: [[1, 2, 3],[4, 5]] becomes [1, 2, 3, 4, 5]
# the zip pairs them up

for i in zip(*pat[::-1]):
    cv2.rectangle(full_img, i, (i[0] + w, i[1] + h), 2)

cv2.imwrite('test.jpg', full_img)
