# Contact booklet API
---

### Get API

```
List

http://localhost:3000/contacts/

By ID

http://localhost:3000/contacts/<id>

```

##### Response:

```
[
  {
    "id": 1,
    "name": "String",
    "note": "String",
    "phoneNumber": "String"
  }
  ...
]
```

#### Request with 

```
http://localhost:3000/contacts/
```

```
Send CRUD request with:
app.delete(http://localhost:3000/contacts/<id>)
app.put(http://localhost:3000/contacts/<id>,body)
app.post(http://localhost:3000/contacts/,body)
```
