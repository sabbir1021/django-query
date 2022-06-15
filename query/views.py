from django.shortcuts import render, HttpResponse
from django.db.models import Q, F , Count
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    # 1 How to find the query associated with a queryset
    queryset = User.objects.all()
    print(queryset)
    queryset = User.objects.filter(id__gt=2)
    print(queryset)

    # 2 How to do OR queries in Django ORM
    queryset = User.objects.filter(first_name__startswith='m') | User.objects.filter(last_name__startswith='a')
    print(queryset)
    queryset = User.objects.filter(Q(first_name__startswith='m')|Q(last_name__startswith='a'))
    print(queryset)

    # 3 How to do AND queries in Django ORM?
    queryset = User.objects.filter(first_name__startswith="m") & User.objects.filter(last_name__startswith='a')
    print(queryset)
    queryset = User.objects.filter(first_name__startswith="m", last_name__startswith='a')
    print(queryset)
    queryset = User.objects.filter(first_name__startswith="m") & User.objects.filter(last_name__startswith='a')
    print(queryset)

    # 4 How to do a NOT query in Django queryset?
    queryset = User.objects.exclude(id__gt=2)
    print(queryset)
    queryset = User.objects.filter(~Q(id__lt=3))
    print(queryset)

    # 5.1 How to do union of two querysets from same or different models?
    queryset1 = User.objects.filter(id__lt=2)
    queryset2 = User.objects.filter(id__gt=3)
    print(queryset1.union(queryset2))
    queryset = User.objects.filter(id=1).values_list("last_name").union(User.objects.all().values_list("last_name")) # values given key and value but values_list just given value.
    print(queryset)
    
    # 5.2 How to do intersection of two querysets from same or different models?
    queryset1 = User.objects.filter(id__lte=2)
    queryset2 = User.objects.filter(id__gte=2)
    print(queryset1.intersection(queryset2))

    # 6. How to select some fields only in a queryset?
    queryset = User.objects.all().values("last_name")
    print(queryset)
    queryset = User.objects.only("last_name")
    print(queryset)

    # 8. How to filter a queryset with criteria based on comparing their field values
    queryset = User.objects.filter(last_name=F("first_name"))
    print(queryset)

    # 12. Find rows which have duplicate field values
    duplicates = User.objects.values('last_name').annotate(name_count=Count('last_name')).filter(name_count__gt=1)
    queryset = User.objects.filter(last_name__in=[item['last_name'] for item in duplicates])
    print(queryset)
    
    # 13. How to find distinct field values from queryset?
    distinct = User.objects.values('last_name').annotate(name_count=Count('last_name')).filter(name_count=1)
    queryset = User.objects.filter(last_name__in=[item['last_name'] for item in distinct])
    print(queryset)
    
    return HttpResponse("okkk")