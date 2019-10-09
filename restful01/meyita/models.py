from django.db import models

# Create your models here.

class cal(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    hour = models.IntegerField()
    cntFormer = models.IntegerField()
    sumFormer = models.CharField(max_length=15, blank=False, default='')
    cntNewDM = models.IntegerField()
    sumNewDM = models.CharField(max_length=15, blank=False, default='')
    cntNew = models.IntegerField()
    sumNew = models.CharField(max_length=15, blank=False, default='')
    cntITA = models.IntegerField()
    sumITA = models.CharField(max_length=15, blank=False, default='')

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.name

class cpl(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    hour = models.IntegerField()
    cntFormer = models.IntegerField()
    sumFormer = models.CharField(max_length=15, blank=False, default='')
    cntNewDM = models.IntegerField()
    sumNewDM = models.CharField(max_length=15, blank=False, default='')
    cntNew = models.IntegerField()
    sumNew = models.CharField(max_length=15, blank=False, default='')
    cntITA = models.IntegerField()
    sumITA = models.CharField(max_length=15, blank=False, default='')

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.name

class cpb(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    hour = models.IntegerField()
    cntCR = models.IntegerField()
    sumCR = models.CharField(max_length=15, blank=False, default='')
    cntCDP = models.IntegerField()
    sumCDP = models.CharField(max_length=15, blank=False, default='')
    cntCDR = models.IntegerField()
    sumCDR = models.CharField(max_length=15, blank=False, default='')
    cntCV = models.IntegerField()
    sumCV = models.CharField(max_length=15, blank=False, default='')
    cntPA = models.IntegerField()
    sumPA = models.CharField(max_length=15, blank=False, default='')
    cntPR = models.IntegerField()
    sumPR = models.CharField(max_length=15, blank=False, default='')
    cntP = models.IntegerField()
    sumP = models.CharField(max_length=15, blank=False, default='')


    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.name

class cdl(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    hour = models.IntegerField()
    denialReason = models.CharField(max_length=100, blank=False, default='')
    cntDenial = models.IntegerField()
    sumDenials = models.CharField(max_length=15, blank=False, default='')

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.name