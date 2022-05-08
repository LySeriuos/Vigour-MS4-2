from django.hhtp import HttpResponse


class StripeWebHook_Handler:
    """Handle Stripe webhooks"""

    # function for getting atributes from stripe
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
