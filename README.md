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