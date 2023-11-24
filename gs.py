# Turma ESPY
# Por Gabriela Trevisan (RM99500) e Rafael Henrique Pedra Franck (RM550875).

# Lista para armazenar as operações realizadas pelo usuário
operacoes_realizadas = []

# Variável global para manter o controle dos agendamentos
agendamentos = []

# Variável global para manter o controle dos pacientes
pacientes = []

# Função para adicionar uma operação à lista de operações realizadas
def adicionar_operacao(operacao):
    operacoes_realizadas.append(operacao)

# Função para encontrar UPA mais próxima
def upa_proxima():
    print('')
    print('Você acessou a página "Identificar UPA mais próxima"!')
    print(' -'*30)

    while True:
        print('Escolha uma das opções de bairro:')
        print('1. Tatuapé')
        print('2. Jardim Paulista')
        print('3. Jardim São Paulo')
        print('4. Perdizes')
        print('')

        escolha = input('Digite o número correspondente (1, 2, 3 ou 4), ou digite "V" para voltar ao menu principal: ')
        if escolha.lower() == "v":
            print('Retornando ao menu principal...')
            return
        if escolha not in ["1", "2", "3", "4"]:
            print('')
            print('Opção inválida, por favor, digite "1", "2", "3" ou "4", ou "V" para voltar ao menu principal.')
            continue

        confirmacao = input(f'Você selecionou o bairro {escolha}. Isto está correto? Digite S para SIM e N para NÃO: ')
        if confirmacao.lower() == "s":
            if escolha == "1":
                print('A UPA mais próxima é a UPA Tatuapé! Endereço:  Av. Celso Garcia, 4974')
                adicionar_operacao('Encontrou a UPA mais próxima:  Tatuapé - Av. Celso Garcia, 4974')
            elif escolha == "2":
                print('A UPA mais próxima é a UPA Einstein Ibirapuera! Endereço: Av. República do Líbano, 501')
                adicionar_operacao('Encontrou a UPA mais próxima: Jardim Paulista - Av. República do Líbano, 501')
            elif escolha == "3":
                print('A UPA mais próxima é a UPA Dr. Lauro Ribas Braga! Endereço: R. Voluntários da Pátria, 943')
                adicionar_operacao('Encontrou a UPA mais próxima: Jardim São Paulo - R. Voluntários da Pátria, 943')
            elif escolha == "4":
                print('A UPA mais próxima é a UPA Dr. José Serra Ribeiro! Endereço: Av. Sumaré, 100')
                adicionar_operacao('Encontrou a UPA mais próxima: Perdizes - Av. Sumaré, 100')

            voltar = input('Digite "V" para voltar ao menu principal ou pressione Enter para continuar: ')
            if voltar.lower() == "v":
                return
        elif confirmacao.lower() == "n":
            continue
        else:
            print('Opção inválida, digite "S" para SIM ou "N" para NÃO.')

