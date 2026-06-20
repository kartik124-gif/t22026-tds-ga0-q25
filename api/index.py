from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np
import json

app = FastAPI()

# Enable CORS for POST from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)

TELEMETRY_DATA = json.loads("""
[
  {"region": "apac", "service": "support",         "latency_ms": 147.13, "uptime_pct": 99.101, "timestamp": 20250301},
  {"region": "apac", "service": "checkout",        "latency_ms": 171.45, "uptime_pct": 99.13,  "timestamp": 20250302},
  {"region": "apac", "service": "support",         "latency_ms": 228.76, "uptime_pct": 99.035, "timestamp": 20250303},
  {"region": "apac", "service": "checkout",        "latency_ms": 129.92, "uptime_pct": 98.076, "timestamp": 20250304},
  {"region": "apac", "service": "payments",        "latency_ms": 111.74, "uptime_pct": 98.421, "timestamp": 20250305},
  {"region": "apac", "service": "support",         "latency_ms": 168.8,  "uptime_pct": 97.499, "timestamp": 20250306},
  {"region": "apac", "service": "payments",        "latency_ms": 120.24, "uptime_pct": 97.912, "timestamp": 20250307},
  {"region": "apac", "service": "payments",        "latency_ms": 169.55, "uptime_pct": 99.013, "timestamp": 20250308},
  {"region": "apac", "service": "payments",        "latency_ms": 219.12, "uptime_pct": 97.682, "timestamp": 20250309},
  {"region": "apac", "service": "support",         "latency_ms": 196.51, "uptime_pct": 98.839, "timestamp": 20250310},
  {"region": "apac", "service": "payments",        "latency_ms": 187.74, "uptime_pct": 99.123, "timestamp": 20250311},
  {"region": "apac", "service": "recommendations", "latency_ms": 200.4,  "uptime_pct": 97.527, "timestamp": 20250312},
  {"region": "emea", "service": "checkout",        "latency_ms": 124.2,  "uptime_pct": 98.896, "timestamp": 20250301},
  {"region": "emea", "service": "checkout",        "latency_ms": 164.64, "uptime_pct": 97.479, "timestamp": 20250302},
  {"region": "emea", "service": "checkout",        "latency_ms": 138.97, "uptime_pct": 98.306, "timestamp": 20250303},
  {"region": "emea", "service": "checkout",        "latency_ms": 198.57, "uptime_pct": 97.394, "timestamp": 20250304},
  {"region": "emea", "service": "analytics",       "latency_ms": 194.69, "uptime_pct": 97.202, "timestamp": 20250305},
  {"region": "emea", "service": "payments",        "latency_ms": 190.72, "uptime_pct": 98.427, "timestamp": 20250306},
  {"region": "emea", "service": "support",         "latency_ms": 173.24, "uptime_pct": 97.338, "timestamp": 20250307},
  {"region": "emea", "service": "support",         "latency_ms": 172.39, "uptime_pct": 98.676, "timestamp": 20250308},
  {"region": "emea", "service": "support",         "latency_ms": 125.17, "uptime_pct": 99.017, "timestamp": 20250309},
  {"region": "emea", "service": "catalog",         "latency_ms": 118.5,  "uptime_pct": 99.023, "timestamp": 20250310},
  {"region": "emea", "service": "recommendations", "latency_ms": 176.1,  "uptime_pct": 99.036, "timestamp": 20250311},
  {"region": "emea", "service": "support",         "latency_ms": 119.56, "uptime_pct": 97.239, "timestamp": 20250312},
  {"region": "amer", "service": "support",         "latency_ms": 121.26, "uptime_pct": 98.748, "timestamp": 20250301},
  {"region": "amer", "service": "catalog",         "latency_ms": 235.58, "uptime_pct": 98.904, "timestamp": 20250302},
  {"region": "amer", "service": "recommendations", "latency_ms": 170.91, "uptime_pct": 97.91,  "timestamp": 20250303},
  {"region": "amer", "service": "payments",        "latency_ms": 121.88, "uptime_pct": 97.535, "timestamp": 20250304},
  {"region": "amer", "service": "catalog",         "latency_ms": 166.18, "uptime_pct": 98.623, "timestamp": 20250305},
  {"region": "amer", "service": "recommendations", "latency_ms": 184.11, "uptime_pct": 97.551, "timestamp": 20250306},
  {"region": "amer", "service": "analytics",       "latency_ms": 169.17, "uptime_pct": 98.107, "timestamp": 20250307},
  {"region": "amer", "service": "analytics",       "latency_ms": 171.76, "uptime_pct": 97.175, "timestamp": 20250308},
  {"region": "amer", "service": "analytics",       "latency_ms": 148.03, "uptime_pct": 97.594, "timestamp": 20250309},
  {"region": "amer", "service": "catalog",         "latency_ms": 129.71, "uptime_pct": 97.58,  "timestamp": 20250310},
  {"region": "amer", "service": "support",         "latency_ms": 163.88, "uptime_pct": 97.139, "timestamp": 20250311},
  {"region": "amer", "service": "payments",        "latency_ms": 185.9,  "uptime_pct": 99.473, "timestamp": 20250312}
[
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 177.74,
    "uptime_pct": 98.862,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 133.15,
    "uptime_pct": 99.254,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 210.06,
    "uptime_pct": 99.258,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 155.09,
    "uptime_pct": 98.123,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 123.97,
    "uptime_pct": 97.969,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 206.2,
    "uptime_pct": 99.398,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 122.92,
    "uptime_pct": 98.787,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 156.65,
    "uptime_pct": 97.247,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 136.41,
    "uptime_pct": 99.18,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 220.86,
    "uptime_pct": 99.161,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 174.52,
    "uptime_pct": 97.78,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 153.03,
    "uptime_pct": 97.553,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 188.03,
    "uptime_pct": 98.46,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 149.51,
    "uptime_pct": 97.453,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 102.8,
    "uptime_pct": 97.625,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 204.84,
    "uptime_pct": 98.658,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 174.03,
    "uptime_pct": 98.228,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 124.8,
    "uptime_pct": 99.329,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 134.33,
    "uptime_pct": 97.368,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 235.01,
    "uptime_pct": 98.294,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 203.41,
    "uptime_pct": 97.59,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 221.55,
    "uptime_pct": 98.336,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 162.31,
    "uptime_pct": 99,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 203.04,
    "uptime_pct": 97.873,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 205.33,
    "uptime_pct": 97.557,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 111.78,
    "uptime_pct": 97.622,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 202.44,
    "uptime_pct": 99.228,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 184.42,
    "uptime_pct": 98.45,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 184.07,
    "uptime_pct": 98.969,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 154.24,
    "uptime_pct": 97.422,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 193.19,
    "uptime_pct": 98.765,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 211.73,
    "uptime_pct": 99.215,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 178.12,
    "uptime_pct": 99.309,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 123.58,
    "uptime_pct": 99.176,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 130.3,
    "uptime_pct": 99.12,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 129.66,
    "uptime_pct": 97.913,
    "timestamp": 20250312
  }
]
""")

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []
    for region in regions:
        records   = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes   = [r["uptime_pct"]  for r in records]
        results.append({
            "region":      region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime":  round(float(np.mean(uptimes)), 3),
            "breaches":    int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}
