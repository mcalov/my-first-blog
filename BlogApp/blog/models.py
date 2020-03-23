from django.db import models

# Create your models here.
from django.conf import settings
from django.db  import models
from django.utils import timezone
# from imagekit.models import ImageSpecField
# from imagekit.processors import ResizeToFill

# class Post(models.Model):
#     author  = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     title   = models.CharField(max_length=100)
#     text    = models.TextField()
#     createdDate = models.DateTimeField(default=timezone.now)
#     publishedDate = models.DateTimeField(blank=True, null=True)
#
#     image = models.ImageField(upload_to = 'images/', default = 'images/name.jpg')
#
#     def publish(self):
#         self.publishedDate = timezone.now()
#     def __str__(self):
#         return  self.title

# class Data(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     income = models.IntegerField(default=1)
#     createdData = models.DateTimeField(default=timezone.now)
#
# class InnoData(models.Model):
#     Jahr = models.DateTimeField()
#     Landkreis = models.CharField(max_length=40)
#     BIPEinwohner = models.IntegerField()
#     BIPErwerb = models.IntegerField()

class BIP(models.Model):
    EinwohnerFULL=models.CharField(default="BIP pro Einwohner",max_length=130)
    EinwohnerUNIT=models.CharField(default="EUR",max_length=130)
    Einwohner = models.IntegerField(null=True)
    ErwerbstaetigerFULL=models.CharField(default="BIP pro Erwerbstaetiger",max_length=130)
    ErwerbstaetigerUNIT=models.CharField(default="EUR",max_length=130)
    Erwerbstaetiger = models.IntegerField(null=True)

class BWS(models.Model):
    EinwohnerFULL=models.CharField(default="BWS je Einwohner (Insgesamt)",max_length=130)
    EinwohnerUNIT=models.CharField(default="Tsd. EUR",max_length=130)
    Einwohner = models.FloatField(null=True)

    ErwerbstaetigerFULL=models.CharField(default="BWS je Erwerbstätige (Insgesamt)",max_length=130)
    ErwerbstaetigerUNIT=models.CharField(default="Tsd. EUR",max_length=130)
    Erwerbstaetiger = models.FloatField(null=True)

    ErwerbstaetigerLandForstFischereiFULL=models.CharField(default="BWS je Erwerbstätiger (Land- und Forstwirtschaft, Fischerei (A))",max_length=130)
    ErwerbstaetigerLandForstFischereiUNIT=models.CharField(default="Tsd. EUR",max_length=130)
    ErwerbstaetigerLandForstFischerei = models.FloatField(null=True)

    ErwerbstaetigerProduzierendesGewerbeOhneBaugewerbeFULL=models.CharField(default="BWS je Erwerbstätiger (Produzierendes Gewerbe ohne Baugewerbe (B-E))",max_length=130)
    ErwerbstaetigerProduzierendesGewerbeOhneBaugewerbeUNIT=models.CharField(default="Tsd. EUR",max_length=130)
    ErwerbstaetigerProduzierendesGewerbeOhneBaugewerbe = models.FloatField(null=True)

    ErwerbstaetigerVerarbeitendesGewerbeFULL=models.CharField(default="BWS je Erwerbstätiger (Verarbeitendes Gewerbe ( C ) )",max_length=130)
    ErwerbstaetigerVerarbeitendesGewerbeUNIT=models.CharField(default="Tsd. EUR",max_length=130)
    ErwerbstaetigerVerarbeitendesGewerbe = models.FloatField(null=True)

    ErwerbstaetigerBaugewerbeFULL=models.CharField(default="BWS je Erwerbstätiger (Baugewerbe (F))",max_length=130)
    ErwerbstaetigerBaugewerbeUNIT=models.CharField(default="Tsd. EUR",max_length=130)
    ErwerbstaetigerBaugewerbe = models.FloatField(null=True)

    ErwerbstaetigerHandelVerkehrGastFULL=models.CharField(default="BWS je Erwerbstätiger (Handel,Verkehr,Gastgewerbe,Informa-/Kommunikation)",max_length=130)
    ErwerbstaetigerHandelVerkehrGastUNIT=models.CharField(default="Tsd. EUR",max_length=130)
    ErwerbstaetigerHandelVerkehrGast = models.FloatField(null=True)

    ErwerbstaetigerFinVersUntFULL=models.CharField(default="BWS je Erwerbstätiger (Fin-,Vers.-,Unt.-dienstl.,Grundst.-/Wohnungswesen)",max_length=130)
    ErwerbstaetigerFinVersUntUNIT=models.CharField(default="Tsd. EUR",max_length=130)
    ErwerbstaetigerFinVersUnt = models.FloatField(null=True)

    ErwerbstaetigerOeffentliErzGesunFULL=models.CharField(default="BWS je Erwerbstätiger (öffentl. u. sonst. Dienstl.,Erziehung, Gesundheit)",max_length=130)
    ErwerbstaetigerOeffentliErzGesunUNIT=models.CharField(default="Tsd. EUR",max_length=130)
    ErwerbstaetigerOeffentliErzGesun = models.FloatField(null=True)

class Oekonomie(models.Model):
    Jahr = models.IntegerField()
    Landkreis = models.CharField(max_length=40)

    BIPFieldFULL = models.CharField(default="Bruttoinlandsprodukt",max_length=130)
    BIPField = models.ForeignKey(BIP, on_delete=models.CASCADE)
    BWSFieldFULL = models.CharField(default="Bruttowertschöpfung", max_length=130)
    BWSField = models.ForeignKey(BWS, on_delete=models.CASCADE)

    ArbeitsproduktivitaetFULL=models.CharField(default="Arbeitsproduktivität (BIP je Arbeitsstunde)",max_length=130)
    ArbeitsproduktivitaetUNIT=models.CharField(default="EUR",max_length=130)
    Arbeitsproduktivitaet=models.FloatField(null=True)
