# json_types_api
An API which returns each of the valid JSON types as the root object of the response.

## Usage

Run this in a terminal:

```
./api.py
```

Then open up a web browser and open [http://127.0.0.1:5000]().

## Endpoints (and responses):

* /null

```json
null
```

* /nubmer

```json
3.14159
```

* /string

```json
"Hello, world!"
```

* /boolean

```json
true
```

* /array

```json
[2,3,5,7,11,13,17]
```

* /object

```json
{"one": 1, "two": 2, "three": 3}
```



