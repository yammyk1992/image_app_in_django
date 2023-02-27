# from rest_framework import viewsets
#
# from .models import Subscription
# from .serializers import SubscriptionBasicUserSerializer
#
#
# class ServiceViewSet(viewsets.ModelViewSet):
#     queryset = Subscription.objects.all()
#     serializer_class = SubscriptionBasicUserSerializer

    # def get_serializer_class(self):
    #     user = Subscriptions.objects.filter(client=self.request.user, plan="Basic")
    #     print(user)
    #     if user:
    #         return ImagesBasicUserSerializer
    #     elif user.plan == 'Premium':
    #         return ImagesPremiumUserSerializer

    # def get_queryset(self):
    #     return Images.objects.filter(author=self.request.user)
