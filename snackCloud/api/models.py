# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Role(models.Model):
	RoleID = models.AutoField(primary_key=True)
	RoleName = models.CharField(max_length = 40)
	Active = models.BooleanField()

class Product(models.Model):
	ProductID = models.AutoField(primary_key=True)
	ProductName = models.CharField(max_length = 40)
	Price = models.IntegerField()
	Active = models.BooleanField()
	def __unicode__(self):
		return self.ProductName

class User(models.Model):
	UserID = models.AutoField(primary_key=True)
	Username = models.CharField(max_length = 40)
	Password = models.CharField(max_length = 40)
	Email = models.EmailField()
	Phone = models.IntegerField()
	Points = models.IntegerField()
	SMS = models.CharField(max_length = 40)
	RoleID = models.ForeignKey(Role)
	Active = models.BooleanField()
	def __unicode__(self):
		return self.Username

class Machine(models.Model):
	MachineID = models.AutoField(primary_key=True)
	Location = models.CharField(max_length = 40)
	Active = models.BooleanField()
	def __unicode__(self):
		return self.Location

class Inventory(models.Model):
	InventoryID = models.AutoField(primary_key=True)
	ProductID = models.ForeignKey(Product)
	MachineID = models.ForeignKey(Machine)
	Quantity = models.IntegerField()
	Position = models.CharField(max_length = 40)
	def __unicode__(self):
		return self.Position

class Sale(models.Model):
	SaleID = models.AutoField(primary_key=True)
	UserID = models.ForeignKey(User)
	InventoryID = models.ForeignKey(Inventory)
	DateSale = models.DateField()
	def __unicode__(self):
		return str(self.DateSale)

