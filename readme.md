# 🧠 AI-Based Crowd Density & Flow Tracker  
### *Preventing Stampedes and Saving Lives*

---

## 📘 Overview

This project uses **AI-driven computer vision** to analyze live video feeds and estimate **crowd density and flow** in real time.  
It aims to **prevent stampedes**, detect **overcrowding**, and **assist emergency management** by providing early alerts and live dashboards.

The system leverages **YOLOv8 for detection** and **ByteTrack for multi-object tracking**, combined with a FastAPI backend and a React + Vite dashboard.

---

## 🚨 Problem Statement

Crowd stampedes in public gatherings—like religious events, concerts, or festivals—can result in catastrophic loss of life.  
The challenge is to:
- **Detect high crowd density zones early**
- **Monitor crowd flow direction and velocity**
- **Provide live alerts to security teams**

Traditional manual monitoring is too slow.  
Our system brings **AI automation** to make real-time decisions possible.

---

## 🧩 Key Features

| Feature | Description |
|----------|-------------|
| 🧍‍♂️ **Crowd Detection** | Detects and tracks individuals in each frame using YOLOv8 + ByteTrack |
| 📈 **Density Estimation** | Computes crowd density heatmaps and grid-based occupancy metrics |
| 🔄 **Flow Tracking** | Estimates motion vectors of tracked individuals to detect abnormal flow |
| 🚨 **Alert System** | Triggers alerts when density thresholds exceed safe limits |
| 💻 **Real-Time Dashboard** | Displays live density data and trends on a web UI (React + Vite) |
| ☁️ **Scalable Architecture** | Modularized microservices via Docker Compose for easy deployment |

---

## 🏗️ System Architecture

┌────────────────┐ HTTP (JSON) ┌─────────────────┐ WebSocket ┌───────────────────┐
│ AI Service │ ───────────────────▶ │ FastAPI API │ ───────────────▶ │ React Dashboard │
│ (YOLO + ByteTrack) │ │ (Ingest + WS) │ │ (Vite + WebSocket) │
└────────────────┘ └─────────────────┘ └───────────────────┘
▲ │
│ ▼
Video Feed Alert Logic
(Camera / File) (Density Threshold)


---

## ⚙️ Tech Stack

| Layer | Technology |
|--------|-------------|
| 🎥 **Object Detection** | [YOLOv8](https://github.com/ultralytics/ultralytics) |
| 🔁 **Tracking** | [ByteTrack](https://github.com/ifzhang/ByteTrack) |
| 🧮 **AI Frameworks** | PyTorch, OpenCV, NumPy |
| ⚙️ **Backend API** | FastAPI (Python) |
| 🌐 **Frontend** | React + Vite + Tailwind |
| 🔌 **Communication** | REST + WebSocket |
| 🐳 **Deployment** | Docker + Docker Compose |

---

## 🧱 Folder Structure



crowd-density-tracker/
├── ai/
│ ├── inference_bytrack.py # YOLO + ByteTrack detection logic
│ ├── requirements.txt
│ └── Dockerfile
├── backend/
│ ├── main.py # FastAPI backend (WebSocket + Ingest)
│ ├── requirements.txt
│ └── Dockerfile
├── frontend/
│ ├── src/
│ │ ├── App.jsx # Dashboard UI
│ │ └── hooks/useLive.js # Live WebSocket hook
│ ├── package.json
│ ├── vite.config.js
│ └── Dockerfile
├── data/
│ └── sample.mp4 # Sample test video
├── docker-compose.yml
└── README.md


---

## 🧠 How It Works (Step-by-Step)

1. **AI Inference**
   - YOLOv8 detects humans in each video frame.
   - ByteTrack assigns consistent IDs for each person.
   - System calculates crowd density and movement vectors.

2. **Backend API**
   - Receives live data from AI service via `/ingest` endpoint.
   - Broadcasts density metrics to all frontend clients using WebSockets.

3. **Frontend Dashboard**
   - Connects to backend WebSocket (`/ws/live`).
   - Displays live density metrics, timestamps, and alert statuses.

---

## 🚀 How to Run Locally (Docker)

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- (Optional) NVIDIA GPU drivers if you want to enable CUDA acceleration

### Steps
```bash
# Clone this repository
git clone https://github.com/<your-username>/crowd-density-tracker.git
cd crowd-density-tracker

# Add a sample video
mkdir -p data
wget -O data/sample.mp4 https://samplelib.com/lib/preview/mp4/sample-5s.mp4

# Start all containers
docker compose up --build


Then visit:

Frontend: http://localhost:5173

Backend API: http://localhost:8000/docs

🧩 Example Output
ai-1       | Processed 10 frames...
backend-1  | Received density data from cam1
frontend-1 | Live updates displayed in dashboard ✅

💡 Future Enhancements

Add Heatmap Visualization on video frames

Integrate real RTSP camera feeds

Add Geo-tagging for multi-camera zones

Use Kafka for scalable event streaming

Integrate AI anomaly detection for panic detection

🧑‍💻 Contributors
Name	Role	Area
Your Name	Team Lead / AI Developer	YOLO + ByteTrack Integration
Teammate 2	Backend Developer	FastAPI + Data Pipeline
Teammate 3	Frontend Developer	React Dashboard
Teammate 4	ML Engineer	Flow Estimation, Heatmaps
🏁 Hackathon Implementation Plan
Phase	Goal	Duration
Phase 1	Set up repo, Docker, base pipeline	1 day
Phase 2	Integrate YOLOv8 + ByteTrack	1 day
Phase 3	FastAPI WebSocket + REST endpoints	0.5 day
Phase 4	React Dashboard (live updates)	1 day
Phase 5	Testing + Demo prep	0.5 day
🛠️ Learning & Understanding

During development, we explored:

Computer Vision fundamentals — object detection, optical flow, density mapping

Multi-object tracking (MOT) — using ByteTrack for real-world reliability

Real-time communication — with FastAPI WebSockets

Frontend reactivity — via custom React hooks (useLive.js)

🧾 License

This project is open-source under the MIT License — feel free to modify and expand for educational or research purposes.

“Smart crowd monitoring can save lives — AI makes it possible in real time.” 🧠
