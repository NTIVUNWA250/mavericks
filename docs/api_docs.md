# MOMO SMS REST API

This API allows interaction with the SMS records of This project designated to design a website that processes MoMo SMS data in XML format, clean and categorize the data, store it in a relational database, and offer a frontend interface to analyze and visualize the data to the user.

Using plain Python(http.server) we are able to extract records and it requires authentication for all write and read operations

### AUTHENTICATION

The API usees Basic Auth and it includes an Authorization header in every request made.

- **Username**: `admin`
- **Password**: `admin123`
- **Header Format**: `Authorization: Basic Yhfndionfio34mfdio=`

### API ENDPOOINTS

1. **List All Transactions**
   To list all transactions we use the following Endpoint:

- **Endpoint**: `GET /transactions`
- **Success Response**: `200 OK`
- **Output**:

```
[
  {
    "id": "76662021700",
    "type": "Transfer Received",
    "amount": 2000.0,
    "sender": "Jane Smith",
    "receiver": "Mobile Money User",
    "timestamp": "10 May 2024 4:30:58 PM"
  }

  {
    "id": "76662021702",
    "type": "Payment Sent",
    "amount": 1500.0,
    "sender": "John Smith",
    "receiver": "Mobile Money User",
    "timestamp": "13 May 2024 6:00:00 PM"
  }
]
```

2. **List one Transaction**
   To list one transactions we use the following Endpoint:

- **Endpoint**: `GET /transactions/{id}`
- **Success Response**: `200 OK`
- **Error Response**: `404 Not Found`

3. **Add All Transactions**
   To add a transactions we use the following Endpoint:

- **Endpoint**: `POST /transactions`
- **Request Body**:

```
  {
    "id": "766620217012",
    "type": "Payment",
    "amount": 100.0,
    "sender": "Group_10",
    "receiver": "Robert",
    "timestamp": "12 May 2024 2:30:58 PM"
  }
```

- **Success Response**: `201 Created`

4. **Update Transaction**
   To Update a record we use the following Endpoint:

- **Endpoint**: `PUT /transactions/{id}`
- **Success Response**: `200 OK`

5. **Delete Transactions**
   To remove a Record we use the following Endpoint:

- **Endpoint**: `DELETE /transactions/{id}`
- **Success Response**: `200 OK`
- **Output**: `{"message": "Record Deleted"}`

### Error Codes

| Code | Meaning      | Desc                                                                  |
| ---- | ------------ | --------------------------------------------------------------------- |
| 200  | OK           | Request has succeeded                                                 |
| 201  | Created      | Resource was added successfuly                                        |
| 400  | Bad Request  | Invalid JSON body or a field is missing                               |
| 401  | Unauthorized | Missing auth credentials                                              |
| 404  | Not Found    | The requested endpoint is not present or transaction ID doesnot exist |

The API usees Basic Auth and it includes an Authorization header in every request made.

1. **Authorization Guard**: every req made is supposed to pass through the `authenticate()` check before being allowed to reach the route logic
2. **INput Validation**: `POST` and `PUT` methods verifies that the req body is valid JSON
3. **Data integrity**: Transactions ID must be unique, if an existing ID is found it should return `404 Bad Request` when a `Post ` request is passed
