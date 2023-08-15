import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "telespot.settings")
import django

django.setup()
from diagram.models import City, YearlyPlan, YearlyFact


def add_city_data(city_name, plan_values, fact_values):
    city, created = City.objects.get_or_create(name=city_name)
    for year, plan, fact in zip(range(2018, 2024), plan_values, fact_values):
        yearly_plan, created = YearlyPlan.objects.get_or_create(city=city, year=year)
        yearly_plan.plan_value = plan
        yearly_plan.save()
        yearly_fact, created = YearlyFact.objects.get_or_create(city=city, year=year)
        yearly_fact.fact_value = fact
        yearly_fact.save()
    print(f"Data added for {city_name}")


city_data = [
    {
        "name": "Москва",
        "plan_values": [550000, 605000, 665500, 732050, 805255, 885781],
        "fact_values": [625000, 580000, 665600, 780000, 903564, 833423],
    },
    {
        "name": "Екатеринбург",
        "plan_values": [0, 0, 1100000, 1210000, 1331000, 1464100],
        "fact_values": [0, 0, 1400000, 1240000, 1100000, 956465],
    },
    {
        "name": "Саратов",
        "plan_values": [355000, 390500, 429550, 0, 515460, 0],
        "fact_values": [340500, 386785, 550000, 0, 657948, 0],
    },
    {
        "name": "Пенза",
        "plan_values": [154000, 169400, 186340, 204974, 225471, 248019],
        "fact_values": [130500, 154000, 196550, 220434, 298000, 180564],
    },
]
for city_info in city_data:
    add_city_data(city_info["name"], city_info["plan_values"], city_info["fact_values"])
