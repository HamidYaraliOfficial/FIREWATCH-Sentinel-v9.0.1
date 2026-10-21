from fastapi import FastAPI, Form, Request, Response
from fastapi.responses import HTMLResponse, JSONResponse
app=FastAPI(title='FIREWATCH Demo Target',version='2.0-demo')
@app.middleware('http')
async def weak_cors(request:Request,call_next):
    response=await call_next(request)
    origin=request.headers.get('origin')
    if origin: response.headers['Access-Control-Allow-Origin']=origin; response.headers['Access-Control-Allow-Credentials']='true'
    return response
@app.get('/',response_class=HTMLResponse)
def home():
    return '''<html><head><title>Demo Target</title></head><body><h1>FIREWATCH Demo Target</h1><p>Intentional weaknesses for local testing.</p><form action="/login" method="post"><input name="username"><input name="password" type="password"><button>Login</button></form><script src="http://cdn.example.invalid/demo.js"></script><a href="/set-cookie">Set cookie</a><a href="/admin/panel">Admin</a><a href="/api/users/1">User 1</a></body></html>'''
@app.get('/admin/panel')
def admin(): return {'admin':True,'message':'demo only'}
@app.get('/api/users/1')
def user(): return {'id':1,'name':'demo','email':'demo@example.invalid'}
@app.get('/set-cookie')
def set_cookie(response:Response): response.set_cookie('session_id','demo-value'); return {'ok':True}
@app.post('/login')
def login(username:str=Form(...),password:str=Form(...)): return {'ok':False,'message':'Demo only'}
@app.get('/graphql')
def graphql_get(): return {'data':{'status':'demo'}}
@app.post('/graphql')
async def graphql_post(request:Request):
    payload=await request.json()
    q=str(payload.get('query',''))
    if '__schema' in q:
        return JSONResponse({'data':{'__schema':{'queryType':{'name':'Query'},'mutationType':None,'types':[{'name':'Query','kind':'OBJECT','fields':[{'name':'user'}]},{'name':'User','kind':'OBJECT','fields':[{'name':'id'},{'name':'email'}]}]}}})
    return {'data':{'user':{'id':1}}}
@app.get('/robots.txt')
def robots(): return Response('User-agent: *\nAllow: /\n',media_type='text/plain')
@app.get('/security.txt')
def security(): return Response('Contact: security@example.invalid\n',media_type='text/plain')
