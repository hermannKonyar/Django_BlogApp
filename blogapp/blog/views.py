from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

data2 = {


    "blogs": [
        {
            'id': 1,
            'title': 'İzmir Köfte',
            'image': '5.jpg',
            'Description': """Malzemeler \n
            Köfte için, kıymayı çukur bir kaba alın. Rendelenmiş soğan, galeta unu, yumurta, bayat ekmek içi, çok ince kıyılmış maydanoz, tuz ve baharatı ekleyip iyice yoğurun.Köfte harcından cevizden biraz daha büyük parçalar koparıp oval köfteler hazırlayın. Kızgın yağda hafifçe kızartıp kağıt havlu üzerine aktarın.Patateslerin kabuğunu soyup elma dilimi şeklinde kesin. Tuzla tatlandırdıktan sonra kızgın yağda hafifçe kızartın.Aynı şekilde kağıt havlu üzerine aktarın. Yemeğin sosu için domatesleri elma dilimi şeklinde doğrayıp salça ile birlikte zeytinyağında karıştırmadan 10 dakika pişirin.Tuz ve toz biberi ekleyip tatlandırın. Sosu ocaktan alın. Isıya dayanıklı bir kaba köfteleri ve patatesleri yerleştirin.Hazırladığınız sosu patates ve köftelerin üzerinde gezdirin. Sivri biberlerin çekirdeklerini temizleyip iri parçalar şeklinde doğrayıp ilave edin.Önceden ısıtılmış 200 dereceye ayarlı fırında 15 dakika pişirin. Şimdiden afiyet olsun.
            """},
        {
            'id': 2,
            'title': 'Hamsi Pilavı',
            'image': '6.jpg',
            'Description': """ Hamsiler güzelce ayıklanır ve kılçıkları temizlenip yıkanır.
            Hamsiler suda bekletilir ve tuz, limon suyu eklenir. Bu sayede hamsi kokusu pilava sinmez. En az 20 dakika.
            Kuş üzümleri bir kaseye alınıp ılık suda bekletilir.
            Pirinçler yıkanıp sıcak suda tuz eklenip bekletilir.
            Tencereye tereyağı ve sıvı yağ koyulur. Soğanlar eklenip kavrulur.
            Fıstıklar eklenip kavurmaya devam edilir.
            Kuş üzümlerinin suyu süzülür ve tencereye eklenir.
            Karabiber, yenibahar, tuz eklenir.
            Pirinçler eklenip suyu da eklenip kısık ateşte pişirilir.
            Pişince maydanoz eklenip karıştırılır.
            Borcam tereyağıyla iyice yağlanır ve hamsiler dizilir.
            İç harcı eklenip gene hamsi dizilir.
            Üzerine çok az sıvı yağ dökülür.
            180 derece fırında 25 dakika kızarana kadar pişirilir. Bende bir Rizeli olarak yöresel yemeğimizi paylaşmak istedim. Afiyet olsun.
            
            """},
        {
            'id': 4,
            'title': 'Etli Ekmek',
            'image': '8.jpg',
            'Description': """ Yaş mayayı biraz ılık suda eritin ve unu ekleyin. Kıvamına göre su ekleyin.
            Hamur, ekmek hamuru kıvamında olacak (ne sert, ne yumuşak) 30-40 dakika kadar hamuru dinlenmeye bırakın.
            Küçük küçük kesilmis soğan, domates ve biberi kıymaya ekleyip yoğurun.
            Yarım çay bardağı sıvı yağ dökün (harcı yumuşak olacak, köfte gibi değil).
            Baharatları da ekleyip karıştırın.
            Hamuru beze haline getirin ve isterseniz tüm tepsiye göre, isterseniz de resimdeki gibi ince bir şekilde açın.
            Harcından üzerine yayın.
            220 derecede kızarana kadar pişirin.
            Üzerini maydanoz ile süsleyerek servis yapın.
            Bu hamurdan 2,5 tepsi çıkıyor. Afiyet olsun.
            
            """}
        
    ]
}

data = {
    "blogs": [
        {
            'id': 1,
            'title': 'Ege Yöresi Yemekleri',
            'image': '5.jpg',
            'isActive': True,
            'isHome': True,
            'Description': 'İzmir Köfte'
        },
        {
            'id': 2,
            'title': 'Karadeniz Yöresi Yemekleri',
            'image': '6.jpg',
            'isActive': True,
            'isHome': True,
            'Description': 'Hamzi Pilavı'
        },
        {
            'id': 3,
            'title': 'Balkan Yemekleri',
            'image': '7.jpg',
            'isActive': True,
            'isHome': True,
            'Description': 'Trileçe'
        },
        {
            'id': 4,
            'title': 'İç Anadolu Yemekleri',
            'image': '8.jpg',
            'isActive': True,
            'isHome': False,
            'Description': 'Etli Ekmek'
        }
    ]
}


def index(request):
    context = {
        "blogs": data['blogs']
    }
    return render(request, "blog/index.html", context)


def blogs(request):
    context = {
        "blogs": data2['blogs']
    }
    return render(request, "blog/blogs.html", context)


def blog_details(request, id):

    blogs = data2['blogs']
    selectedBlog = None

    for blog in blogs:
        if blog['id'] == id:
            selectedBlog = blog

    return render(request, "blog/blogs-details.html", {
        'blog': selectedBlog,
    })


def foods(request):
    context = {
        "blogs": data['blogs']
    }
    return render(request, "blog/blogs.html", context)
