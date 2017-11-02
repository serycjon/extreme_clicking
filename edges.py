import cv2
import numpy as np

img = cv2.imread("examples/beermat.jpg")    
detector = cv2.ximgproc.createStructuredEdgeDetection('model.yml.gz')
edges = detector.detectEdges(np.float32(img) / 255)
cv2.imshow("image", img)    
cv2.imshow("edges", guided)    
cv2.waitKey(0)
