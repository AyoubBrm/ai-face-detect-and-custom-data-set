from ultralytics import YOLO

model = YOLO("C:\\Users\\ayoub\\Desktop\\face-detect-\\detect\\train4\\weights\\best.pt")

if __name__ == "__main__":
    result = model("WIN_20240902_07_30_49_Pro.jpg",# you can choose path for your image or vidoi (first arg)
        save=True) 
    result[0].show()