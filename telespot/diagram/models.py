from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class YearlyPlan(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    plan_value = models.IntegerField(null=True)


class YearlyFact(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    fact_value = models.IntegerField(null=True)
