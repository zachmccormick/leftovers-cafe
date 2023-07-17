from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from app.inventory.forms import LeftoversForm
from app.inventory.models import Leftovers


class LeftoversAllView(ListView):
    model = Leftovers


class LeftoversMineView(LoginRequiredMixin, ListView):
    model = Leftovers

    def get_queryset(self):
        return Leftovers.objects.filter(sold_by=self.request.user)


class LeftoversDetailView(DetailView):
    model = Leftovers


class LeftoversCreateView(LoginRequiredMixin, CreateView):
    model = Leftovers
    form_class = LeftoversForm

    def form_valid(self, form):
        form.instance.sold_by = self.request.user
        return super().form_valid(form)


class LeftoversUpdateView(LoginRequiredMixin, UpdateView):
    model = Leftovers
    form_class = LeftoversForm

    def form_valid(self, form):
        if self.object.sold_by != self.request.user:
            raise RuntimeError("You can't edit leftovers that aren't yours!")
        return super().form_valid(form)


class LeftoversDeleteView(LoginRequiredMixin, DeleteView):
    model = Leftovers
    success_url = reverse_lazy("leftovers-all")

    def form_valid(self, form):
        if self.object.sold_by != self.request.user:
            raise RuntimeError("You can't delete leftovers that aren't yours!")
        return super().form_valid(form)
