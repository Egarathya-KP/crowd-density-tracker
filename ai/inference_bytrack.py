"""
Basic YOLOv8 + ByteTrack pipeline stub.
Detects and tracks people, computes density grid and flow metrics,
then POSTs results to the backend API every second.
"""
import cv2, numpy as np, time, requests
from ultralytics import YOLO
# from bytetrack import ByteTrack  # integrate your chosen ByteTrack implementation

BACKEND_URL = "http://backend:8000/ingest"  # container name

def main(video="data/sample.mp4"):
    model = YOLO("yolov8n.pt")
    cap = cv2.VideoCapture(video)
    frame_id = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        results = model.predict(frame, imgsz=640, conf=0.35, classes=[0])
        detections = []
        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                score = float(box.conf[0])
                detections.append([x1, y1, x2, y2, score])

        # TODO: integrate ByteTrack update() here → get tracks
        # For now, simulate density with number of detections
        density = len(detections)
        payload = {
            "camera": "cam1",
            "ts": time.time(),
            "density": density,
            "grid_counts": [[density]],
            "avg_flow": [[{"vx": 0, "vy": 0}]],
        }
        try:
            requests.post(BACKEND_URL, json=payload, timeout=1)
        except Exception as e:
            print("Backend not reachable:", e)
        frame_id += 1
        if frame_id % 10 == 0:
            print(f"Processed {frame_id} frames...")
    cap.release()

if __name__ == "__main__":
    main()
