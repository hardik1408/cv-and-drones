import cv2
import numpy as np

# Load the distorted image
img = cv2.imread('dist.jpg')
cv2.imshow('Distorted Image', img)
# Prepare object points (3D coordinates of chessboard corners in real world)
objp = np.zeros((6*9, 3), np.float32)
objp[:, :2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2)  # Fill in X and Y coordinates

# Arrays to store object points and image points from all images
objpoints = []
imgpoints = []

# Find chessboard corners in the image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, corners = cv2.findChessboardCorners(gray, (9, 6), None)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)  # Define the criteria
corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)

if ret:
    objpoints.append(objp)
    imgpoints.append(corners)
    corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)

# Calibrate camera
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# Undistort the image
undistorted_img = cv2.undistort(img, mtx, dist, None, mtx)

# Display the undistorted image
cv2.imshow('Undistorted Image', undistorted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
