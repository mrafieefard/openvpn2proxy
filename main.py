from fastapi import FastAPI,HTTPException
import uvicorn

from type import ConfigResponse,ActivePayload
from common import get_configs_list,active_config,start_up,deactive

app = FastAPI()

@app.get("/configs_list")
async def get_configs_list_route():
    configs = get_configs_list()
    return ConfigResponse(configs=configs)

@app.post("/active")
async def set_active_route(payload : ActivePayload):
    is_active = active_config(payload.name)
    
    if is_active:
        raise HTTPException(status_code=200,detail="success")
    else:
        raise HTTPException(status_code=500,detail="failed")
    
@app.post("/deactive")
async def set_active_route(payload : ActivePayload):
    is_deactive = deactive(payload.name)
    
    if is_deactive:
        raise HTTPException(status_code=200,detail="success")
    else:
        raise HTTPException(status_code=500,detail="failed")
    

if __name__ == "__main__":
    start_up()
    uvicorn.run(app)