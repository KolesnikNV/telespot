from django.shortcuts import render
from .models import City, YearlyPlan, YearlyFact


def diagram_page(request):
    cities = City.objects.all()
    data = {}
    for city in cities:
        plans = YearlyPlan.objects.filter(city=city)
        facts = YearlyFact.objects.filter(city=city)
        years = {plan.year for plan in plans} | {fact.year for fact in facts}
        data[city.name] = {"years": list(years), "plans": [], "facts": []}
        for year in years:
            plan = plans.filter(year=year).first()
            fact = facts.filter(year=year).first()
            data[city.name]["plans"].append(plan.plan_value if plan else 0)
            data[city.name]["facts"].append(fact.fact_value if fact else 0)
    return render(request, "diagram_page.html", {"data": data})
