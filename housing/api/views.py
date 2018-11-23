from rest_framework import viewsets
from housing.models import House
from provider.models import Provider
from department.models import Department 
from distance.models import Distance 
from housing.api.paginations import HousePagination
from serializers import HouseSerializer
from rest_framework import permissions

class HouseViewSet(viewsets.ModelViewSet):
    pagination_class = HousePagination
    serializer_class = HouseSerializer
    permission_classes = (permissions.BasePermission,)

    def get_queryset(self):
        # queryset = House.objects.all()
        # house_id = self.request.query_params.get('id', None)
        # if house_id:
        #     queryset = queryset.filter(id = house_id)

        # name = self.request.query_params.get('name', None)
        # if name:
        #     name_list = name.split()
        #     for n in name_list:
        #         queryset = queryset.filter(name__icontains = n)

        # provider = self.request.query_params.get('provider', None)
        # # if provider:
        # #     provider_qs = Provider.objects.all()
        # #     provider_ids = provider_qs.filter(name__iexact = provider).values_list('pk', flat = True)
        # #     if provider_ids:
        # #         provider_id = provider_ids[0]
        # if provider:
        #     queryset = queryset.filter(provider = provider)

        # location = self.request.query_params.get('location', None)
        # if location:
        #     location_list = location.split()
        #     for l in location_list:
        #         queryset = queryset.filter(location__icontains = l)

        # types = self.request.query_params.get('types', None)
        # if types:
        #     queryset = queryset.filter(types__icontains = types)

        # maxprice = self.request.query_params.get('maxprice', None)
        # if maxprice:
        #     queryset = queryset.filter(price__lte = maxprice)
        # minprice = self.request.query_params.get('minprice', None)
        # if minprice:
        #     queryset = queryset.filter(price__gte = minprice)

        # # TO CHECK (bc no acess to department and distance credentials)
        # department = self.request.query_params.get('department', None)
        # distance = self.request.query_params.get('distance', None)
        # if department:
        #     department_qs = Department.objects.all()
        #     department_ids = department_qs.filter(name__iexact = department).values_list('pk', flat = True)
        #     if department_ids:
        #         department_id = department_ids[0]
        #         distance_qs = Distance.objects.all()
        #         distance_qs = distance_qs.filter(department_id=department_id)
        #         distance_qs = distance_qs.filter(distance__lte = distance)
        #         queryset = queryset.filter(id__in = distance_qs)
        
        # # Print the actual SQL query, for showing the TA about the actual query
        # # print(queryset.query)
        # return queryset


        basequery = "SELECT id FROM housing_house"

        query_parts = []
        params = []
        
        #Get Id
        house_id = self.request.query_params.get('id', None)
        if house_id:
            query_parts.append("id = %s")
            params.append(house_id)

        #Get name (TODO: issue with %)
        name = self.request.query_params.get('name', None)
        if name:
            name_list = name.split()
            for n in name_list:
                query_parts.append("name LIKE %s")
                params.append('\''+'%%'+n+'%%'+'\'')

        #Get provider id
        provider = self.request.query_params.get('provider', None)
        if provider:
            query_parts.append("provider_id = %s")
            params.append(provider)

        #Get location (TODO: issue with %)
        location = self.request.query_params.get('location', None)
        if location:
            location_list = location.split()
            for l in location_list:
                query_parts.append("location LIKE %s")
                params.append('\''+'%%'+l+'%%'+'\'')

        #Get types
        types = self.request.query_params.get('types', None)
        if types:
            query_parts.append("types = %s")
            params.append('%'+types+'%')

        #Get price range
        maxprice = self.request.query_params.get('maxprice', None)
        minprice = self.request.query_params.get('minprice', None)
        if maxprice and minprice:
            query_parts.append("price >= %s AND price <= %s")
            params.append(minprice)
            params.append(maxprice)
        elif maxprice:
            query_parts.append("price <= %s")
            params.append(maxprice)
        elif minprice:
            query_parts.append("price >= %s")
            params.append(minprice)
        
        if len(query_parts) > 0:
            basequery += " WHERE "

        house_query = basequery + " AND ".join(query_parts)
        # print(house_query)
        # print(tuple(params))
        print(basequery + " AND ".join(query_parts) % tuple(params))
        house_queryset = list(House.objects.raw(basequery + " AND ".join(query_parts) % tuple(params)))

        return house_queryset


        