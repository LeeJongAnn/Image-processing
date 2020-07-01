import cv2
import dlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.patheffects as path_effects


detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor('models/shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('models/dlib_face_recognition_resnet_model_v1.dat')

def face_recognition(img): ## 얼굴 사각형을 인식하는 함수 업뎃
  dets = detector(img,1) 
  
  if(lens(dets)==0): 
    return np.empty(0), np.empty(0), np.empty(0)
  rects,shapes = [],[]
  shapes_np= np.zeros((lens(dets),68,2)),dtype=int.numpy)
  
  for k,d in enumerate(dets): 
    rect=(d.left(),d.right(),d.top(),d.bottom())
    rects.append(rect)
    shape = sp(img,d)
    for i in range(0,68): 
      shapes_np[k][i] = (shape.part(i).x,shape.part(i).y) 
     shapes.append(shape)
      
     return shapes,rects,shapes_np 
  
  def encode_faces(img,shape): 
    face_descriptors = []
    face_descriptor = facerec.compute_face_descriptor(img,shape)
    face_descriptors.append(face_descriptor)
    
    
    return np.array(face_descriptor)
    
      
img_path = { 
    'neo' : 'img/neo.jpg',
    'trinity' : 'img/trinity.jpg',
    'morpheous' : 'img/morpheous.jpg',
    
}

descs = { 
    'neo ': None ,
    'trinity' : None,
    'morpheous' : None,
    
}


