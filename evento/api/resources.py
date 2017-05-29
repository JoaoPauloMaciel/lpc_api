from tastypie.resources import ModelResource
from tastypie import fields, utils
from evento.models import *
from django.contrib.auth.models import User
from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized

#1
class TipoInscricaoResource(ModelResource):
    def obj_create(self, bundle, **kwargs):
        print (bundle.data)

        tipo=TipoInscricao()
        tipo.descricao=bundle.data['descricao'].upper()

        if TipoInscricao.objects.filter(descricao=tipo).exists():
            raise Unauthorized ('Já existe tipo com esse nome!')

        else:
            tipo.save()

        bundle.obj=tipo
        return bundle

    def obj_delete_list(self, bundle, **kwargs):
        #print (bunble.date)
        raise Unauthorized ('Ação invalida! Não altorizado para realuzar está ação.')


    class Meta:
        queryset = TipoInscricao.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith',)
        }

#
class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        allowed_methods = ['get', 'post','delete', 'put']
        resource_name = 'user'
        excludes = ['password', 'is_active']

#2
class PessoaResource(ModelResource):
    class Meta:
        queryset = Pessoa.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith',)
        }

class EventoResource(ModelResource):
    realizador = fields.ToOneField(PessoaResource, 'realizador')
    #tipoinscricao = fields.ToOneField(TipoInscricaoResource, 'tipoInscricao')

    class Meta:
        queryset = Evento.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith',)
        }

class InscricaoResource(ModelResource):

    pessoa = fields.ToOneField(PessoaResource, 'pessoa')
    evento = fields.ToOneField(EventoResource, 'evento')
    tipoinscricao = fields.ToOneField(TipoInscricaoResource, 'tipoInscricao')

    def obj_create(self, bundle, **kwargs):
        inscP = bundle.data['pessoa'].split("/")
        inscE = bundle.data['evento'].split("/")
        inscT = bundle.data['tipoinscricao'].split("/")
        print(inscP[4], inscE[4], inscT[4])

        tipo=Inscricoes()
        tipo.pessoa = PessoaFisica.objects.get(pk = int(inscP[4]))
        tipo.evento = Evento.objects.get(pk = int(inscE[4]))
        tipo.tipoInsc = TipoInscricao.objects.get(pk = int(inscT[4]))

        #print(tipo.tipoInsc)

        if Inscricoes.objects.filter(pessoa = inscP[4]).exists() and  Inscricoes.objects.filter(evento = inscE[4]).exists():
            raise Unauthorized ('Já existe Inscricao com esse nome!')

        else:

            tipo.save()
            bundle.obj=tipo
        return bundle

        def obj_delete_list(self, bundle, **kwargs):
            #print (bunble.date)
            raise Unauthorized ('Ação invalida! Não altorizado para realuzar está ação.')


    class Meta:
        queryset = Inscricoes.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith',)
        }




#3
class PessoaFisicaResource(ModelResource):
    class Meta:
        queryset = PessoaFisica.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith',)
        }


#4
class PessoaJuridicaResource(ModelResource):
    class Meta:
        queryset = PessoaJuridica.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith',)
        }

#7
class EventoCientificoResource(ModelResource):

    class Meta:
        queryset = EventoCientifico.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith',)
        }


#8
class AutorResource(ModelResource):
    class Meta:
        queryset = Autor.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith',)
        }

#9
class ArtigoCientificoResource(ModelResource):
    evento = fields.ToOneField(EventoCientificoResource, 'evento')
    class Meta:
        queryset = ArtigoCientifico.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith',)
        }

#10
class ArtigoAutorResource(ModelResource):
    artigoCientifico = fields.ToOneField(ArtigoCientificoResource, 'artigoCientifico')
    autor = fields.ToOneField(AutorResource, 'autor')
    class Meta:
        queryset =  ArtigoAutor.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith',)
        }
