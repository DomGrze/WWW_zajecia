>>> from lab3.models import Osoba, Druzyna
>>> q = Osoba.objects.all()
>>> q
<QuerySet [<Osoba: Andrzej Arbuz>, <Osoba: Johnny Janowich>, <Osoba: Jan Janowicz>, <Osoba: Jaglak Mateusz>, <Osoba: Test Te
sting>, <Osoba: Artur Zzyz>]>
>>> w = Osoba.objects.filter(id=3)
>>> w
<QuerySet [<Osoba: Test Testing>]>
>>> e = Osoba.objects.filter(imie__startswith='J') 
>>> e
<QuerySet [<Osoba: Johnny Janowich>, <Osoba: Jan Janowicz>, <Osoba: Jaglak Mateusz>]>
>>> r = Druzyna.objects.values('nazwa').distinct()
>>> r
<QuerySet [{'nazwa': 'Jaglaki'}, {'nazwa': 'Test1'}, {'nazwa': 'Twierdza'}]>
>>> t = Druzyna.objects.all().order_by('-nazwa')           
>>> t                                                      
<QuerySet [<Druzyna: Twierdza DE>, <Druzyna: Test1 PL>, <Druzyna: Jaglaki IZ>]>
>>> y = Osoba(imie='Zadanie11')
>>> y
<Osoba: Zadanie11 >
