import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],

  // Configure the dev server
  server: {
    host: "0.0.0.0",
    port: 5173, // default Vite port
    strictPort: true,

    // Proxy API requests to FastAPI backend (for local dev)
    proxy: {
      "/api": {
        target: "http://localhost:8000",
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ""),
      },
      "/ws": {
        target: "ws://localhost:8000",
        ws: true, // enable WebSocket proxy
      },
    },
  },

  // Optional: build output
  build: {
    outDir: "dist",
    sourcemap: true,
  },
});
