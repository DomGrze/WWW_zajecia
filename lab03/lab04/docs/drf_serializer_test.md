from lab04.models import Osoba
from lab04.serializers import OsobaSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

osoba = Osoba(imie='Dominik', nazwisko='Grzeszczyk', miesiac_urodzenia=8)

osoba.save()

serializer = OsobaSerializer(osoba)

serializer.data

output: {'id': 6, 'imie': 'Dominik', 'nazwisko': 'Grzeszczyk', 'miesiac_urodzenia': '8', 'kraj': None}
content = JSONRenderer().render(serializer.data)

content

output: b'{"id":6,"imie":"Dominik","nazwisko":"Grzeszczyk","miesiac_urodzenia":"8","kraj":null}'
import io

stream = io.BytesIO(content)

data = JSONParser().parse(stream)

deserializer = OsobaSerializer(data=data)

deserializer.is_valid()

output: False

deserializer.errors

OUTPUT:
{'kraj': [ErrorDetail(string='This field may not be null.', code='null')]}
deserializer.fields
{'id': IntegerField(read_only=True), 'imie': CharField(required=True), 'nazwisko': CharField(required=True), 'miesiac_urodzenia': ChoiceField(choices=(('1', 'styczeń'), ('2', 'luty'), ('3', 'marzec'), ('4', 'kwiecień'), ('5 ', 'maj'), ('6', 'czerwiec'), ('7', 'lipiec'), ('8', 'sierpień'), ('9', 'wrzesień'), ('10', 'październik'), ('11', 'listopad'), ('12', 'grudzień')), default='1'), 'kraj': PrimaryKeyRelatedField(queryset=<QuerySet [<Druzyna: Polska (PL)>, <Druzyna: JAGLAKI (DE)]>)}

PO DODANIU 'allow_null=True':

deserializer.is_valid()

OUTPUT: True

deserializer.validated_data

OUTPUT: OrderedDict([('imie', 'Dominik'), ('nazwisko', 'Grzesznik'), ('miesiac_urodzenia', '8'), ('kraj', None)])

deserializer.save()

OUTPUT: <Osoba: Dominik Grzesznik>

deserializer.data

OUTPUT: {'id': 7, 'imie': 'Dominik', 'nazwisko': 'Grzesznik', 'miesiac_urodzenia': '8', 'kraj': None}



from lab04.models import Druzyna

from lab04.serializers import DruzynaSerializer

from rest_framework.renderers import JSONRenderer

from rest_framework.parsers import JSONParser

druzyna = Druzyna('PL', 'Polaki')

druzyna.save()

serializer = DruzynaSerializer(druzyna)

serializer.data

OUTPUT: {'id': 3, 'kraj': 'PL', 'nazwa': 'Polaki'}

content = JSONRenderer().render(serializer.data)

content

OUTPUT: b'{"id":3,"kraj":"PL","nazwa":"Polaki"}'

import io

stream = io.BytesIO(content)

data = JSONParser().parse(stream)

deserializer = DruzynaSerializer(data=data)

deserializer.is_valid()

OUTPUT: True

deserializer.validated_data

OUTPUT: OrderedDict([('kraj', 'PL'), ('nazwa', 'Polaki')])

deserializer.save()

OUTPUT: <Druzyna: Polaki (PL)>

deserializer.data

OUTPUT: {'id': 4, 'kraj': 'PL', 'nazwa': 'Polaki'}
