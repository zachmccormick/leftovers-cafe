from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from app.inventory.models import Leftovers
from app.payment.models import Purchase
from app.payment.tasks import complete_purchase


class PurchaseConfirmationView(LoginRequiredMixin, UpdateView):
    model = Leftovers
    fields = []
    template_name = 'payment/purchase_confirm.html'

    def form_valid(self, form):
        if self.object.sold_by == self.request.user:
            raise RuntimeError("You cannot purchase your own items!")
        if self.object.purchased_by:
            raise RuntimeError("You cannot purchase items that are already purchased!")
        purchase = Purchase()
        purchase.leftover = self.object
        purchase.user = self.request.user
        purchase.save()
        complete_purchase.delay(purchase.pk)
        return super().form_valid(form)
