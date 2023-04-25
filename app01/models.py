from django.db import models


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)


class BreastCancer(models.Model):
    clump_thickness = models.FloatField()
    uniformity_of_cell_size = models.FloatField()
    uniformity_of_cell_shape = models.FloatField()
    marginal_adhesion = models.FloatField()
    single_epithelial_cell_size = models.FloatField()
    bare_nuclei = models.FloatField()
    bland_chromatin = models.FloatField()
    normal_nucleoli = models.FloatField()
    mitoses = models.FloatField()
    result = models.BooleanField(null=True)
