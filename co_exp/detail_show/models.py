from django.db import models

# Create your models here.
class genelist(models.Model):
    geneaccession = models.CharField(max_length=15)
    coexpress_gene = models.CharField(max_length=15)
    cor = models.CharField(max_length=100)
    p_value = models.CharField(max_length=100)

class ontology(models.Model):
    geneaccession = models.CharField(max_length=15)
    geneontology = models.CharField(max_length=200)

class kegg(models.Model):
    geneaccession = models.CharField(max_length=15)
    genekegg = models.CharField(max_length = 100)

class descs(models.Model):
    geneaccession = models.CharField(max_length=15)
    description = models.CharField(max_length=200)
    alias = models.CharField(max_length=20)
    location = models.CharField(max_length=100)

class heatmap(models.Model):
    geneaccession = models.CharField(max_length=15)
    runid = models.CharField(max_length=12)
    tpm = models.CharField(max_length=20)
    tissue = models.CharField(max_length=15)