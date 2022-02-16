# e-commerce-platform
*  python manage.py startapp ecommerce
* python manage.py makemigrations
* python manage.py migrate
* python manage.py createsuperuser
* python manage.py runserver

# Introduction
The project is the backend of an ecommerce application containing APIs and Database for the same.
## List of Features
* User registeration and login
* Product orders
* Wishlist and cart
* Product reviews
* Report generation
* Email notification

# Approach
* Used django rest framework
* CSR
* Database feature by mysql
* Project setup by django-admin startproject
* File storage in cloud(eg- AWS S3)
* Frontend comprise of Angular or React for the app to interact with backend

# Merits of CSR
* Common backend for web,android and IOS app.
* Modern way to interact with server using rest APIs

# Database design
## User
| Attribute   | Datatype      | Description             |
| ----------- | ------------- | ----------------------- |
| userId      | AutoField     | Primary key             |
| userType    | CharField     | vendor or customer      |
| name        | CharField     | Name of user            |
| address     | CharField     | Address of user         |
| phoneNumber | CharField     | Exact 10 digits         |
| email       | CharField     | unique key              |
| status      | BooleanField  | Soft deletion of user   |
| createdTs   | DateTimeField | User creation timestamp |

## Product
| Attribute          | Datatype      | Description                |
| ------------------ | ------------- | -------------------------- |
| productId          | AutoField     | primary key                |
| vendorId           | IntegerField  | foreign key                |
| productName        | CharField     | Name of product            |
| productImageURL    | CharFIeld     | URL of product image       |
| price              | IntegerField  | price of product           |
| productQuantity    | IntegerField  | quantity of product        |
| productDescription | CharFIeld     | Description of product     |
| productUnit        | CharField     | Unit of product            |
| createdTs          | DateTImeField | Product creation timestamp |

## Order
| Attribute              | DataType        | Description                 |
| ---------------------- | --------------- | --------------------------- |
| orderId                | AutoField       | primary key                 |
| orderNumber            | IntegerField    | unique key                  |
| productId              | IntegerField    | foreign key                 |
| userId                 | IntegerField    | foreign key                 |
| orderedProductQuantity | IntegerField    | quantity of product ordered |
| orderedProductUnit     | CharField       | unit of the product ordered |
| status                 | CharField(enum) | status of order             |
| createdTs              | DateTImeField   | order creation timestamp    |


## Review
| Attribute | DataType           | Description               |
| --------- | ------------------ | ------------------------- |
| reviewId  | AutoField          | primary key               |
| userId    | IntegerField       | foreign key               |
| comment   | CharField          | content of the review     |
| rating    | IntegerField(enum) | rating given              |
| productId | IntegerField       | foriegn key               |
| createdTs | DateTimeFIeld      | review creation timestamp |


## Shopping Cart
| Attribute       | DataType        | Description                 |
| --------------- | --------------- | --------------------------- |
| entryId         | AutoField       | primary key                 |
| productId       | IntegerField    | foreign key                 |
| userId          | IntegerField    | foriegn key                 |
| productQuantity | IntegerField    | quantity of product in cart |
| status          | CharFIeld(enum) | status of product in cart   |


## Wishlist
| Attribute       | DataType        | Description                     |
| --------------- | --------------- | ------------------------------- |
| entryId         | AutoFIeld       | primary                         |
| productId       | IntegerField    | foreign key                     |
| userId          | IntegerField    | foreign key                     |
| productQuantity | IntegerField    | quantity of product in wishlist |
| status          | CharField(enum) | status of product in wishlist   |


