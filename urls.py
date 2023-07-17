from django.contrib import admin
from django.urls import path, include

import app.inventory.views
import app.payment.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    path('', app.inventory.views.LeftoversAllView.as_view(), name='leftovers-all'),
    path('leftovers/mine', app.inventory.views.LeftoversMineView.as_view(), name='leftovers-mine'),
    path('leftovers/new', app.inventory.views.LeftoversCreateView.as_view(), name='leftovers-new'),
    path('leftovers/<int:pk>', app.inventory.views.LeftoversDetailView.as_view(), name='leftovers-detail'),
    path('leftovers/<int:pk>/edit', app.inventory.views.LeftoversUpdateView.as_view(), name='leftovers-edit'),
    path('leftovers/<int:pk>/delete', app.inventory.views.LeftoversDeleteView.as_view(), name='leftovers-delete'),

    path('leftovers/<int:pk>/purchase', app.payment.views.PurchaseConfirmationView.as_view(),
         name='leftovers-purchase'),
]
