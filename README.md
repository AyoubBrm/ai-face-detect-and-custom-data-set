# Face Detection AI using YOLOv11

# 📌 Overview

## This project provides a face detection AI using YOLOv11. It consists of two main scripts:

* train.py – Used to train the YOLOv11 model on your dataset.

* run.py – Runs the trained model to detect faces using the trained weights.

* This project supports any dataset for face detection and can be customized as needed.

# 🚀 Installation

1️⃣ Install Dependencies

Ensure you have Python 3.8+ installed, then install the required dependencies:

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126

pip install Ultralytics

2️⃣ Clone the Repository

* git clone https://github.com/AyoubBrm/face-detect-.git

* cd face-detect-ai

# 🏋️‍♂️ Training the Model

* To train the model on your dataset, run:

* python train.py

## Ensure your dataset is prepared and formatted for YOLO.

* Modify train.py to adjust training parameters such as epochs, batch size, and dataset path.

# 🏃 Running Face Detection

* After training, you can run the model using:

* python run.py

# This script loads the trained weights from:

* detect/train4/weights/best.pt

# Ensure the model file exists in this directory before executing the script.

* 🔧 Customization

* Supports any dataset in YOLO annotation format.

* Modify train.py to adjust training settings like batch size, learning rate, and epochs.

* Update run.py to configure inference settings, such as confidence thresholds and input sources.