# Função para encontrar UBS mais próxima
def ubs_proxima():
    print('')
    print('Você acessou a página "Identificar UBS mais próxima"!')
    print(' -'*30)

    while True:
        print('Escolha uma das opções de bairro:')
        print('1. Vila Leopoldina')
        print('2. Mandaqui')
        print('3. Morumbi')
        print('4. Vila Carrão')
        print('')

        escolha_ubs = input('Digite o número correspondente (1, 2, 3 ou 4), ou digite "V" para voltar ao menu principal: ')
        if escolha_ubs.lower() == "v":
            print('Retornando ao menu principal...')
            return
        if escolha_ubs not in ["1", "2", "3", "4"]:
            print('')
            print('Opção inválida, por favor, digite "1", "2", "3" ou "4", ou "V" para voltar ao menu principal.')
            continue

        confirmacao = input(f'Você selecionou o bairro {escolha_ubs}. Isto está correto? Digite S para SIM e N para NÃO: ')
        if confirmacao.lower() == "s":
            if escolha_ubs == "1":
                print('A UBS mais próxima é a UBS Parque da Lapa! Endereço: R. Bergson, 52')
                adicionar_operacao('Encontrou a UBS mais próxima:  Vila Leopoldina - R. Bergson, 52')
            elif escolha_ubs == "2":
                print('A UBS mais próxima é a UBS Vila Barbosa! Endereço: Av. Mandaqui, 1971')
                adicionar_operacao('Encontrou a UBS mais próxima: Mandaqui - Av. Mandaqui, 197')
            elif escolha_ubs == "3":
                print('A UBS mais próxima é a UBS Real Parque [Paulo Mangabeira Albernaz Filho]! Endereço: R. Barão de Melgaço, 339')
                adicionar_operacao('Encontrou a UBS mais próxima: Jardim São Paulo - R. Barão de Melgaço, 339')
            elif escolha_ubs == "4":
                print('A UBS mais próxima é a UBS Vila Carrão! Endereço: R. Dr. Jaci Barbosa, 280')
                adicionar_operacao('Encontrou a UBS mais próxima: Vila Carrão - R. Dr. Jaci Barbosa, 280')

            voltar = input('Digite "V" para voltar ao menu principal ou pressione Enter para continuar: ')
            if voltar.lower() == "v":
                return
        elif confirmacao.lower() == "n":
            continue
        else:
            print('Opção inválida, digite "S" para SIM ou "N" para NÃO.')

# Função para verificar se uma data é válida
# Função para verificar se a data é válida
def data_valida(data):
    try:
        dia, mes, ano = map(int, data.split('/'))
        return 1 <= mes <= 12 and 1 <= dia <= 31 and 1900 <= ano <= 2024
    except ValueError:
        return False

# Função para cadastrar paciente
def cadastro_paciente():
    print('')
    print('Você acessou a página "Cadastrar Paciente"!')
    print(' -'*30)
    print('\nAdicionar paciente:')
    nome = input('Nome do Paciente: ')
    idade = int(input('Idade (apenas números): '))
    data_nascimento = input('Data de Nascimento (dd/mm/aaaa): ')
    data_hoje = input('Data de Hoje (dd/mm/aaaa): ')
    cpf_paciente = int(input('CPF do Paciente: '))

    # Verifica se a data de nascimento é válida e não futura em relação à data de hoje
    if data_valida(data_nascimento) > data_valida(data_hoje):
        print('')
        print('Dados inválidos. O paciente não foi adicionado.')
        return

    paciente = {
        'nome': nome,
        'idade': idade,
        'data_nascimento': data_nascimento,
        'data_hoje': data_hoje,
        'cpf_paciente': cpf_paciente,
        'visualizado': False,
    }

    print('')
    print('Estes dados estão corretos? (S/N)')
    confirma = input().strip().upper()
    if confirma == 'S':
        pacientes.append(paciente)
        print('Paciente adicionado com sucesso.')
        adicionar_operacao('Fez novo cadastro de paciente')
        print('')
    else:
        print('Cadastro de paciente descartado')
        print('')

# Função para agendamento de consulta em UBS
def agendamento_consulta():
    print('')
    print('Você acessou a página "Agendar consulta em UBS"!')
    print(' -'*30)
    print('\nAgendar consulta:')
    ubs_agendamento = input('UBS em que o atendimento será realizado: ')
    nome_paciente = input('Nome do Paciente: ')
    cpf_paciente1 = int(input('CPF do Paciente: '))
    idade_paciente = int(input('Idade (apenas números): '))
    nome_medico = input('Nome do Médico: ')
    crm_medico = int(input('CRM do Médico: '))
    especialidade = input('Especialidade: ')
    data_consulta = input('Data da Consulta (dd/mm/aaaa): ')
    hora_consulta = int(input('Por favor, coloque o horário da consulta no formato 24h (exemplo: 18 [seis da tarde]): '))
    data_atual = input('Data de Hoje (dd/mm/aaaa): ')

    # Verifica se a data de nascimento é válida e não futura em relação à data de hoje
    if data_valida(data_atual) > data_valida(data_consulta):
        print('')
        print('Dados inválidos. O paciente não foi adicionado.')
        return

    agendamento = {
        'ubs_agendamento': ubs_agendamento,
        'nome_paciente': nome_paciente,
        'cpf_paciente1': cpf_paciente1,
        'idade_paciente': idade_paciente,
        'nome_medico': nome_medico,
        'crm_medico': crm_medico,
        'especialidade': especialidade,
        'data_consulta': data_consulta,
        'hora_consulta': hora_consulta,
        'data_atual': data_atual,
        'visualizado': False,
    }

    print('')
    print('Estes dados estão corretos? (S/N)')
    confirma = input().strip().upper()
    if confirma == 'S':
        agendamentos.append(agendamento)
        print('Agendamento realizado com sucesso.')
        adicionar_operacao('Agendou nova consulta')
        print('')
    else:
        print('Agendamento descartado')
        print('')

