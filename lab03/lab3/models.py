from django.db import models
from django.utils import timezone


class Druzyna(models.Model):
    nazwa = models.CharField(max_length=60)

    kraj = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.nazwa} {self.kraj}'

class Osoba(models.Model):
    druzyna = models.ForeignKey(Druzyna,
                                on_delete=models.CASCADE,
                                null=True)
    imie = models.CharField(max_length=60,
                            blank=False)
    nazwisko = models.CharField(max_length=60,
                                blank=False)
    class miesiac_urodzenia(models.IntegerChoices):
        Styczen = 1
        Luty = 2
        Marzec = 3
        Kwiecien = 4
        Maj = 5
        Czerwiec = 6
        Lipiec = 7
        Sierpien = 8
        Wrzesien = 9
        Pazdziernik = 10
        Listopad = 11
        Grudzien = 12

    miesiac_urodzenia = models.IntegerField(choices=miesiac_urodzenia.choices,
                                            default=1)
    data_dodania = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'

    class Meta:
        ordering = ["nazwisko"]
