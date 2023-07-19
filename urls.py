from functools import partial

from decorator_include import decorator_include
from django.contrib import admin
from django.urls import path, include

import app.inventory.views
import app.payment.views
from lib.tracing import for_service

admin_app = partial(for_service, 'admin')
auth_app = partial(for_service, 'auth')
inventory_app = partial(for_service, 'inventory')
payment_app = partial(for_service, 'payment')

urlpatterns = [
    path('admin/', decorator_include(admin_app(), admin.site.urls)),
    path('accounts/', decorator_include(auth_app(), 'allauth.urls')),

    path('', inventory_app()(app.inventory.views.LeftoversAllView.as_view()), name='leftovers-all'),
    path('leftovers/mine', inventory_app()(app.inventory.views.LeftoversMineView.as_view()), name='leftovers-mine'),
    path('leftovers/new', inventory_app()(app.inventory.views.LeftoversCreateView.as_view()), name='leftovers-new'),
    path('leftovers/<int:pk>', inventory_app()(app.inventory.views.LeftoversDetailView.as_view()),
         name='leftovers-detail'),
    path('leftovers/<int:pk>/edit', inventory_app()(app.inventory.views.LeftoversUpdateView.as_view()),
         name='leftovers-edit'),
    path('leftovers/<int:pk>/delete', inventory_app()(app.inventory.views.LeftoversDeleteView.as_view()),
         name='leftovers-delete'),

    path('leftovers/<int:pk>/purchase', payment_app()(app.payment.views.PurchaseConfirmationView.as_view()),
         name='leftovers-purchase'),
]
