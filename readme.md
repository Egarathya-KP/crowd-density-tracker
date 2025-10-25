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

