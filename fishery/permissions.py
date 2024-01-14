from rest_framework import permissions

from fishery.models import Fishery
class IsFisheryAccepted(permissions.BasePermission):
    def has_permission(self, request, view):
        fishery_id = view.kwargs.get('pk')
        if fishery_id:
            try:
                fishery = Fishery.objects.get(pk=fishery_id)
                if fishery.status == 'Accepted':
                    return True
                else:
                    return False
            except Fishery.DoesNotExist:
                return False
        else:
            return False
