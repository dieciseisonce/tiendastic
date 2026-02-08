from fastapi import FastAPI

app = FastAPI(title="Tiendastic Sync")

@app.get("/health")
def health():
    return {"ok": True}
