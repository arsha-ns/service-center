from django.shortcuts import render

from rest_framework import viewsets

from rest_framework.response import Response

from rest_framework import authentication

from rest_framework import permissions

from api.serializers import CustomerSerializer,WorkSerializer

from api.models import Customer,Work

from rest_framework.decorators import action

from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.




class CustomerViewSetView(viewsets.ModelViewSet):

    serializer_class=CustomerSerializer

    queryset=Customer.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAdminUser]
    

    def perform_create(self, serializer):
      
      serializer.save(technician=self.request.user)



class WorkCreateView(CreateAPIView):

   serializer_class=WorkSerializer

   authentication_classes=[authentication.TokenAuthentication]

   permission_classes=[permissions.IsAdminUser]


   def perform_create(self, serializer):
      
      id=self.kwargs.get("pk")

      customer_instance=Customer.objects.get(id=id)

      serializer.save(customer=customer_instance)


class WorkDetailView(RetrieveUpdateDestroyAPIView):

   serializer_class =WorkSerializer

   queryset=Work.objects.all()

   authentication_classes=[authentication.TokenAuthentication]

   permission_classes=[permissions.IsAdminUser]






















































   




# ===================================================================================

# custom method  for add work
# ===================


   #  @action(methods=["post"],detail=True)
   #  def add_work(self,request,*args,**kwargs):
       
   #     id=kwargs.get("pk")

   #     customer_instance=Work.objects.get(id=id)

   #     serialzer_instance=WorkSerializer(data=request.data)


   #     if serialzer_instance.is_valid():
          
   #        serialzer_instance.save(customer=customer_instance)

   #        return Response(data=serialzer_instance.data)
       
   #     else:
          
   #        return Response(data=serialzer_instance.errors)
# ======================================================================