import { useState, useEffect } from "react";

export default function App() {
  const [data, setData] = useState(null);
  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8000/ws/live");
    ws.onmessage = (e) => setData(JSON.parse(e.data));
    return () => ws.close();
  }, []);
  return (
    <div className="p-6 text-center">
      <h1 className="text-2xl font-bold mb-4">AI Crowd Tracker Dashboard</h1>
      {data ? (
        <>
          <p>Camera: {data.camera}</p>
          <p>Density: {data.density}</p>
          <p>Timestamp: {new Date(data.ts * 1000).toLocaleTimeString()}</p>
        </>
      ) : (
        <p>Waiting for live data...</p>
      )}
    </div>
  );
}
