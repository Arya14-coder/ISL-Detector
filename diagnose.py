import mediapipe as mp
print(f"MediaPipe attributes: {dir(mp)}")
try:
    print(f"MediaPipe solutions: {mp.solutions}")
except AttributeError:
    print("MediaPipe has no attribute 'solutions'")
