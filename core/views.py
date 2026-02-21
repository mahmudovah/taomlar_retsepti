from django.shortcuts import render, redirect
from .models import Comment, Meal

# Create your views here.

def index_view(request):
    meals = Meal.objects.filter(status='activ')
    print(meals)
    context = {'meals':meals}
    return render(request, 'index.html', context)

def meal_detail(request, pk):
    meal = Meal.objects.get(id=pk)
    comments = Comment.objects.filter(meal=meal).order_by("-created_at")

    if request.method == "POST":
        author = request.POST.get("author")
        body = request.POST.get("body")
        Comment.objects.create(
            meal=meal,
            author = author,
            body = body
        )
        return redirect("meal_detail", meal.id)
    return render(request, "meal_detail.html", context={"meal": meal,"comments":comments})

def contact_view(request):
    return render(request, "contact.html")
