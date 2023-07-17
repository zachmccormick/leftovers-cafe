import logging
import time

from celery import shared_task

from app.payment.models import Purchase

logger = logging.getLogger(__name__)


@shared_task
def complete_purchase(pk):
    purchase = Purchase.objects.get(pk=pk)
    if not purchase:
        logger.warning(f"Could not find purchase {pk} and could not run complete_purchase")
    purchase.leftover.purchased_by = purchase.user
    purchase.leftover.save()
    time.sleep(5)

    purchase.completed = True
    purchase.save()
