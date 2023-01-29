from django.contrib import admin
from domainz.billing.models import StripeCustomer

admin.site.register(StripeCustomer)
