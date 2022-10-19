from django.db import models


class Osoba(models.Model):
    imie = models.CharField(max_lenght=60,
                            blank=False)
    nazwisko = models.CharField(max_length=60,
                                blank=False)
    miesiac_urodzenia = (
        ('1','Styczen'),
        ('2', 'Luty'),
        ('3', 'Marzec'),
        ('4', 'Kwiecien'),
        ('5', 'Maj'),
        ('6', 'Czerwiec'),
        ('7', 'Lipiec'),
        ('8', 'Sierpien'),
        ('9', 'Wrzesien'),
        ('10', 'Pazdziernik'),
        ('11', 'Listopad'),
        ('12', 'Grudzien'),
    )