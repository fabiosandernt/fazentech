from django.db import models

# Create your models here.
class Setor(models.Model):
    nome = models.CharField(max_length=100, null=False)
    slug = models.CharField(max_length=15)
    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=100, null=False)
    cpf = models.CharField(max_length=100, null=False)
    setor = models.ForeignKey('Setor', on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class TipoEstabelecimento(models.Model):
    nome = models.CharField(max_length=100, null=False)
    slug = models.CharField(max_length=15)
    def __str__(self):
        return self.nome

class Varegista(models.Model):
    nome = models.CharField(max_length=100, null=False)
    cnpj = models.CharField(max_length=14, null=False)
    endereco = models.CharField(max_length=100, null=False)
    tipo_estabelecimento = models.ForeignKey('TipoEstabelecimento', on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class TipoEquipamento(models.Model):
    nome = models.CharField(max_length=100, null=False)
    slug = models.CharField(max_length=15)
    def __str__(self):
        return self.nome

class Equipamento(models.Model):
    nome = models.CharField(max_length=100, null=False)
    quantidade = models.IntegerField(default=0)
    tipo = models.ForeignKey('TipoEquipamento', on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class EspecieDeVaca(models.Model):
    nome = models.CharField(max_length=100, null=False)
    slug = models.CharField(max_length=15)
    def __str__(self):
        return self.nome

class TipoDeProducao(models.Model):
    nome = models.CharField(max_length=100, null=False)
    slug = models.CharField(max_length=15)
    def __str__(self):
        return self.nome

class ControleDeAnimal(models.Model):
    nome = models.CharField(max_length=100, null=False)
    data_chegada = models.DateField()
    data_ultima_producao = models.DateField()
    def __str__(self):
        return self.nome

class ProducaoDeLeite(models.Model):
    inseminacao = models.BooleanField(default=False)
    ultima_ordenha = models.DateField()
    temperatura_armazenamento = models.IntegerField()
    especie = models.ForeignKey('EspecieDeVaca', on_delete=models.CASCADE)
    animal = models.ForeignKey('ControleDeAnimal', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.ultima_ordenha)

class ControleDePlantio(models.Model):
    nome = models.CharField(max_length=100, null=False)
    data_chegada = models.DateField()
    data_ultima_producao = models.DateField()
    def __str__(self):
        return self.nome

class Producao(models.Model):
    produto = models.CharField(max_length=100, null=False)
    quantidade = models.IntegerField()
    valor = models.FloatField()
    peso = models.FloatField()
    tipo = models.ForeignKey('TipoDeProducao', on_delete=models.CASCADE)
    def __str__(self):
        return self.produto
