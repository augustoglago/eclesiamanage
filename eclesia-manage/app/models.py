from django.db import models

class Membro(models.Model):
    nomeMembro = models.CharField(max_length=150)
    enderecoMembro = models.CharField(max_length=200)
    telefoneMembro = models.CharField(max_length=11)
    dataNascimentoMembro = models.DateField()

    def __str__(self):
        return self.nomeMembro
    

class Visita(models.Model):
    localVisita = models.CharField(max_length=200)
    dataVisita = models.DateField()
    anfitriaoVisita = models.ForeignKey(Membro, on_delete=models.CASCADE, related_name='visitas_anfitriao')  # Adicionado related_name

    def __str__(self):
        return self.localVisita
    

class Ministerio(models.Model):
    nomeMinisterio = models.CharField(max_length=50)
    descricaoMinisterio = models.CharField(max_length=300)
    liderMinisterio = models.ForeignKey(Membro, on_delete=models.CASCADE, related_name='lider_ministerio')  # Adicionado related_name
    membrosMinisterio = models.ManyToManyField(Membro, related_name='ministerios')  # Adicionado related_name

    def __str__(self):
        return self.nomeMinisterio


class TipoInstrumento(models.Model):
    nomeTipoInstrumento = models.CharField(max_length=50)

    def __str__(self):
        return self.nomeTipoInstrumento


class Instrumento(models.Model):
    nomeInstrumento = models.CharField(max_length=50)
    instrumentistaInstrumento = models.ManyToManyField(Membro, related_name='instrumentos')  # Adicionado related_name
    tipoInstrumento = models.ForeignKey(TipoInstrumento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomeInstrumento
    

class Funcao(models.Model):
    nomeFuncao = models.CharField(max_length=50)
    descricaoFuncao = models.CharField(max_length=300)
    membroFuncao = models.ManyToManyField(Membro, related_name='funcoes')  # Adicionado related_name

    def __str__(self):
        return self.nomeFuncao
    

class PequenoGrupo(models.Model):
    membrosPequenoGrupo = models.ManyToManyField(Membro, related_name='pequenos_grupos')  # Adicionado related_name
    nomePequenoGrupo = models.CharField(max_length=100)
    localPequenoGrupo = models.CharField(max_length=200)
    liderPequenoGrupo = models.ForeignKey(Membro, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomePequenoGrupo
    

class Evento(models.Model):
    nomeEvento = models.CharField(max_length=100)
    dataEvento = models.DateField()
    localEvento = models.CharField(max_length=200)

    def __str__(self):
        return self.nomeEvento
