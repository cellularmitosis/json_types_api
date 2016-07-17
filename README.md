# json_types_api
An API which returns each of the valid JSON types as the root object of the response.

## Usage

Run this in a terminal:

```
./api.py
```

Then open up a web browser and open [http://127.0.0.1:5000]().

## Endpoints (and responses):

* http://127.0.0.1:5000/null

```json
null
```

* http://127.0.0.1:5000/number

```json
3.14159
```

* http://127.0.0.1:5000/string

```json
"Hello, world!"
```

* http://127.0.0.1:5000/boolean

```json
true
```

* http://127.0.0.1:5000/array

```json
[2,3,5,7,11,13,17]
```

* http://127.0.0.1:5000/object

```json
{"one": 1, "two": 2, "three": 3}
```



