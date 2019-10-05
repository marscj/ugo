from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import transaction

from middleware.viewsets import CustomModelViewSet
from middleware.permissions import BackendPermission

from .import PaymentStatus, PaymentAction
from .models import Payment
from .serializers import PaymentSerializer
    
class PaymentView(CustomModelViewSet):
    serializer_class = PaymentSerializer
    permission_classes = [BackendPermission]
    queryset = Payment.objects.all()

    permissionId = Payment.__name__

    @transaction.atomic
    @action(detail=True, methods=['put'], permission_classes=[BackendPermission])
    def refund(self, request, pk=None):

        payment = self.get_object()

        if payment.status == PaymentStatus.REFUNDING and payment.action == PaymentAction.REFUNDED:
            payment.refund()

        return Response({'result': 'ok'})