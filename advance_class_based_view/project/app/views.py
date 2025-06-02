
# # ------------------------ViewSets-----------------------------------: No built-in actions. You define them manually: 
# # During dispatch, the following attributes are available on the ViewSet.
# # basename - the base to use for the URL names that are created.
# # action - the name of the current action (e.g., list, create).
# # detail - boolean indicating if the current action is configured for a list or detail view.
# # suffix - the display suffix for the viewset type - mirrors the detail attribute.
# # name - the display name for the viewset. This argument is mutually exclusive to suffix.
# # description - the display description for the individual view of a viewset.

# from rest_framework.response import Response
# from .serializers import StudentSerializer
# from .models import Student
# from rest_framework import status
# from rest_framework import viewsets

# class StudentViewSet(viewsets.ViewSet):
#     def list(self, request):
#         # print("List")
#         # print("Basename:", self.basename)
#         # print("Action:", self.action)
#         # print("Detail:", self.detail)
#         # print("Suffix:", self.suffix)
#         # print("Name:", self.name)
#         # print("Description:", self.description)
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)

#     def create(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             # return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def update(self,request, pk):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             # return Response(serializer.data)
#             return Response({'msg':'Complete Data Updated'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def partial_update(self,request, pk):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             # return Response(serializer.data)
#             return Response({'msg':'Partial Data Updated'})
#         return Response(serializer.errors)

#     def destroy(self,request, pk):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'Data Deleted'})
    
#  GenericViewSet	: GenericViewSet: gives you the foundation and reusable tools like get_queryset() or get_serializer().
# Mixins: give you the actual API behavior/actions (GET, POST, PUT, DELETE, etc.).
# So, you combine them based on what actions you want in your ViewSet. 
# from rest_framework import viewsets, mixins
# from .models import Student
# from .serializers import StudentSerializer

# class StudentViewSet(mixins.ListModelMixin,
#                      mixins.CreateModelMixin,
#                      mixins.RetrieveModelMixin,
#                      mixins.UpdateModelMixin,
#                      mixins.DestroyModelMixin,
#                      viewsets.GenericViewSet):
#     """
#     ViewSet for listing, creating, retrieving, and updating Students.
#     """
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


    
    # ModelViewSet : Full CRUD: list(), create(), retrieve(), update(), destroy(): 
from rest_framework import status, viewsets
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
class StudentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

 # ReadOnlyModelViewSet : Only list() and retrieve() for read-only APIs
# from rest_framework import viewsets
# from .serializers import StudentSerializer
# from .models import Student
# class StudentViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     A simple ViewSet for viewing accounts.
#     """
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer