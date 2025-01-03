# program to capture video feed and images from webcam

# importing OpenCV library
import cv2

# Open the default camera
cam = cv2.VideoCapture("/dev/video0")

if not cam.isOpened():
    print("Error: Could not open camera.")
    exit()

# Get the default frame width and height
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Set brightness, contrast & define the codec format
cam.set(cv2.CAP_PROP_BRIGHTNESS, 128)
cam.set(cv2.CAP_PROP_CONTRAST, 128)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M','J','P','G'))

# Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

while True:
    # reading the input using the camera
    ret, frame = cam.read()

    # check if frames are being read correctly
    if not ret:
        print("Failed to grab frame")
        break

    # Display the captured frame
    cv2.imshow('Camera', frame)

# 	# saving image in local storage 
# 	cv2.imwrite("Camera.png", image) 

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and writer objects
cam.release()
#out.release()
cv2.destroyAllWindows()


# Python program to capture a single image using the pygame library 

# import pygame 
# import pygame.camera
# from pygame.locals import *

# # initializing the camera 
# pygame.camera.init() 

# # make the list of all available cameras 
# camlist = pygame.camera.list_cameras() 
# print(camlist)

# # if camera is detected or not 
# if camlist: 

# 	# initializing the cam variable with default camera 
# 	cam = pygame.camera.Camera(camlist[0], (640, 480))

# 	# opening the camera 
# 	cam.start()

# 	# capturing the single image 
# 	image = cam.get_image()
	
#     # pygame.display.set_caption("pyGame Camera View")

# 	# saving the image 
# 	#pygame.image.save(image, "filename.jpg")

# # if camera is not detected the moving to else part 
# else: 
# 	print("No camera on current device") 


# import pygame
# import pygame.camera

# pygame.init()

# gameDisplay = pygame.display.set_mode((640,480))

# pygame.camera.init()
# print (pygame.camera.list_cameras())
# cam = pygame.camera.Camera('/dev/video0')
# cam.start()
# while True:
#    img = cam.get_image()
#    gameDisplay.blit(img,(0,0))
#    pygame.display.update()
#    for event in pygame.event.get() :
#       if event.type == pygame.QUIT :
#          cam.stop()
#          pygame.quit()
#          exit()