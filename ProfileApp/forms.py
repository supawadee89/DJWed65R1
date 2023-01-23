from django.forms import *

class ProductForm(Form):
    BRAND_LIST = [('Acer', 'Acer'), ('HP','HP'), ('LENOVO','LENOVO'),('DELL','DELL'),('HUWEI','HUWEI')]
    MADE_LIST = [('Thai','Thai'),('China','China')]
    id = CharField(max_length=13, label="รหัสสินค้า",
            required=True, widget=TextInput(attrs={'size' : '15'}))
    name = CharField(max_length=50, label="=ชื่อสินค้า",
            required=True, widget=TextInput(attrs={'size': '55'}))
    brand = CharField(max_length=13, label="ยี่ห้อ",
            required=True, widget=TextInput(attrs={'size': '35'}))
    price = FloatField(min_value=1.00, max_value=10000.00, label="ราคาต่อหน่วย",
            required=True, widget=NumberInput(attrs={'size': '10'}))
    net = IntegerField(min_value=0, max_value=1000, label="คงเหลือ",
            required=True, widget=NumberInput(attrs={'size': '10'}))