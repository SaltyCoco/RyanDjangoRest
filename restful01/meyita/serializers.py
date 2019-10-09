from rest_framework import serializers
from meyita.models import cal
from meyita.models import cpl
from meyita.models import cpb
from meyita.models import cdl
import meyita.views

class calSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    date = serializers.DateTimeField()
    hour = serializers.IntegerField()
    cntFormer = serializers.IntegerField()
    sumFormer = serializers.CharField(max_length=15)
    cntNewDM = serializers.IntegerField()
    sumNewDM = serializers.CharField(max_length=15)
    cntNew = serializers.IntegerField()
    sumNew = serializers.CharField(max_length=15)
    cntITA = serializers.IntegerField()
    sumITA = serializers.CharField(max_length=15)

    def create(self, validated_data):
        return cal.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.hour = validated_data.get('hour', instance.hour)
        instance.cntFormer = validated_data.get('cntFormer', instance.cntFormer)
        instance.sumFormer = validated_data.get('sumFormer', instance.sumFormer)
        instance.cntNewDM = validated_data.get('cntNewDM', instance.cntNewDM)
        instance.sumNewDM = validated_data.get('sumNewDM', instance.sumNewDM)
        instance.cntNew = validated_data.get('cntNew', instance.cntNew)
        instance.sumNew = validated_data.get('sumNew', instance.sumNew)
        instance.cntITA = validated_data.get('cntITA', instance.cntITA)
        instance.sumITA = validated_data.get('sumITA', instance.sumITA)
        instance.save()
        return instance

class cplSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    date = serializers.DateTimeField()
    hour = serializers.IntegerField()
    cntFormer = serializers.IntegerField()
    sumFormer = serializers.CharField(max_length=15)
    cntNewDM = serializers.IntegerField()
    sumNewDM = serializers.CharField(max_length=15)
    cntNew = serializers.IntegerField()
    sumNew = serializers.CharField(max_length=15)
    cntITA = serializers.IntegerField()
    sumITA = serializers.CharField(max_length=15)

    def create(self, validated_data):
        return cal.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.hour = validated_data.get('hour', instance.hour)
        instance.cntFormer = validated_data.get('cntFormer', instance.cntFormer)
        instance.sumFormer = validated_data.get('sumFormer', instance.sumFormer)
        instance.cntNewDM = validated_data.get('cntNewDM', instance.cntNewDM)
        instance.sumNewDM = validated_data.get('sumNewDM', instance.sumNewDM)
        instance.cntNew = validated_data.get('cntNew', instance.cntNew)
        instance.sumNew = validated_data.get('sumNew', instance.sumNew)
        instance.cntITA = validated_data.get('cntITA', instance.cntITA)
        instance.sumITA = validated_data.get('sumITA', instance.sumITA)
        instance.save()
        return instance

class cpbSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    date = serializers.DateTimeField()
    hour = serializers.IntegerField()
    cntCR = serializers.IntegerField()
    sumCR = serializers.CharField(max_length=15)
    cntCDP = serializers.IntegerField()
    sumCDP = serializers.CharField(max_length=15)
    cntCDR = serializers.IntegerField()
    sumCDR = serializers.CharField(max_length=15)
    cntCV = serializers.IntegerField()
    sumCV = serializers.CharField(max_length=15)
    cntPA = serializers.IntegerField()
    sumPA = serializers.CharField(max_length=15)
    cntPR = serializers.IntegerField()
    sumPR = serializers.CharField(max_length=15)
    cntP = serializers.IntegerField()
    sumP = serializers.CharField(max_length=15)

    def create(self, validated_data):
        return cpb.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.hour = validated_data.get('hour', instance.hour)
        instance.cntCR = validated_data.get('cntCR', instance.cntCR)
        instance.sumCR = validated_data.get('sumCR', instance.sumCR)
        instance.cntCDP = validated_data.get('cntCDP', instance.cntCDP)
        instance.sumCDP = validated_data.get('sumCDP', instance.sumCDP)
        instance.cntCDR = validated_data.get('cntCDR', instance.cntCDR)
        instance.sumCDR = validated_data.get('sumCDR', instance.sumCDR)
        instance.cntCV = validated_data.get('cntCV', instance.cntCV)
        instance.sumCV = validated_data.get('sumCV', instance.sumCV)
        instance.cntPA = validated_data.get('cntPA', instance.cntPA)
        instance.sumPA = validated_data.get('sumPA', instance.sumPA)
        instance.cntPR = validated_data.get('cntPR', instance.cntPR)
        instance.sumPR = validated_data.get('sumPR', instance.sumPR)
        instance.cntP = validated_data.get('cntP', instance.cntP)
        instance.sumP = validated_data.get('sumP', instance.sumP)
        instance.save()
        return instance

class cdlSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    date = serializers.DateTimeField()
    hour = serializers.IntegerField()
    denialReason = serializers.CharField(max_length=100)
    cntDenial = serializers.IntegerField()
    sumDenials = serializers.CharField(max_length=15)

    def create(self, validated_data):
        return cdl.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.hour = validated_data.get('hour', instance.hour)
        instance.denialReason = validated_data.get('denialReason', instance.denialReason)
        instance.cntDenial = validated_data.get('cntDenial', instance.cntDenial)
        instance.sumDenial = validated_data.get('sumDenial', instance.sumDenial)