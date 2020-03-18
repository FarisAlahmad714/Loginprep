from django.db import models
import re
# from datetime import date, datetime


# class ShowManager(models.Manager):
#     def basic_validator(self, post_data):
#         errors = {}

#      if len(post_data["title"]) < 2:
#     error["title"] = "Please enter at least 2 characters or the title. "

#     if len(post_data["network"]) < 3:
#     error["network"] = "Please enter at least 2 characters or the network. "

#     if len(post_data["desc"]) < 10:
#     error["desc"] = "Please enter at least 10 characters or the description. "

#     return errors

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def validator(self, data):
        errors = {}
        if len(data['fname']) < 2:
            errors['fname'] = "First name has to be 2 chars"
        if len(data['lname']) < 2:
            errors['lname'] = "Last name has to be 2 chars"
        if not EMAIL_REGEX.match(data['email']):
            errors['email'] = "Email is invalid"
        if data['password'] != data['cpassword']:
            errors['password'] = "Password do not match"
        if len(data['password']) < 8:
            errors['password'] = "Password is too short"
        return errors


class Users(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return f"user: {self.first_name}, {self.last_name}, {self.password}"
