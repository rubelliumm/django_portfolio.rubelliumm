from django.db import models


class Groups(models.Model):
    name = models.CharField(max_length=2, null=False)

    def __str__(self):
        return self.name


class Teams(models.Model):
    name = models.CharField(max_length=20, null=False)
    team_group = models.ForeignKey(Groups, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
