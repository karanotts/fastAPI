# fastAPI
Learning FastAPI - https://fastapi.tiangolo.com/tutorial/

<hr>

## Installing FastAPI:

    pipenv install fastapi[all]

or 

    pipenv install fastapi
    pipenv install uvcorn

## First Steps: <br>

### Step 1: Import ```FastAPI```

    from fastapi import FastAPI

### Step 2: Create a ```FastAPI``` instance:

    app = FastAPI()

### Step 3: Define a <strong>path</strong> <i>(route)</i> <strong>operation</strong> <i>(HTTP method)</i> decorator:

    @app.get("/")

-- where <strong>get</strong> is the operation, and <strong>/</strong> is the path. 

There are more operations available:
```
@app.post()
@app.put()
@app.delete()
@app.options()
@app.head()
@app.patch()
@app.trace()
```

### Step 4: Define <strong>path operation function</strong> and return the content:


"normal": 

    def root():
        return {"message": "Hello World"}

or concurrent:

    async def root():
        return {"message": "Hello concurrent World}
    

Example:
```
@app.get("/items/{item_id}")
async def get_items(item_id: int:
    return {"item_id": item_id}
```

### Step 5: Start the webserver

```
uvicorn main:app --reload
```

### Step 6: Check the API!
```

$ curl http://127.0.0.1:8000/items/1
{"item_id":1}

$ curl http://127.0.0.1:8000/items/hello
{"detail":[{"loc":["path","item_id"],"msg":"value is not a valid integer","type":"type_error.integer"}]}

```
![API](images/api_intro.png?raw=true "Swagger API GUI")