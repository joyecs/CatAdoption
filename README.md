# non profit site for cats
# Cat Adoption Site API


## Cats

    JSON
        {
          "breed": string,
          "age": string,
          "color": string,
          "image": image file

        }

### Get all cats
**Link**: cats/api/cats/
**Method**: GET
**Request**:
**Return**: All cats in DB
### Get a cat with id
**Link**: cats/api/cats/1(id)
**Method**: GET
**Request**:
**Return**: A cat in DB
### Post a cat
**Link**: cats/api/cats/
**Method**: POST
**Request**:
**Return**: The cat in DB

## Customers API
    JSON
        {
			"id": int,
			"name": string,
			"phone": string,
			"email": string,
			"address": string,
			"annual_income": int,
			"reason_to_adopt_cats": string
        }

### Get all cats
**Link**: customers/
**Method**: GET
**Request**:
**Return**: All customers in DB
### Get a customer with id
**Link**: customers /1(id)
**Method**: GET
**Request**:
**Return**: A customer  in DB
### Post a customer
**Link**: customers/
**Method**: POST
**Request**:
**Return**: The customer in DB
