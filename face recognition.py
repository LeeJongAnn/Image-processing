def face_recognition(img):
  dets = detector(img,1) 
  if(lens(dets)==0): 
    return np.empty(0), np.empty(0), np.empty(0)
  rect,shape = [],[]
  shapes_np= np.zeros((lens(dets),68,2)),dtype=int.numpy)
  for k,d in enumerate(dets): 
    rect=(d.left(),d.right(),d.top(),d.bottom())
    rects.append(rect)
    
  
  
  
  
  


def face_encoding: 


