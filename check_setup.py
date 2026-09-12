import torch
gpu = torch.cuda.get_device_name(0) if torch.cuda.is_available() else "N/A"
print(f"PyTorch {torch.__version__} | CUDA available: {torch.cuda.is_available()} | GPU: {gpu}")

import torchvision
print(f"TorchVision {torchvision.__version__}")

import cv2
print(f"OpenCV {cv2.__version__}")

import transformers
print(f"Transformers {transformers.__version__}")

import ultralytics
print(f"Ultralytics {ultralytics.__version__}")

import gradio
print(f"Gradio {gradio.__version__}")

import numpy
print(f"NumPy {numpy.__version__}")

import sklearn
print(f"Scikit-learn {sklearn.__version__}")

import timm
print(f"Timm {timm.__version__}")

import onnxruntime
print(f"ONNX Runtime {onnxruntime.__version__}")

import albumentations
print(f"Albumentations {albumentations.__version__}")

import easyocr
print(f"EasyOCR {easyocr.__version__}")

import streamlit
print(f"Streamlit {streamlit.__version__}")

import fastapi
print(f"FastAPI {fastapi.__version__}")

print("\n🏆 ALL SYSTEMS GO! Ready to win the hackathon!")
