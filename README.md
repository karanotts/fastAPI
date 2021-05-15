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
    
