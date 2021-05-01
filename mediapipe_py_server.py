import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

#Creating the connection to send the data
import socket
import pickle
import json

HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ipv4 and TCP
s.bind((socket.gethostname(), 1234))
s.listen(5)

clientsocket, address = s.accept()
print(f"Connection from {address} has ben estabilished!")

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_holistic.Holistic(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as holistic:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = holistic.process(image)

    # Draw landmark annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS)
    mp_drawing.draw_landmarks(
        image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    mp_drawing.draw_landmarks(
        image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    mp_drawing.draw_landmarks(
        image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
    cv2.imshow('MediaPipe Holistic', image)
    

    
    #preparing and sending the data

    
    # clientsocket, address = s.accept()
    # print(f"Connection from {address} has ben estabilished!")
    # print(results.pose_landmarks)
    # d = results.pose_landmarks
    # msg = pickle.dumps(d)
    pose=''
    
    try:
      pose=results.pose_landmarks.landmark
    except:
      pose=''

    #creating serialized variable to convert to json
    if isinstance(pose,str):
      msg = json.dumps('nada')
    else:
      pose_serialize=[]
      for i in range(len(pose)):
          x=pose[i].x
          y=pose[i].y
          z=pose[i].z
          pose_serialize.append([i,x,y,z])
          
      msg = json.dumps(pose_serialize)

      


    # print(msg)
    print('len: ',len(msg))
    print('len encode: ',len(msg.encode('utf-8')))
    # while True:
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg.encode('utf-8')
    clientsocket.send(msg)
    # #finish sending data    

    # clientsocket.sendall(msg.encode('utf-8'))

    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()