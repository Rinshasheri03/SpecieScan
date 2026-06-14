# USAGE
# python yolo_video.py --input videos/airport.mp4 --output output/airport_output.avi --yolo yolo-coco
# import the necessary packages
import datetime

import numpy as np
import argparse



import time
import cv2
import os






labelsPath = os.path.sep.join([r"C:\Users\user\Desktop\myproject final1\myproject\templates\yolo-coco", "coco.names"])
LABELS = open(labelsPath).read().strip().split("\n")
# initialize a list of colors to represent each possible class label.

np.random.seed(42)
COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),
	dtype="uint8")

# derive the paths to the YOLO weights and model configuration
weightsPath = os.path.sep.join([r"C:\Users\user\Desktop\myproject final1\myproject\templates\yolo-coco", "yolov3.weights"])
configPath = os.path.sep.join([r"C:\Users\user\Desktop\myproject final1\myproject\templates\yolo-coco", "yolov3.cfg"])
def rectangles_overlap(rect1, rect2):
    # Check for horizontal overlap
    if rect1[0] < rect2[0] + rect2[2] and rect1[0] + rect1[2] > rect2[0]:
        # Check for vertical overlap
        if rect1[1] < rect2[1] + rect2[3] and rect1[1] + rect1[3] > rect2[1]:
            return True
    return False
# load our YOLO object detector trained on COCO dataset (80 classes)
# and determine only the *output* layer names that we need from YOLO
print("[INFO] loading YOLO from disk...")
net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
ln = net.getLayerNames()
ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
(W, H) = (None, None)

def predict_object(fn):
	frame=cv2.imread(fn)
	reclist=[]
	(H, W) = frame.shape[:2]
	# construct a blob from the input frame and then perform a forward
	# pass of the YOLO object detector, giving us our bounding boxes
	# and associated probabilities
	blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
		swapRB=True, crop=False)
	net.setInput(blob)
	start = time.time()
	layerOutputs = net.forward(ln)
	end = time.time()

	# initialize our lists of detected bounding boxes, confidences,
	# and class IDs, respectively
	boxes = []
	confidences = []
	classIDs = []

	# loop over each of the layer outputs
	for output in layerOutputs:
		# loop over each of the detections
		for detection in output:
			# extract the class ID and confidence (i.e., probability)
			# of the current object detection
			scores = detection[5:]
			classID = np.argmax(scores)
			confidence = scores[classID]

			# filter out weak predictions by ensuring the detected
			# probability is greater than the minimum probability
			if confidence > 0.6 and classID!=25 and classID!=14:
				print(classID)
				print(confidence)
				if classID!=75:
					return False
				else:
					if confidence > 0.7:
						return False

	return True
# print(predict_object(r"C:\PycharmProjects\PycharmProjects\myproject\media\1000227137.jpg"))