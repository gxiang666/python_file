from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from App.models import Animal


def hello(request):
    template = loader.get_template('Hello.html')
    print(template)
    # result = template.render(context={"haha":"你哈什么哈"})
    result = template.render()
    print(result)
    return HttpResponse(result)
    # return render(request, 'Hello.html')
    # return HttpResponse("<h1>HelloWorld</h1>")


def get_animals(request):
    animals = Animal.objects.all()

    data_dict = {
        "msg":"ok",
        "status":200
    }

    # return render(request, 'AnimalList.html', context={"animals": animals, "data": data_dict})
    return render(request, 'AnimalList.html', context={"data": data_dict})


def get_animals_two(request):
    animals = Animal.objects.all()
    score = 60
    val1 = 100
    val2 = 100
    content = """<h1>呵呵呵</h1><script>

    var h3s = document.getElementsByTagName('h2');
    for(var i = 0; i < h3s.length; i++){
        h3s[i].innerHTML = '德玛西亚'+i;
    }

    </script>"""
    return render(request, 'AnimalListTwo.html', context={"animals": animals, "score": score, "value1": val1, "value2": val2, "content": content})


def index(request):
    return render(request, 'index.html')


def index_two(request):
    return render(request, 'index_two.html')


def index_three(request):
    return render(request, 'index_three.html')
