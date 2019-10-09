from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from meyita.models import cal
from meyita.models import cpl
from meyita.models import cpb
from meyita.models import cdl
from meyita.serializers import calSerializer
from meyita.serializers import cplSerializer
from meyita.serializers import cpbSerializer
from meyita.serializers import cdlSerializer


# cal
class calList(generics.ListCreateAPIView):
    queryset = cal.objects.all()
    serializer_class = calSerializer
    name = 'cal-list'

class calDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = cal.objects.all()
    serializer_class = calSerializer
    name = 'cal-detail'
###############################################################

#cpl
class cplList(generics.ListCreateAPIView):
    queryset = cpl.objects.all()
    serializer_class = cplSerializer
    name = 'cpl-list'

class cplDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = cpl.objects.all()
    serializer_class = cplSerializer
    name = 'cpl-detail'
###############################################################

#cpb
class cpbList(generics.ListCreateAPIView):
    queryset = cpb.objects.all()
    serializer_class = cplSerializer
    name = 'cpb-list'

class cpbDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = cpb.objects.all()
    serializer_class = cpbSerializer
    name = 'cpb-detail'
###############################################################

#cdl
class cdlList(generics.ListCreateAPIView):
    queryset = cdl.objects.all()
    serializer_class = cdlSerializer
    name = 'cdl-list'

class cdlDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = cdl.objects.all()
    serializer_class = cdlSerializer
    name = 'cdl-detail'
###############################################################

#apiRoot
class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'cal': reverse(calList.name, request=request),
            'cpl': reverse(cplList.name, request=request),
            'cpb': reverse(cpbList.name, request=request),
            'cdl': reverse(cdlList.name, request=request)
        })
