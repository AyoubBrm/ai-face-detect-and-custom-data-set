from ultralytics import YOLO

model = YOLO("yolo11n.pt")

if __name__ == "__main__":
    result = model.tran(data="C:\\Users\\ayoub\\Desktop\\face-detect-\\FACE.DET.v3i.yolov11\\data.yaml",
        epochs=5,# you can increas the epochs for best performance more repeat more accuracy 
        imgsz=640, 
        device=0)  #you can use "cpu" insted of (0 gpu)