# Access Patterns
| Serial No. | Secure   | Entity         | Method | URi                                    | Details                                                  | Build Prority |
| ---------- | -------- | -------------- | ------ | -------------------------------------- | -------------------------------------------------------- | ------------- |
|            |          |                |        |                                        |                                                          |               |
| 1          | Secure   | user           | GET    | /user                                  | give info of that user                                   | H             |
| 2          | Secure   |                | POST   | /user                                  | add a new user                                           | M             |
| 3          | Secure   |                | PATCH  | /user                                  | update his details                                       | L             |
| 4          | Secure   |                | DELETE | /user                                  | delete user                                              | L             |
|            |          |                |        |                                        |                                                          |               |
|            |          |                |        |                                        |                                                          |               |
| 5          | Insecure | product        | GET    | /product                               | list of products                                         | H             |
| 6          | Secure   |                | POST   | /product                               | create new product                                       | M             |
|            |          |                |        |                                        |                                                          |               |
|            |          |                |        |                                        |                                                          |               |
| 7          | Insecure | product by id  | GET    | /product/{productId}                   | given a productId, give details of that product          | M             |
| 8          | Secure   |                | PATCH  | /product/{productId}                   | given a productId, update details of that product        | M             |
| 9          | Secure   |                | DELETE | /product/{productId}                   | given a productId,delete that product                    | L             |
|            |          |                |        |                                        |                                                          |               |
|            |          |                |        |                                        |                                                          |               |
| 10         | Secure   | order          | GET    | /order                                 | given a userId, get all orders placed                    | L POC         |
| 11         | Secure   |                | POST   | /order                                 | add an order                                             | H             |
|            |          |                |        |                                        |                                                          |               |
|            |          |                |        |                                        |                                                          |               |
| 12         | Secure   | order by id    | GET    | /order/{orderId}                       | given an order id,get a specific order                   | M             |
| 13         | Secure   |                | PATCH  | /order/{orderId}                       | given an order id,update a specific order                | L POC         |
| 14         | Secure   |                | DELETE | /order/{orderId}                       | given an order id set the status of order to cancelled   | L POC         |
|            |          |                |        |                                        |                                                          |               |
|            |          |                |        |                                        |                                                          |               |
| 15         | Insecure | review         | GET    | /product/{productId}/review            | given a product id,get all reviews                       | M Not in POC  |
| 16         |          |                | POST   | /product/{productId}/review            | given a product id,add a new review                      | M Not in POC  |
|            |          |                |        |                                        |                                                          |               |
|            |          |                |        |                                        |                                                          |               |
| 17         | Insecure | review by id   | GET    | /product/{productId}/review/{reviewId} | given a product id and review id,get a particular review | L             |
| 18         | Secure   |                | PATCH  | /product/{productId}/review/{reviewId} | given a product id and review id, update a review        | L             |
| 19         | Secure   |                | DELETE | /product/{productId}/review/{reviewId} | given a product id and review id, delete review          | L             |
|            |          |                |        |                                        |                                                          |               |
|            |          |                |        |                                        |                                                          |               |
| 20         | Secure   | wishlist       | GET    | /wishlist-entry                        | get wishlist of customer                                 | L POC         |
| 21         | Secure   |                | POST   | /wishlist-entry                        | add item to wishlist                                     | L POC         |
|            |          |                |        |                                        |                                                          |               |
|            |          |                |        |                                        |                                                          |               |
| 22         | Secure   | wishlist by id | GET    | /wishlist-entry/{entryId}              | given an entry id,get an item from wishlist of customer  | L             |
| 23         | Secure   |                | PATCH  | /wishlist-entry/{entryId}              | given an entry id, update wishlist item                  | L             |
| 24         | Secure   |                | DELETE | /wishlist-entry/{entryId}              | given an entry id, delete item from wishlist             | L POC         |
|            |          |                |        |                                        |                                                          |               |
|            |          |                |        |                                        |                                                          |               |
| 25         | Secure   | cart           | GET    | /cart-entry                            | get items in cart of customer                            | L POC         |
| 26         | Secure   |                | POST   | /cart-entry                            | add to cart                                              | L POC         |
| 27         | Secure   |                |        |                                        |                                                          |               |
| 28         | Secure   |                |        |                                        |                                                          |               |
|            |          |                |        |                                        |                                                          |               |
|            |          |                |        |                                        |                                                          |               |
| 29         |          | cart by id     | GET    | /cart-entry/{entryId}                  | get info about a cart entry                              | L             |
| 30         |          |                | PATCH  | /cart-entry/{entryId}                  | update a cart entry                                      | L             |
| 31         |          |                | DELETE | /cart-entry/{entryId}                  | remove a cart entry                                      | L POC         |

* The above table consists of all required access patterns for the app.
* Currently implemented pattern number 1,5,6,7
* H - High
* M - Medium
* L - Low
* POC - Proof of concept

#Authentication
* Will be implementing Oauth in the future. Currently, userId is directly passed in the authorization header instead of JWT token because:
1) I don't have complete understanding of Oauth
2) So, doing what I know and leaaring other things in the process.