# Função para "imprimir" o agendamento da consulta (salvar o agendamento da consulta em .txt)
def imprimir_agendamento(agendamentos):
    try:
        with open("agendamento_consulta.txt", "w") as arquivo:
            arquivo.write('Detalhes do Agendamento:\n')
            arquivo.write('\n')
            arquivo.write(f'UBS: {agendamentos["ubs_agendamento"]}\n')
            arquivo.write(f'Nome do Paciente: {agendamentos["nome_paciente"]}\n')
            arquivo.write(f'CPF do Paciente: {agendamentos["cpf_paciente1"]}\n')
            arquivo.write(f'Idade do Paciente: {agendamentos["idade_paciente"]}\n')
            arquivo.write(f'Nome do Medico: {agendamentos["nome_medico"]}\n')
            arquivo.write(f'CRM do Medico: {agendamentos["crm_medico"]}\n')
            arquivo.write(f'Especialidade: {agendamentos["especialidade"]}\n')
            arquivo.write(f'Data da Consulta: {agendamentos["data_consulta"]}\n')
            arquivo.write(f'Horario da Consulta: {agendamentos["hora_consulta"]}\n')
            arquivo.write(f'Data Atual: {agendamentos["data_atual"]}\n')
            arquivo.write('\n')
        print('Agendamento salvo em "agendamento_consulta.txt"')
    except Exception as e:
        print(f'Ocorreu um erro ao salvar o agendamento: {e}')


# No loop principal do programa, adicione uma opção para salvar o resumo em um arquivo .txt
while True:
    print('')
    print(' -' * 30)
    print('Bem-vindo à plataforma de agendamentos SUSTech')
    print(' -' * 30)
    print('Atualmente, possuímos algumas opções para facilitar o agendamento de consultas em UBSs após a ida do paciente a UPA:')
    print('1. Identificar UPA mais próxima')
    print('2. Identificar UBS mais próxima')
    print('3. Cadastro de Paciente')
    print('4. Agendar consulta em UBS')
    print('5. Resumo de Operações')
    print('6. Imprimir o último agendamento de consulta realizado')
    print('7. Sair')
    print('')
    opcao = input('Por favor, digite sua opção: ')
    print(' -' * 30)

    if opcao == '1':
        upa_proxima()
    elif opcao == '2':
        ubs_proxima()
    elif opcao == '3':
        cadastro_paciente()
    elif opcao == '4':
        agendamento_consulta()
    elif opcao == '5':
        print('Resumo das operações realizadas:')
        for operacao in operacoes_realizadas:
            print(f'- {operacao}')
    elif opcao == '6':
        if agendamentos:
            imprimir_agendamento(agendamentos[-1])  # Imprime o último agendamento
        else:
            print('Nenhum agendamento disponível para imprimir.')
        print('')
    elif opcao == '7':
        confirmacao = input('Deseja realmente encerrar o programa? (S/N): ').strip().upper()
        if confirmacao == 'S':
            print('')
            print('Resumo das operações realizadas:')
            for operacao in operacoes_realizadas:
                print(f'- {operacao}')
            print('')
            print('Encerrando o programa. Obrigado por utilizar o SUSTech. Até logo!')
            break
    else:
        print('Opção inválida.')