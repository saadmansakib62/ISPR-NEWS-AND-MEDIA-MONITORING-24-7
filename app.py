from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI(title="ISPR Command Media Monitoring API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/api/health")
def health():
    return {"status": "OPERATIONAL", "sources": 75, "sectors": 6}

@app.get("/api/rss")
async def proxy_rss(url: str = Query(...)):
    async with httpx.AsyncClient(timeout=10.0, follow_redirects=True) as client:
        r = await client.get(url)
        return {"status": r.status_code, "xml": r.text}
