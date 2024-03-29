# ZakerFit WebApplication project

## Introduction:

ZakerFit Project is a web application service that has made by Django and Django Rest Framework.
This project is for CrossFit Gym, and designed for coaches, trainers and players to sign in and create their own
account, shopping section and Online Training plans, and some other features that explains in this Document later.
Hope You enjoy and if you have an idea, contact with me with amirmahdikahdooi@gmail.com.

## Endpoints:

- /accounts/get-verification-code/

__Allowed Method__: `POST`

In this Endpoint you're able to send verification code to users,
We Use Kavenegar to send SMS verifications, you can visit their website in [Here](https://kavenegar.com/).

Your sending data should be something like this:

```json
{
  "phone_number": "9123456789"
}
```

And Output Will contained Phone Number and Verification Code:

```json
{
  "phone_number": "9123456789",
  "verification_code": "123456"
}
```

- /accounts/confirm-verification-code/

__Allowed Method__: `POST`

In this Endpoint, you can send phone number and verification code to this endpoint, then check the timeout, phone number
and code that have been sent, and validate phone number and return a 32 character code to registering new user by using
it.

__Note:__ if phone number was already validate, return `409 HTTP Response`

Your sending data should be something like this:

```json
{
  "phone_number": "9123456789",
  "validation_code": "123456"
}
```

Output Will be something like this if User Does not exist:

```json
{
  "phone_number": "9123456789",
  "verify_token": "32 char Token"
}
```

- /accounts/get-verify-token/

__Allowed Method__: `POST`

In this Endpoint, you can verify_token by the number that you have get verification code and validate as a
valid number in model.

__Note:__ if the phone number was not valid yet, you get `404 HTTP Not Found` and if phone_number has no verify_token
response will be `401 HTTP Unauthorized`.

Your sending data should be something like this:

```json
{
  "phone_number": "9123456789"
}
```

Output Will be something like this if User Does not exist:

```json
{
  "verify_token": "32 char Token"
}
```

- /accounts/register/

In this EndPoint you can use your validated mobile phone number to register into Website.

__Allowed Method:__ `POST`

__JSON data that you post must have this required fields:__

1. phone_number
2. first_name
3. last_name
4. gender (Which in number, __1 for Male__ and __2 for Female__)
5. password1
6. password2
7. verify_token

__This Fields also can send, but are not required:__

1. email
2. age

**Example:**

```json
{
  "phone_number": "9123456789",
  "first_name": "Amir",
  "last_name": "Kahdouii",
  "gender": 1,
  "email": "example@info.com",
  "age": 18,
  "passsword1": "********",
  "passsword2": "********",
  "verify_token": "32 char token"
}
```

**Response:**

If user create successfully, you will get `HTTP 201 Created`, and user object like below:

```json
{
  "phone_number": "9123456789",
  "email": "example@info.com",
  "first_name": "Amir",
  "last_name": "Kahdouii",
  "gender": 1,
  "age": 18
}
```

- /accounts/token/

In This endpoint you can get JWT Token by sending phone_number and password data.

__Allowed Method:__ `POST`

__Note:__ Access token lifetime was change into 10 minutes, you can change it in **config/settings.py**

Sending Data Example:

```json
{
  "phone_number": "9123456789",
  "password": "********"
}
```

Output Example:

```json
{
  "access": "access token",
  "refresh": "refresh token"
}
```

- /accounts/token/refresh/

In This endpoint you can get New access Token by using refresh token.

__Allowed Method:__ `POST`

Sending Data Example:

```json
{
  "refresh": "refresh token"
}
```

Output Example:

```json
{
  "access": "new access token"
}
```

## Todo:

- [x] Customize User model
- [x] Complete Authentication system, such as: admin panel, model managers,...
- [ ] Create Endpoints for authentications, verifying phone number and email and sign-in and register system
- [ ] Create Coach Permissions and Make Users as a Coach or trainer
- [ ] Create Login section for coaches
- [ ] Create HeadCoach Endpoints and permissions such as making users, trainers and...
- [ ] Make Profile Model for users
- [ ] Create Online shop section
- [ ] Create Online training Section
- [ ] Create videos tutorial section
- [ ] Create Picture gallery Section
- [ ] Choose class Section