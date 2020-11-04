from django.shortcuts import render
from .models import *
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

def busca_binaria(vet, num):
    esquerda, direita = 0, len(vet)
    while 1:
        meio = (esquerda + direita) // 2
        aux_num = vet[meio]

        if num == aux_num.id:
            return aux_num
        elif num > aux_num.id:
            esquerda = meio
        else:
            direita = meio

class TesteView(View):
    def get(self, request):
        return render(request, 'index.html')

# CREATE
class VaregistaView(View):
    def get(self, request):
        tipo_estabelecimento = TipoEstabelecimento.objects.all()
        return render(request, 'varegista.html', {'tipo_estabelecimentos':tipo_estabelecimento})

    def post(self, request):
        print(request.POST)
        try:
            tipo = TipoEstabelecimento.objects.get(slug=request.POST['tipo_estabelecimento'])

            varegista = Varegista()
            varegista.nome = request.POST['nome']
            varegista.cnpj = request.POST['cnpj']
            varegista.endereco = request.POST['endereco']
            varegista.tipo_estabelecimento = tipo
            varegista.save()

        except Exception as e:
            print(e)

        tipo_estabelecimento = TipoEstabelecimento.objects.all()

        return render(request, 'varegista.html', {'tipo_estabelecimentos':tipo_estabelecimento})

class EquipamentoView(View):
    def get(self, request):
        tipo_equipamento = TipoEquipamento.objects.all()
        return render(request, 'equipamento.html', {'tipo_equipamentos':tipo_equipamento})

    def post(self, request):
        print(request.POST)
        try:
            tipo = TipoEquipamento.objects.get(slug=request.POST['tipo_equipamento'])

            equipamento = Equipamento()
            equipamento.nome = request.POST['nome']
            equipamento.quantidade = request.POST['quantidade']
            equipamento.tipo = tipo
            equipamento.save()

        except Exception as e:
            print(e)

        tipo_equipamento = TipoEquipamento.objects.all()

        return render(request, 'equipamento.html', {'tipo_equipamentos':tipo_equipamento})

class ProducaoDeLeiteView(View):
    def get(self, request):
        especie_de_vaca = EspecieDeVaca.objects.all()
        controle_de_animal = ControleDeAnimal.objects.all()

        return render(request, 'producaodeleite.html', {'especie_de_vacas':especie_de_vaca,
                                                        'controle_de_animais':controle_de_animal})

    def post(self, request):
        print(request.POST)
        try:
            especie = EspecieDeVaca.objects.get(slug=request.POST['especie_de_vaca'])
            controle = ControleDeAnimal.objects.get(id=request.POST['controle_de_animal'])
            producao_de_leite = ProducaoDeLeite()

            if request.POST['inseminacao'] == 'sim':
                producao_de_leite.inseminacao = True
            else:
                producao_de_leite.inseminacao = False

            producao_de_leite.ultima_ordenha = request.POST['ultima_ordenha']
            producao_de_leite.temperatura_armazenamento = request.POST['temperatura_armazenamento']
            producao_de_leite.especie = especie
            producao_de_leite.animal = controle
            producao_de_leite.save()

        except Exception as e:
            print(e)

        especie_de_vaca = EspecieDeVaca.objects.all()
        controle_de_animal = ControleDeAnimal.objects.all()

        return render(request, 'producaodeleite.html', {'especie_de_vacas': especie_de_vaca,
                                                        'controle_de_animais': controle_de_animal})

class FuncionarioView(View):
    def get(self, request):
        setor = Setor.objects.all()
        return render(request, 'funcionario.html', {'setores':setor})

    def post(self, request):
        print(request.POST)
        try:
            setor_funcionario = Setor.objects.get(slug=request.POST['setor'])

            funcionario = Funcionario()
            funcionario.nome = request.POST['nome']
            funcionario.cpf = request.POST['cnpj']
            funcionario.setor = setor_funcionario
            funcionario.save()

        except Exception as e:
            print(e)

        setor = Setor.objects.all()
        return render(request, 'funcionario.html', {'setores': setor})

