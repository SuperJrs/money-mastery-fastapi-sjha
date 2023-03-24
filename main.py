from fastapi import FastAPI
from controllers.conta import router as router_conta
from controllers.meta import router as router_meta

app = FastAPI()

app.include_router(router_conta)
app.include_router(router_meta)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=3005, reload=True)
