from django.shortcuts import render
from django.views import generic
from django.http.response import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from common import services as com_s
from . import models as m
from . import form as f


class DirectSalesView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = m.Venta
    form_class = f.CrearVentaForm
    template_name = 'ventas/components/direct_sales.html'
    permission_required = 'transmision.can_admin_direccionamiento'

    def get_context_data(self, **kwargs):
        kwargs.update({
            'active': 'si'
        })
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        # com_s.send_daily_notification(form.instance.total_venta)
        form.instance.usuario = self.request.user
        form.save()
        return JsonResponse({'ok': True})
