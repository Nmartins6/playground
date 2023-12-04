import cv2

# Load the image
image = cv2.imread('Foto_2023-12-01_141717.jpg')

# Get image dimensions
height, width, _ = image.shape

# Define proportions for the bottom left crop (30% of width and 40% of height)
percentage_width = 0.5
percentage_height = 0.5

# Calculate coordinates for the crop
x = 0  # Leftmost part
y = int(height * (1 - percentage_height))  # 40% of the height from the bottom
crop_width = int(width * percentage_width)  # 30% of the width
crop_height = int(height * percentage_height)  # 40% of the height

# Draw a rectangle to show the area to be cropped
cv2.rectangle(image, (x, y), (x + crop_width, y + crop_height), (0, 255, 0), 2)

# Show the image with the rectangle outlining the crop area
cv2.imshow('Image with Contour', image)
cv2.waitKey(0)

# Crop the region of interest from the image
cropped_image = image[y:y+crop_height, x:x+crop_width]

# Show the cropped image
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
