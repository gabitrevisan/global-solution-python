TURMA ESPY

INTEGRANTES DO GRUPO:
- Gabriela Trevisan da Silva (RM99500)
- Rafael Henrique Pedra Franck (RM550875)

O PROBLEMA:
Desde sua implementação, as Unidades de Pronto Atendimento (UPA) têm sido um ponto crucial no atendimento emergencial à saúde ao sempre operarem com máxima capacidade. No entanto, uma lacuna persistente tem sido a desconexão com as Unidades Básicas de Saúde (UBS), resultando em dificuldades significativas para o agendamento de consultas especializadas, como por exemplo nas áreas de cardiologia e neurologia.
A falta de um sistema integrado que facilite a transição do atendimento de emergência para a continuidade do cuidado nas UBSs tem sido uma barreira constante. Isso impacta diretamente na qualidade de vida dos pacientes que necessitam de acompanhamento especializado após uma visita à UPA, pois o agendamento de consultas específica, torna-se complexo e, por vezes, inacessível, na maneira em que o próprio paciente tem que marcá-la.
Essa desconexão entre os serviços de emergência e a sequência de assistência afeta diretamente a qualidade de vida dos pacientes. A ausência de um sistema eficiente de encaminhamento e agendamento de consultas especializadas compromete não apenas a eficácia do tratamento, mas também prolonga o tempo de espera, gerando angústia e potenciais complicações de saúde para aqueles que buscam atendimento contínuo e direcionado.
A necessidade premente é a implementação de um sistema unificado que permita a comunicação ágil entre UPAs e UBSs. Esse sistema possibilitaria não apenas o registro imediato das necessidades do paciente, mas também a facilitação do agendamento e encaminhamento para consultas especializadas, como as de cardiologia e neurologia, citadas anteriormente.
Além disso, a conscientização sobre a importância desse sistema entre os profissionais de saúde e os pacientes é essencial. Educar e informar sobre os benefícios de um sistema conectado ajudaria a promover o acesso adequado aos cuidados de saúde, diminuindo as lacunas existentes entre os serviços de emergência e os de atenção primária.
Em suma, a ausência de um sistema que conecte eficientemente as UPAs com as UBSs cria um obstáculo significativo no acesso e na continuidade do cuidado para consultas especializadas, como as de cardiologia e neurologia. A implementação de um sistema integrado é imperativa para garantir um atendimento eficaz e contínuo, priorizando a saúde e o bem-estar dos pacientes.

A SOLUÇÃO:
Em conjunto, a dupla concluiu que existem diversos problemas relacionados a área da saúde, tanto pública quanto privada, mas decidimos seguir com o primeiro problema identificado: a falta de integração entre todos os sistemas de saúde pública.
De início, procuramos conversar com um indivíduo, mais precisamente o coordenador da UPA Campo-Limpo, que trabalha na área da saúde há mais de quinze anos, e possui experiência nos setores público e privado. Relatamos o problema encontrado e questionamos se ainda ocorre com frequência, e como esperado, recebemos uma resposta afirmativa. A partir disso, a dupla realizou um brainstorm para encontrar a melhor solução possível e que se adequava aos conhecimentos adquiridos em sala de aula.
A resolução foi a criação de uma interface que, à princípio, conecte a Unidade de Pronto Atendimento (UPA) com a Unidade Básica de Saúde (UBS); assim resolvendo a maior dor dos pacientes de unidades públicas que, quando iniciam seu tratamento emergencial na UPA e precisam de cuidados contínuos, é difícil agendar um segmento, pois muitas vezes eles precisam ir até uma UBS, e muitos sequer sabem desse fato, longe de onde foram atendidos anteriormente, e necessitam enfrentar filas longas e demoradas, sem a certeza de que realmente conseguirão ser atendidos naquele lugar, pois em casos contrários, terão de ir até outra unidade e repetir o procedimento inteiro por mais uma vez.
Com uma plataforma que integre essas duas unidades, o problema de enfrentar todo esse processo trabalhoso e que muitas vezes agrava a situação do paciente, além de convergir para outros subproblemas, como por exemplo duplo-agendamentos e ansiedade naqueles que não conseguem receber os cuidados necessários, serão resolvidos.

PRINCIPAIS FUNCIONALIDADES IMPLEMENTADAS:

01.Lista de Operações Realizadas: Armazena as operações realizadas pelo usuário em uma lista chamada operacoes_realizadas.
02. Controle de Agendamentos: Utiliza uma variável global agendamentos para controlar as informações dos agendamentos realizados.
03. Controle de Pacientes: Utiliza uma variável global pacientes para controlar as informações dos pacientes cadastrados.
04. Função para Adicionar Operação [adicionar_operacao(operacao):]: Adiciona uma operação à lista de operações realizadas.
05. Função para Identificar UPA mais Próxima [upa_proxima():]: Permite ao usuário escolher um bairro e informa a UPA mais próxima com base na escolha.
06. Função para Identificar UBS mais Próxima [ubs_proxima():]: Permite ao usuário escolher um bairro e informa a UBS mais próxima com base na escolha.
07. Função para Verificar Data Válida [data_valida(data):]: Verifica se uma data é válida.
08. Função para Cadastrar Paciente [cadastro_paciente():]: Solicita informações do paciente (nome, idade, data de nascimento, CPF) e realiza o cadastro, verificando a validade dos dados.
09. Função para Agendamento de Consulta em UBS [agendamento_consulta():]: Solicita informações para o agendamento de consulta em uma UBS, verificando a validade dos dados.
10. Função para Imprimir Agendamento em .txt [imprimir_agendamento(agendamento):]: Salva os detalhes do agendamento em um arquivo .txt.
11. Loop Principal do Programa: Oferece um menu com as seguintes opções:
    a - Identificar UPA mais próxima.
    b - Identificar UBS mais próxima.
    c - Cadastrar Paciente.
    d - Agendar consulta em UBS.
    e - Visualizar o resumo de operações realizadas.
    f - Imprimir o último agendamento de consulta realizado.
    g - Sair do programa (encerrar).

O código utiliza estruturas de repetição (while), estruturas condicionais (if, elif, else), listas, dicionários e manipulação de arquivos para implementar as funcionalidades descritas.

LINK PARA ACESSO NO GITHUB:
https://github.com/gabitrevisan/global-solution-python