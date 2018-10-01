class Pessoa():
    nome = ''
    telefone = ''
    email = ''
    endereco = ''

    def clean_telefone(self, telefone):
        if len(telefone) < 8:
            raise NameError('Telefone inválido!')
        return telefone

    def clean_email(self, email):
        if email.find('@') == -1 or email.find('.com') == -1:
            raise NameError('Email inválido!')
        return email

    def __init__(self, nome, telefone, email, endereco):
        self.email = self.clean_email(email)
        self.telefone = self.clean_telefone(telefone)
        self.nome = nome
        self.endereco = endereco

    def __str__(self):
        return 'Nome: {}, Telefone: {}, Email: {}, Endereço: {}'.format(self.nome, self.telefone, self.email, self.endereco)
    
    # monkeypatch pra utilizar o método __str__ ao exibir o objeto dentro de uma lista.
    __repr__ = __str__

class Agenda():
    contatos = {}

    def adiciona_contato(self, Pessoa):
        self.contatos[Pessoa.nome] = Pessoa

    def remove_contato(self, nome):
        print('Contato removido: \n', self.contatos.pop(nome, 'Contato não encontrado.'))

    def limpa_agenda(self):
        self.contatos.clear()
        print('Agenda limpa.')

    def exibe(self):
        if len(self.contatos) > 0:
            for i,el in enumerate(self.contatos):
                print(str(i+1)+':',self.contatos.get(el),'\n')
        else:
            print('Nenhuma entrada.')

    def consulta(self, nome):
        entradas = []
        for el in self.contatos:
            if el.find(nome) != -1:
                entradas.append(self.contatos.get(el))
        if len(entradas) == 0:
            print('Nenhum contato encontrado.')
        else:
            for i,el in enumerate(entradas):
                print(str(i+1)+':', el)
        #print('\n',self.contatos.get(nome, 'Não encontrado!'))

def main():
    agenda = Agenda()
    while True:
        print('\nDeseja inserir, consultar ou excluir?')
        s = int(input('\n Inserir [1] - Consultar [2] - Excluir [3]\n'))

        if s == 1:
            nome = input('Insira o nome: ')
            telefone = input('Insira o telefone: ')
            email = input('Insira o email: ')
            endereco = input('Insira o endereço: ')
            pessoa = Pessoa(nome, telefone, email, endereco)
            agenda.adiciona_contato(pessoa)
        elif s == 2:
            print('\nBuscar por nome ou listar todos?')
            s = int(input('\n Buscar [1] - Listar todos [2]\n'))
            if s == 1:
                consulta = input('Insira o nome a ser buscado: ')
                agenda.consulta(consulta)
            else:
                agenda.exibe()
        elif s == 3:
            print('\nExcluir 1 ou excluir todos?')
            s = int(input('\n Somente 1 entrada [1] - Excluir todos [2]\n'))
            if s == 1:
                ex_nome = input('Insira o nome a ser excluído: ')
                agenda.remove_contato(ex_nome)
            elif s == 2:
                confirmacao = input('Tem certeza? (s/n)\n')
                if confirmacao.lower() == 's':
                    agenda.limpa_agenda()
                else:
                    print('Operação cancelada!')
        else:
            print('Opcão inválida!')
        
# entrypoint
main()