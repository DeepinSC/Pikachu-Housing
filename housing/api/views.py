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
        basequery = "SELECT id FROM housing_house"

        query_parts = []
        params = []
        
        #Get Id
        house_id = self.request.query_params.get('id', None)
        if house_id:
            query_parts.append("id = %s")
            params.append(house_id)

        #Get name 
        name = self.request.query_params.get('name', None)
        if name:
            name_list = name.split()
            for n in name_list:
                query_parts.append("upper(name) LIKE upper(%s)")
                params.append('\''+'%%'+n+'%%'+'\'')

        #Get provider id
        provider = self.request.query_params.get('provider', None)
        if provider:
            query_parts.append("provider_id = %s")
            params.append(provider)

        #Get location 
        location = self.request.query_params.get('location', None)
        if location:
            location_list = location.split()
            for l in location_list:
                query_parts.append("upper(location) LIKE upper(%s)")
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

        sql = "housing_house.id IN (" + (basequery + " AND ".join(query_parts) % tuple(params)) + ")"
        house_queryset = House.objects.extra(where=[sql])

        return house_queryset
