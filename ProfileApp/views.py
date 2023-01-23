from django.shortcuts import render ,HttpResponse, redirect

# Create your views here.
def test(request):
    return HttpResponse ("<H1>Hello Woeld <br> This is My World Wide Web </h1>")

def home(request):
    return render(request, 'home.html')

def firstweb(request):
    return render(request, 'firstweb.html')

def secondpage(request):
    return render(request, 'secondpage.html')

def thirdpage(request):
    return render(request, 'thirdpage.html')

def header(request):
    return render(request, 'header.html')

def rolemodel(request):
    return render(request, 'rolemodel.html')

def hny (request):
    return  render(request, 'hny.html')

def showMyData(request):
    showID = "65342310066-0"
    showName = "นางสาวสุภาวดี อรุณโณ"
    showAddress = "36 หมู่ 2 ตำบลทุ่งเขาหลวง อำเภอทุ่งเขาหลวง จังหวัดร้อยเอ็ด 415701"
    showTel = "0952523660"
    showGender = "หญิง"
    showBirthday = "14 กันยายน 2544"
    showWeight = 55
    showHeight = 173
    showStatus = "นักศึกษา"
    showSchool = "มหาวิทยาลัยเทคโนโลยีราชมงคลอีสาน วิทยาเขตขอนแก่น"

    products = []

    product = ['ลิป Hermes ', 2500.00, '../../static/images/A1.jpg']
    products.append(product)
    product = ['ลิป YSL ', 1500.00, '../../static/images/A2.jpg']
    products.append(product)
    product = ['ลิป Diro', 1500.00, '../../static/images/A3.jpg']
    products.append(product)
    product = ['ลิป Chanel', 1450.00, '../../static/images/A4.jpg']
    products.append(product)
    product = ['ลิป loveyou', 1200.00, '../../static/images/A5.png']
    products.append(product)
    product = ['ลิป บ็อบบี้ บราวน์', 590.00, '../../static/images/A6.jpg']
    products.append(product)
    product = ['ลิป Sleeping Mask', 700.00, '../../static/images/A7.jpg']
    products.append(product)
    product = ['ลิป  Y.O.U', 1200.00, '../../static/images/A8.jpg']
    products.append(product)
    product = ['ลิป 4U2', 520.00, '../../static/images/A9.png']
    products.append(product)
    product = ['ลอป โซลเกิร์ล', 49.00, '../../static/images/A10.jpg']
    products.append(product)

    context = {'showID': showID, 'showName': showName, 'showAddress': showAddress, 'showTel': showTel,
               'showGender': showGender, 'showBirthday': showBirthday, 'showWeight': showWeight,
               'showHeight': showHeight, 'showStatus': showStatus, 'showSchool': showSchool, 'products': products}

    return render(request, 'showMyData.html', context)

from ProfileApp.models import *
product_list = []
def showProduct(request):
    product = models.Product('p1','mouse','Acer',500.00,120)
    product_list.append(product)
    product = models.Product('p1', 'mouse', 'Acer', 500.00, 120)
    product_list.append(product)
    product = models.Product('p1', 'mouse', 'Acer', 500.00, 120)
    product_list.append(product)
    product = models.Product('p1', 'mouse', 'Acer', 500.00, 120)
    product_list.append(product)
    product = models.Product('p1', 'mouse', 'Acer', 500.00, 120)
    product_list.append(product)
    context = {'product':product_list}
    return render(request,'showOurProduct.html',context)

def newProduct(request):
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
        brand = request.POST['brand']
        price = request.POST['price']
        net = request.POST['net']

        product = Product(id, name, brand, price, net)
        product_list.append(product)
        return redirect('showOurproduct')

    else:
        return render(request, 'frmProductNormal.html')

from ProfileApp.forms import *
def frmProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form = Form.cleaned_data
            id = form.get ('id')
            name = form.get('name')
            brand = form.get ('brand')
            price = form.get ('price')
            net = form.get ('net')
            product = Product(id, name, brand, price,net)
            product_list.appemd(product)
            return redirect('showOurproduct')
        else:
            form = ProductForm(form)
    else:
        form = ProductForm()
        context = {'form':form}

