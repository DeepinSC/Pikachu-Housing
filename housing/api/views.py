from rest_framework import viewsets
from housing.models import House
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

        #Get department
        department = self.request.query_params.get('department', None)
        if department:
            query_parts.append("closest_department_float = %s")
            params.append(department)

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

        has_liked = self.request.query_params.get('like', None)
        if has_liked and self.request.user:
            user_id = self.request.user.id
            sql = "housing_house.id IN (SELECT house_id_id FROM like_like WHERE user_id_id = %s AND has_liked = TRUE)" % user_id
            house_queryset = house_queryset.extra(where=[sql])

        srule = self.request.query_params.get('srule', None)
        if srule == 'price-low-to-high':
            house_queryset = house_queryset.filter(price__lt=9999).order_by('price')
        if srule == 'price-high-to-low':
            house_queryset = house_queryset.filter(price__lt=9999).order_by('-price')
        if srule == 'name-ascending':
            house_queryset = house_queryset.order_by('name') 
        if srule == 'name-descending':
            house_queryset = house_queryset.order_by('-name')    

        return house_queryset
