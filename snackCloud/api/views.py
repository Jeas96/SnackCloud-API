from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from datetime import datetime
from api.models import Role,Product,User,Machine,Sale,Inventory
from api.serializers import LoginSerializer,RoleSerializer, ProductSerializer, UserSerializer,MachineSerializer,SaleSerializer,InventorySerializer 

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


#Login, Lista productos por maquina

@csrf_exempt
def machine_products(request):
	try:
		if request.method == 'POST':
			data = JSONParser().parse(request)
	        serializer = MachineSerializer(data=data)
	        if serializer.is_valid():
	            try:
	            	machine = Machine.objects.get(MachineID = data['MachineID'])
	            	inventory = Inventory.objects.filter(MachineID = machine)
	            	serializer = InventorySerializer(inventory,many = True)
	            	return JSONResponse(serializer.data, status=201)
	            except:
	            	return HttpResponse(status=404)
	        else:
	        	return HttpResponse(status=404)
	except Exception as e:
		print(e)
		return HttpResponse(status=404)

@csrf_exempt
def login(request):
	try:
		if request.method == 'POST':
			data = JSONParser().parse(request)
	        serializer = LoginSerializer(data = data)
	        if serializer.is_valid():
	            try:
	            	user = User.objects.get(Username=serializer.data['Username'],Password=serializer.data['Password'])
	            	serializer = UserSerializer(user)
	            	return JSONResponse(serializer.data, status=201)
	            except:
	            	return HttpResponse(status=404)
	        else:
	        	return HttpResponse(status=404)
	except Exception as e:
		print(e)
		return HttpResponse(status=404)

@csrf_exempt
def sale(request):
	try:
		if request.method == 'POST':
			data = JSONParser().parse(request)
			user = User.objects.get(UserID=data['UserID'])
			inventory = Inventory.objects.get(InventoryID = data['InventoryID'])
			machine = Machine.objects.get(InventoryID = inventory.InventoryID)
			product = Product.objects.get(ProductID = machine.ProductID)

			if(user.Points>=product.Price and inventory.Quantity>=1):
				p = Sale(ProductID=product, UserID=user,DateSale=datetime.now())
				user.Points= user.Points - products.Price
				inventory.Quantity = inventory.Quantity-1
				user.save()
				p.save()
	        return HttpResponse(status=201)
	except Exception as e:
		return HttpResponse(status=404)

@csrf_exempt
def signup(request):
	try:
		if request.method == 'POST':
			data = JSONParser().parse(request)
			u = User(Username = data['Username'],Password = data['Password'], 
				Email = data['Email'],Phone=data['Phone'],Points = data['Points'],
				SMS = data['SMS'], RoleID = Role.objects.get(RoleName='User'),Active = True)
			u.save()
			return HttpResponse(status = 201)
	except Exception as e:
		print(e)
		return HttpResponse(status=404)
