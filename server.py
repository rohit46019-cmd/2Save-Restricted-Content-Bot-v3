from aiohttp import web

async def index(request):
    return web.Response(text="Bot running")

app = web.Application()
app.router.add_get("/", index)

if __name__ == "__main__":
    web.run_app(app, port=10000)