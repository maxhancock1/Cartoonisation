from PIL import Image
import cv2


def cartoon_image(image_path):
    img = cv2.imread(image_path)

    # 1. Apply Bilateral Filter
    color_covert = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

    # 2. Convert to Grayscale
    gray = cv2.cvtColor(color_covert, cv2.COLOR_BGR2GRAY)

    # 3. Apply Median Blur
    blur = cv2.medianBlur(gray, 7)

    # 4. Use Adaptive Thresholding
    edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=9, C=2)

    # 5. Convert the Original Image to Color
    color_edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # 6. Bitwise the Color Image with the Edge Mask
    cartooned_image = cv2.bitwise_and(color_covert, color_edges)

    return cartooned_image


cartoon = cartoon_image("Images/cartoon.png")
cv2.imshow('Cartoon Image', cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()

