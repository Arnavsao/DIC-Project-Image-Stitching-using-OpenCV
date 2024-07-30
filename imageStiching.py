import numpy as np
import cv2
import glob
import imutils

# Load images from the directory
image_paths = glob.glob('archive/*.jpg')
images = []

# Loading the images
for image_path in image_paths:
    img = cv2.imread(image_path)
    images.append(img)
    cv2.imshow("Image", img)
    cv2.waitKey(1000)  # Display each image for 1 second
    cv2.destroyAllWindows()

# Initialize Stitcher
ImageStitcher = cv2.Stitcher_create()

# Stitch images
status, stitched_img = ImageStitcher.stitch(images)

# Check stitching status
if status == cv2.Stitcher_OK:
    # Save and display the stitched image
    cv2.imwrite("stitchedOutput.png", stitched_img)
    cv2.imshow("Stitched Image", stitched_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Apply padding to the stitched image
    stitched_img = cv2.copyMakeBorder(stitched_img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=(0, 0, 0))

    # Convert stitched image to grayscale
    gray = cv2.cvtColor(stitched_img, cv2.COLOR_BGR2GRAY)

    # Threshold the grayscale image
    _, thresh_img = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded image
    contours = cv2.findContours(thresh_img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)

    # Find the contour with maximum area
    max_contour = max(contours, key=cv2.contourArea)

    # Create a mask for the largest contour
    mask = np.zeros(thresh_img.shape, dtype="uint8")
    cv2.drawContours(mask, [max_contour], -1, 255, -1)

    # Erode the mask until no non-zero pixels are left
    min_rectangle = mask.copy()
    while cv2.countNonZero(min_rectangle) > 0:
        min_rectangle = cv2.erode(min_rectangle, None)

    # Find contours again on the eroded mask
    contours = cv2.findContours(min_rectangle.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    areaI = max(contours, key=cv2.contourArea)

    # Display the minRectangle Image
    cv2.imshow("minRectangle Image", min_rectangle)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Extract the region of interest from the stitched image
    x, y, w, h = cv2.boundingRect(areaI)
    stitched_img_processed = stitched_img[y:y + h, x:x + w]

    # Write the processed stitched image to a file
    cv2.imwrite("stitchedOutputProcessed.png", stitched_img_processed)

    # Display the processed stitched image
    cv2.imshow("Stitched Image Processed", stitched_img_processed)
    cv2.waitKey(0)
else:
    print("Stitching failed!")
