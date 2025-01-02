# program to capture single image from webcam in python 

# importing OpenCV library 
# import cv2

# initialize the camera 
# If you have multiple camera connected with 
# current device, assign a value in cam_port 
# variable according to that 
# cam_port = 0
# cam = cv2.VideoCapture(cam_port) 

# # reading the input using the camera 
# result, image = cam.read() 

# # If image will detected without any error, 
# # show result 
# if result: 

# 	# showing result, it take frame name and image 
# 	# output 
# 	cv2.imshow("Camera", image) 

# 	# saving image in local storage 
# 	#cv2.imwrite("Camera.png", image) 

# 	# If keyboard interrupt occurs, destroy image 
# 	# window 
# 	cv2.waitKey(0) 
# 	cv2.destroyWindow("Camera") 

# # If captured image is corrupted, moving to else part 
# else: 
# 	print("No image detected. Please! try again")


import cv2

# Open the default camera
cam = cv2.VideoCapture(0)

# Get the default frame width and height
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

while True:
    ret, frame = cam.read()

    # Write the frame to the output file
    # out.write(frame)

    # Display the captured frame
    cv2.imshow('Camera', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture and writer objects
cam.release()
#out.release()
cv2.destroyAllWindows()


# Python program to capture a single image 
# using pygame library 

# importing the pygame library 
# import pygame 
# import pygame.camera 

# # initializing the camera 
# pygame.camera.init() 

# # make the list of all available cameras 
# camlist = pygame.camera.list_cameras() 

# # if camera is detected or not 
# if camlist: 

# 	# initializing the cam variable with default camera 
# 	cam = pygame.camera.Camera(camlist[0], (640, 480)) 

# 	# opening the camera 
# 	cam.start() 

# 	# capturing the single image 
# 	image = cam.get_image() 

# 	# saving the image 
# 	pygame.image.save(image, "filename.jpg") 

# # if camera is not detected the moving to else part 
# else: 
# 	print("No camera on current device") 

# from cv2_enumerate_cameras import enumerate_cameras
# import ctypes
# #print (dir(ctypes))

# for camera_info in enumerate_cameras():
#     print(f'{camera_info.index}: {camera_info.name}')

# from pygrabber.dshow_graph import FilterGraph

# def get_available_cameras() :

#     devices = FilterGraph().get_input_devices()

#     available_cameras = {}

#     for device_index, device_name in enumerate(devices):
#         available_cameras[device_index] = device_name

#     return available_cameras

# print(get_available_cameras())

# from pymf import get_MF_devices
# import cv2

# device_list = get_MF_devices()
# cv_index = None
# for i, device_name in enumerate(device_list):
#     # find index of camera you want
#     q = input(f"Wanna use {device_name}?\n")
#     if q.strip() == "YES":
#         cv_index = i
#         break

# if cv_index is None:
#     print("Not found")
# else:
#     # make sure you use Media Foundation
#     cap = cv2.VideoCapture(cv_index + cv2.CAP_MSMF)
#     while (cap.isOpened):
#         ret, frame = cap.read()
#         if ret:
#             cv2.imshow("frame", frame)
#             k = cv2.waitKey(1)
#             if k > 0:
#                 break
#         else:
#             break
#     cap.release()
#     cv2.destroyAllWindows()

# from pymf import get_MF_devices
# device_list = get_MF_devices()
# for i, device_name in enumerate(device_list):
#     print(f"opencv_index: {i}, device_name: {device_name}")

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