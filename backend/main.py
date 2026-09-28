from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta

app = FastAPI(title="Enterprise BPA API")

# Konfigurasi CORS agar Next.js bisa mengambil data
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/dashboard")
def get_dashboard_data():
    return {
        "sla_health": 94.5,
        "active_requests_progress": 70, # 70% completed
        "expiring_controls": [
            {"id": "C1", "name": "ISO27001 Renewal", "days_left": 25, "risk": "High"},
            {"id": "C2", "name": "SOC2 Access Review", "days_left": 12, "risk": "Critical"}
        ]
    }

@app.get("/api/approvals")
def get_pending_approvals():
    return [
        {"id": "REQ-101", "type": "CapEx", "requester": "John Doe", "priority": "P1", "sla_status": "Breach < 2h", "time_left": "1h 45m"},
        {"id": "REQ-102", "type": "Vendor Onboarding", "requester": "Jane Smith", "priority": "P2", "sla_status": "Due Soon", "time_left": "8h 10m"},
        {"id": "REQ-103", "type": "IT Access", "requester": "Mike Johnson", "priority": "P3", "sla_status": "On Track", "time_left": "24h+"},
    ]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)