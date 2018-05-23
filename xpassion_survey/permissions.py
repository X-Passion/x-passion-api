import rest_framework.permissions

class IsSurveyTarget(rest_framework.permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.method in rest_framework.permissions.SAFE_METHODS:
            return len(set(obj.get_targets().all()).intersection(request.user.groups.all())) > 0
        else:
            return False


