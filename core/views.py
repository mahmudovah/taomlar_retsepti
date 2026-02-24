from django.shortcuts import render, redirect
from .models import Comment, Meal, Ingredient

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


def meal_add(request):
    ingredients=Ingredient.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        description =request.POST.get("description")
        image = request.FILES.get("image")
        ingredient_ids = request.POST.getlist("ingredients")
        status = request.POST.get("status")

        meal = Meal.objects.create(
                name=name,
                description=description,
                image=image,
                status=status
            )        
        meal.ingredients.set(ingredient_ids)

        return redirect("meal_add")
    return render(request, "meal_add.html", {"ingredients":ingredients})