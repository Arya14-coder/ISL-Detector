import sys
import os
print(f"Python path: {sys.path}")
print(f"Current directory: {os.getcwd()}")
print(f"Files in current directory: {os.listdir('.')}")
try:
    import mediapipe
    print(f"Mediapipe file: {mediapipe.__file__}")
    print(f"Mediapipe attributes: {dir(mediapipe)}")
except Exception as e:
    print(f"Error importing mediapipe: {e}")
