from aiohttp import web
from asyncworker import App, RouteTypes

app = App("", "", "", 1)


@app.route(["/"], type=RouteTypes.HTTP, methods=["POST"])
async def operation(request: web.Request):
    data = await request.json()
    return {"result": data["left"] - data["right"]}
