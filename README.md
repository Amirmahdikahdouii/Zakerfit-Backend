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
and code that have been sent. Then if phone number was already registered, return the user and if it's not, return
nothing.

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

And if user exists:

```json
{
  "phone_number": "9123456789",
  "user": {
    "phone_number": "9123456789",
    "email": "example@info.com",
    "first_name": "User First name",
    "last_name": "User Last name"
  }
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