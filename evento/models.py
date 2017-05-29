from django.db import models
from django.utils import timezone

#__1
class Evento(models.Model):
    nome = models.CharField('nome', max_length=200)
    eventoPrincipal = models.CharField('eventoPrincipal', max_length=200)
    sigla = models.CharField('sigla', max_length=20)
    dataEHoraDeInicio = models.DateTimeField('dataEHoraDeInicio', default=timezone.now)
    palavrasChave = models.CharField('palavrasChave', max_length=200)
    logotipo = models.CharField('logotipo', max_length=200)
    realizador = models.ForeignKey('Pessoa')
    cidade = models.TextField('cidade', blank=True, null=True)
    uf = models.CharField('uf', max_length=2)
    endereco = models.TextField('endereco', blank=True, null=True)
    cep = models.TextField('cep', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        self.eventoPrincipal = self.eventoPrincipal.upper()

        super(Evento, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.nome)

#__2
class EventoCientifico(Evento):
    issn = models.CharField('issn', max_length=200)

    def __str__(self):
        return '{}'.format(self.issn)

#__3
class Pessoa(models.Model):
    nome = models.CharField('nome', max_length=200)
    email = models.CharField('email', max_length=200)

    def __str__(self):
        return '{}'.format(self.nome)

#__
class PessoaFisica(Pessoa):
    cpf = models.CharField('cpf', max_length=20)

    def __str__(self):
        return '{}'.format(self.cpf)

#__4
class PessoaJuridica(Pessoa):
    cnpj = models.CharField('cnpj', max_length=100)
    razaoSocial = models.CharField('razaoSocial', max_length=200)

    def __str__(self):
        return '{}'.format(self.cnpj)

#__5
class Autor(Pessoa):
    curriculo = models.CharField('curriculo', max_length=200)

    def __str__(self):
        return '{}'.format(self.curriculo)

#__6
class ArtigoCientifico(models.Model):
    titulo = models.CharField('titulo', max_length=200)
    evento = models.ForeignKey('EventoCientifico')

    def __str__(self):
        return '{}'.format(self.titulo)

#__7
class Inscricoes(models.Model):
    pessoa = models.ForeignKey('PessoaFisica')
    evento = models.ForeignKey('Evento')
    dataEHoraDaInscricao = models.DateTimeField('dataEHoraDaInscricao', default=timezone.now)
    tipoInscricao = models.ForeignKey('TipoInscricao')

    def __str__(self):
        return '{}'.format(self.pessoa)

#__8
class TipoInscricao(models.Model):
    descricao = models.CharField('descricao', max_length=200)

    def __str__(self):
        return '{}'.format(self.descricao)

#__9
class ArtigoAutor(models.Model):
    artigoCientifico = models.ForeignKey('ArtigoCientifico')
    autor = models.ForeignKey('Autor')

    def __str__(self):
        return '{}'.format(self.artigoCientifico)
