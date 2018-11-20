from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj and request.method in permissions.SAFE_METHODS + ('PUT',)
