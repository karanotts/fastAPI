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

<br>
<hr>

# SAMPLE APP

## Create item function:
```
@app.post("/items")
def post_item(item: Item):
    db.append(item.dict())
    return db[-1]
```

## Create item using the API:
```
curl -X 'POST' \
  'http://127.0.0.1:8000/items' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "beach ball",
  "quantity": 1
}'
```

## Get all items function:
```
@app.get("/items")
def get_items():
    return db
```

## Get all items in the API:
```
curl -X 'GET' \
  'http://127.0.0.1:8000/items' \
  -H 'accept: application/json'

[{"name": "beach ball","quantity": 1}]
```

## Get an item by ID function:
```
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return db[item_id-1]
```

## Get an item by ID in the API:
```
curl -X 'GET' \
  'http://127.0.0.1:8000/items/1' \
  -H 'accept: application/json'

{"name":"beach ball","quantity":1}
```

## Delete an item by ID function:
```
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    db.pop(item_id-1)
    return db
```

## Delete an item by ID in the API:
```
curl -X 'DELETE' \
  'http://127.0.0.1:8000/items/1' \
  -H 'accept: application/json'

[]
```