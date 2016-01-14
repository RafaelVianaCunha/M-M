from django.forms import Form, CharField
from django.forms.forms import NON_FIELD_ERRORS
from django.forms.util import ErrorList


class CadastrarProdutoForm(Form):
    nome = CharField(required=True)
    #valor = CharField
    #tecido = CharField
    #tamanho = CharField
    #fabricante = CharField
    #descricao = CharField

    def is_valid(self):
        valid = True
        if not super(CadastrarProdutoForm,self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados')
            valid = False

        return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(NON_FIELD_ERRORS, ErrorList())
        errors.append(message)