class ProducaoView(View):
    def get(self, request):
        tipo_producao = TipoDeProducao.objects.all()
        return render(request, 'tipodeproducao.html', {'tipo_producoes':tipo_producao})

    def post(self, request):
        print(request.POST)
        try:
            tipo = TipoDeProducao.objects.get(slug=request.POST['tipo_producao'])

            producao = Producao()
            producao.produto = request.POST['produto']
            producao.quantidade = request.POST['quantidade']
            producao.valor = request.POST['valor']
            producao.peso = request.POST['peso']
            producao.tipo = tipo
            producao.save()

        except Exception as e:
            print(e)

        tipo_producao = TipoDeProducao.objects.all()
        return render(request, 'tipodeproducao.html', {'tipo_producoes': tipo_producao})

class ControleDePlantioView(View):
    def get(self, request):

        return render(request, 'animaleplantio.html')

    def post(self, request):
        print(request.POST)
        try:

            controledeplantio = ControleDePlantio()
            controledeplantio.nome = request.POST['nome']
            controledeplantio.data_chegada = request.POST['data_chegada']
            controledeplantio.data_ultima_producao = request.POST['data_ultima_producao']
            controledeplantio.save()

        except Exception as e:
            print(e)


        return render(request, 'animaleplantio.html')

class ControleDeAnimalView(View):
    def get(self, request):

        return render(request, 'animaleplantio.html')

    def post(self, request):
        print(request.POST)
        try:

            controledeAnimal = ControleDeAnimal()
            controledeAnimal.nome = request.POST['nome']
            controledeAnimal.data_chegada = request.POST['data_chegada']
            controledeAnimal.data_ultima_producao = request.POST['data_ultima_producao']
            controledeAnimal.save()

        except Exception as e:
            print(e)


        return render(request, 'animaleplantio.html')

class BuscaBinariaView(View):
    def get(self, request):

        valores = ProducaoDeLeite.objects.all().values('animal').distinct()
        print(valores)
        vacas = []
        for vaca in valores:
            vacas.append(vaca['animal'])

        return render(request, 'buscabinaria.html',{'vacas':vacas})

    def post(self, request):
        animais = ControleDeAnimal.objects.all()
        vaca_encontrada = busca_binaria(animais, int(request.POST['animal']))
        print(vaca_encontrada)

        valores = ProducaoDeLeite.objects.all().values('animal').distinct()
        print(valores)
        vacas = []
        for vaca in valores:
            vacas.append(vaca['animal'])

        return render(request, 'buscabinaria.html', {'vacas': vacas,
                                                     'vaca_encontrada':vaca_encontrada})

#READ
class ListaView(View):
    def get(self, request):
        varegista =  Varegista.objects.all()
        return render(request, 'listavaregista.html', {'varegistas': varegista})

#UPDATE e DELETE
class UpdateDeleteView(View):
    def get(self, request, pk=None):
        varegista = Varegista.objects.get(pk=pk)
        tipo_estabelecimento = TipoEstabelecimento.objects.all()
        return render(request, 'update.html', {'varegista': varegista, 'tipo_estabelecimentos': tipo_estabelecimento})

    def post(self, request, pk=None):
        print(request.POST)
        try:
            tipo = TipoEstabelecimento.objects.get(slug=request.POST['tipo_estabelecimento'])
            varegista = Varegista.objects.get(pk=pk)
            varegista.nome = request.POST['nome']
            varegista.cnpj = request.POST['cnpj']
            varegista.endereco = request.POST['endereco']
            varegista.tipo_estabelecimento = tipo
            varegista.save()

        except Exception as e:
            print(e)

        tipo_estabelecimento = TipoEstabelecimento.objects.all()

        return render(request, 'update.html', {'varegista': varegista, 'tipo_estabelecimentos': tipo_estabelecimento})


class DeleteView(View):
    def post(self, request, pk=None):
        varegista = Varegista.objects.get(pk=pk)
        varegista.delete()
        return HttpResponseRedirect(reverse('lista'))