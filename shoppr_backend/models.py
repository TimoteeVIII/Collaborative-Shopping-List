from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username: str = models.CharField(max_length=50, null=False, unique=True)
    password: str = models.CharField(max_length=255, null=False)
    first_name: str = models.CharField(max_length=50, null=False)
    last_name: str = models.CharField(max_length=50, null=False)
    email: str = models.EmailField(max_length=255, null=False, unique=True)
    updated_at: datetime = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'User'


class Household(models.Model):
    name: str = models.CharField(max_length=50)
    password: str = models.CharField(max_length=50)
    adminId: int = models.IntegerField()
    created_at: datetime = models.DateTimeField(auto_now_add=True)
    updated_at: datetime = models.DateTimeField(auto_now=True)
    deleted_at: datetime = models.DateTimeField(null=True)

    class Meta:
        db_table = 'household'


class UserHouseholds(models.Model):
    user: User = models.ForeignKey(User, on_delete=models.CASCADE)
    household: Household = models.ForeignKey(Household, on_delete=models.CASCADE)
    created_at: datetime = models.DateTimeField(auto_now_add=True)
    updated_at: datetime = models.DateTimeField(auto_now=True)
    deleted_at: datetime = models.DateTimeField(null=True)

    class Meta:
        db_table = 'user_households'
        constraints = [models.UniqueConstraint(fields=['user', 'household'], name='unique_user_households')]


class ShoppingList(models.Model):
    uuid: str = models.CharField(unique=True, max_length=255)
    name: str = models.CharField(max_length=255)
    created_at: datetime = models.DateTimeField(auto_now_add=True)
    updated_at: datetime = models.DateTimeField(auto_now=True)
    deleted_at: datetime = models.DateTimeField(null=True)

    class Meta:
        db_table = 'shopping_list'


class ShoppingListItem(models.Model):
    name: str = models.CharField(max_length=255)
    completed: bool = models.BooleanField(default=False)
    shoppingList: ShoppingList = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    created_at: datetime = models.DateTimeField(auto_now_add=True)
    updated_at: datetime = models.DateTimeField(auto_now=True)
    deleted_at: datetime = models.DateTimeField(null=True)

    class Meta:
        db_table = 'shopping_list_item'


class HouseholdShoppingList(models.Model):
    household: Household = models.ForeignKey(Household, on_delete=models.CASCADE)
    shoppingList: ShoppingList = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    created_at: datetime = models.DateTimeField(auto_now_add=True)
    updated_at: datetime = models.DateTimeField(auto_now=True)
    deleted_at: datetime = models.DateTimeField(null=True)

    class Meta:
        db_table = 'household_shopping_list'


class RefreshToken(models.Model):
    user: User = models.ForeignKey(User, on_delete=models.CASCADE)
    refresh_token: str = models.CharField(max_length=255)
    active: bool = models.BooleanField(default=True)
    created_at: datetime = models.DateTimeField(auto_now_add=True)
    updated_at: datetime = models.DateTimeField(auto_now=True)
    deleted_at: datetime = models.DateTimeField(null=True)

    class Meta:
        db_table = 'refresh_token'
