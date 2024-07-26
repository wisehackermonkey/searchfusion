# #%%pip install ultralytics
# # import ultralytics
# from ultralytics import YOLO

# # ultralytics.checks()


# model = YOLO('yolov8n-cls.pt')  # load a pretrained YOLOv8n classification model
# model.train(data='mnist160', epochs=3)  # train the model
# model('https://ultralytics.com/images/bus.jpg')  # predict on an image


# # Load a pretrained YOLOv8n model
# model = YOLO("yolov8n-cls.pt")

# # Run inference on 'bus.jpg' with arguments
# r = model.predict("./images/image.jpg", save=True, imgsz=320, conf=0.5, visualize=True)
# r 

from ultralytics import YOLO
import os
# Load a model

model = YOLO("yolov8x-cls.pt")  # load an official model
# model = YOLO("path/to/best.pt")  # load a custom model
photo_dir = [file for file in os.walk("./photos") ][0]#[0][2]
photos = list(filter(lambda x: x.endswith(('tiff', 'bmp', 'jpeg', 'png', 'dng', 'webp', 'jpg', 'tif')),photo_dir[2]))
root_name = photo_dir[0]
# Predict with the model
image_classifictions = []
for photo in photos:
    results = model.predict(root_name+"/"+photo, save=False, imgsz=320, conf=0.5)  # predict on an image
    print(root_name+"/"+photo)
    image_classifictions.append(results[0].verbose())
s = 0