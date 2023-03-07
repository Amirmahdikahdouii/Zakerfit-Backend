# ZakerFit WebApplication project

## Introduction:

ZakerFit Project is a web application service that has made by Django and Django Rest Framework.
This project is for CrossFit Gym, and designed for coaches, trainers and players to sign in and create their own
account, shopping section and Online Training plans, and some other features that explains in this Document later.
Hope You enjoy and if you have an idea, contact with me with amirmahdikahdooi@gmail.com.

## Endpoints:

- /accounts/get-verification-code/

##### Allowed Method: `POST`

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

##### Allowed Method: `POST`

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
  "verification_code": "123456"
}
```

And if user exists:

```json
{
  "phone_number": "9123456789",
  "verification_code": "123456",
  "user": {
    "phone_number": "9123456789",
    "email": "example@info.com",
    "first_name": "User First name",
    "last_name": "User Last name"
  }
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