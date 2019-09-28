from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import transaction

from middleware.viewsets import CustomModelViewSet
from middleware.permissions import BackendPermission
from app.payment.models import Payment
from app.payment.serializers import PaymentSerializer
    
class PaymentView(CustomModelViewSet):
    serializer_class = PaymentSerializer
    permission_classes = [BackendPermission]
    queryset = Payment.objects.all()

    permissionId = Payment.__name__

    @transaction.atomic
    @action(detail=True, methods=['put'], permission_classes=[BackendPermission])
    def refund(self, request, pk=None):
        print('refund', pk, '------')
        for payment in Payment.objects.all():
            print(payment.id, '------=====')
        payment = self.get_object()
        payment.refund()

        return Response({'result': 'ok'})