from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
        "my_list" : [
            {"restaurant_name" : "five guys",
            "food_type" : "burgers"},
            {"restaurant_name" : "chipotle",
            "food_type" : "mexican"},
            {"restaurant_name" : "mcdonalds",
            "food_type" : "fast food"}
        ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        "my_object" :
            {"restaurant_name" : "chipotle",
            "food_type" : "mexican"}
        

    }
    return render(request, 'detail.html', context)
