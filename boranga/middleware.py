import re

from django.shortcuts import redirect
from django.urls import reverse
from reversion.middleware import RevisionMiddleware
from reversion.views import _request_creates_revision
from django.utils.http import urlquote_plus

CHECKOUT_PATH = re.compile("^/ledger/checkout/checkout")


class FirstTimeNagScreenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (
            not request.user.is_authenticated
            or not request.method == "GET"
            or "api" in request.path
            or "admin" in request.path
            or "static" in request.path
        ):
            return self.get_response(request)

        if (
            request.user.first_name
            and request.user.last_name
            and request.user.residential_address_id
            and self.residential_address_fully_filled(request.user)
            and (
                request.user.postal_same_as_residential
                or self.postal_address_fully_filled(request.user)
            )
            and (request.user.phone_number or request.user.mobile_number)
        ):
            return self.get_response(request)

        path_ft = reverse("account-firstime")
        if request.path in ("/sso/setting", path_ft, reverse("logout")):
            return self.get_response(request)

        return redirect(path_ft + "?next=" + urlquote_plus(request.get_full_path()))
    
    def postal_address_fully_filled(self, user):
        return (
            user.postal_address_id
            and user.postal_address.line1
            and user.postal_address.locality
            and user.postal_address.state
            and user.postal_address.country
            and user.postal_address.postcode
        )

    def residential_address_fully_filled(self, user):
        return (
            user.residential_address_id
            and user.residential_address.line1
            and user.residential_address.locality
            and user.residential_address.state
            and user.residential_address.country
            and user.residential_address.postcode
        )


class RevisionOverrideMiddleware(RevisionMiddleware):
    """
    Wraps the entire request in a revision.

    override venv/lib/python2.7/site-packages/reversion/middleware.py
    """

    # exclude ledger payments/checkout from revision - hack to overcome basket (lagging status)
    # issue/conflict with reversion
    def request_creates_revision(self, request):
        return (
            _request_creates_revision(request)
            and "checkout" not in request.get_full_path()
        )
