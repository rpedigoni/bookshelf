# coding: utf-8
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ProtectedMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *a, **kw):
        return super(ProtectedMixin, self).dispatch(*a, **kw)
