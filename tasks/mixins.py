from django.core.exceptions import PermissionDenied


class UserIsOwnerMixin(object):
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.creator != request.user:
            raise PermissionDenied
        return super(UserIsOwnerMixin, self).dispatch(request, *args, **kwargs)
