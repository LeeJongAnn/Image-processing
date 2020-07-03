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

for name, img_path in img_paths.items():
    img_bgr = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    _, img_shapes, _ = find_faces(img_rgb)
    descs[name] = encode_faces(img_rgb, img_shapes)[0]

np.save('img/descs.npy', descs)


img_bgr = cv2.imread('C:/Users/Lee Jong Ann/Desktop/picture/girl19.jpg')
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

rects, shapes, _ = find_faces(img_rgb)
descriptors = encode_faces(img_rgb, shapes)


fig, ax = plt.subplots(1, figsize=(20, 20))
ax.imshow(img_rgb)

for i, desc in enumerate(descriptors):
    
    found = False
    for name, saved_desc in descs.items():
        dist = np.linalg.norm([desc] - saved_desc, axis=1)

        if dist < 0.6:
            found = True

            text = ax.text(rects[i][0][0], rects[i][0][1], name,
                    color='b', fontsize=40, fontweight='bold')
            text.set_path_effects([path_effects.Stroke(linewidth=10, foreground='white'), path_effects.Normal()])
            rect = patches.Rectangle(rects[i][0],
                                 rects[i][1][1] - rects[i][0][1],
                                 rects[i][1][0] - rects[i][0][0],
                                 linewidth=2, edgecolor='w', facecolor='none')
            ax.add_patch(rect)

            break
    
    if not found:
        ax.text(rects[i][0][0], rects[i][0][1], 'unknown',
                color='r', fontsize=20, fontweight='bold')
        rect = patches.Rectangle(rects[i][0],
                             rects[i][1][1] - rects[i][0][1],
                             rects[i][1][0] - rects[i][0][0],
                             linewidth=2, edgecolor='r', facecolor='none')
        ax.add_patch(rect)

plt.axis('off')
plt.savefig('result/output.png')
plt.show()


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QPushButton,QDesktopWidget,QMainWindow, QAction, qApp
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap = QPixmap('result/output.png')

        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap)
        lbl_size = QLabel('Width: '+str(pixmap.width())+', Height: '+str(pixmap.height()))
        lbl_size.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_img)
        vbox.addWidget(lbl_size)
        self.setLayout(vbox)

        self.setWindowTitle('QPixmap')
        self.move(500, 500)
        self.center()
      
        btn = QPushButton('Quit', self)
        btn.move(250,390)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)
        
        
        
        self.setWindowTitle('Quit Button')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
