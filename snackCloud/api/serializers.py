from rest_framework import serializers
from .models import Role,Product,User,Machine,Sale,Inventory

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('RoleID', 'RoleName', 'Active')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('ProductID', 'ProductName','Price', 'Active')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('UserID', 'Username','Password','Email','Phone','Points','SMS','RoleID','Active')

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model =Machine
        fields = ('MachineID', 'Location', 'Active')

class InventorySerializer(serializers.ModelSerializer):
    ProductID = ProductSerializer()
    class Meta:
        model = Inventory
        fields = ('InventoryID', 'ProductID', 'MachineID','Quantity','Position')

class SaleSerializer(serializers.ModelSerializer):
    InventoryID = InventorySerializer()
    class Meta:
        model = Sale
        fields = ('UserID', 'InventoryID','DateSale')


class LoginSerializer(serializers.Serializer):
    Username = serializers.CharField()
    Password = serializers.CharField()