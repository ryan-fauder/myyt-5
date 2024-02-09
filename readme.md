# Versão final

## To-Do

- [ ]  Melhoria na Manutenção
    - [ ]  Criação de um virtual environment
    - [ ]  Colocar os módulos pessoais no venv e usar em todos os componentes
- [ ]  Melhoria na performance
    - [ ]  Generator/streaming para upload e streaming do vídeo
- [ ]  Tolerância de erros
    - [ ]  Implementar session com scoped
    - [ ]  Conseguir trocar de datanode se o datanode falhar
    - [ ]  Serviço que verifica se um vídeo está disponível em poucos datanodes
- [ ]  Serviço de múltiplos clientes
- [x]  Gerar estatísticas
    - [x]  Criar o servidor de estatísticas
    - [x]  Plotar os gráficos
    - [x]  Testar o envio desses dados
    - [x]  Implementar a biblioteca de captura e envio desses dados
- [x]  Replicação entre máquinas
    - [x]  Como encontrar todas as máquinas
    - [x]  Como executar comandos em todas as máquinas via python
    - [x]  Como instalar as dependências do projeto em todas as máquinas
    - [x]  Como enviar um diretório para todas as máquinas em python
- [ ]  Testar o load balancer
- [x]  Implementar o monitor
- [x]  Serviço de nomes

## Requisitos

- Funcionais
    - Assistir um vídeo
    - Upload de um vídeo
    - Listar vídeos
    - Remover um vídeo
    - Pesquisar vídeo
    - Incluir um novo nó do sistema de armazenamento automaticamente
    - Implementar load balance para distribuição dos vídeos a serem inseridos
    - Implementar monitoramento de falhas dos nós de armazenamento
- Não Funcionais
    - Utilizar RPC para a conexão;
    - Armazenar o vídeo de forma distribuída com fator de réplica 3;

## Arquitetura

- Cliente
    - Angular app:
        
        Lida com as manipulações na DOM para disparar as requisições ao serviço Flask
        
        - VideoService: Serviço do Angular para se comunicar com serviço Flask
            - getVideoList (GET /videos): Busca a lista de vídeos;
            - uploadVideo (POST /upload): Realiza o upload do vídeo;
            - getVideo (GET /video?id): Busca metadados do vídeo;
            - streamVideo (GET /stream?id): Realiza o streaming do vídeo;
    - Flask:
        
        Lida com a comunicação entre o Angular e o Servidor;
        
        - Módulos
            1. Fetch: Móidulo de autoria própria;
            2. Communikate: Móidulo de autoria própria;
            3. Message: Móidulo de autoria própria;
            4. Flask: Para lidar com requisição
            5. Flask_cors: Para lidar com o CORS;
        - Arquitetura
            
            Dispõe dos métodos
            
            - get
            - upload
            - stream
            - list
- Server-side
    - Servidor Principal
        - Decisões de Projeto
            - Uso da biblioteca Alembic para o controle de migrations do banco de dados;
            - Implementação de módulos para o gerenciamento da comunicação via socket entre Servidor e o Flask;
            - Uso da Biblioteca
        - Arquitetura
            - Controllers:
                - datanodeController:
                    - store
                    - delete
                - ReplicationController:
                    - store
                    - index
                    - delete
                    - read
                    - readByTitle
                    - stream
            - DAOs
                - VideoInfoDAO:
                    - add
                    - get
                    - delete
                    - list
                    - getByTitle
                    - associateDatanode(video_id, datanode)
                    - datanodes(video_id)
                - DatanodeDAO:
                    - add
                    - delete
                    - get
                    - list
                    - find(host, port)
                    - qtt_videos
            - Models: Define os modelos de entidades do banco de dados
                - VideoInfoModel:
                    - id (Integer)
                    - title (String)
                    - description(String)
                    - size (Integer)
                    - created_at(String)
                - DataNode:
                    - id
                    - host
                    - port
            - Services
                - LoadBalancerService: Selecionar os datanodes capazes de lidar com as atividades do Controller;
                    - selectDataNode
                    - listDataNode
                    - findDataNode
                - ReplicationService: Realizar os serviços de replicar informação ou buscar informações;
                    - store
                    - delete
                    - stream
    - Servidor DataNode
        - Decisões de Projeto
            - Uso da biblioteca Alembic para o controle de migrations do banco de dados;
            - Implementação de módulos para o gerenciamento da comunicação via socket entre Servidor e o Flask;
        - Arquitetura
            - Controllers:
                - VideoController:
                    - store
                    - index
                    - delete
                    - read
                    - readByTitle
                    - stream
            - DAOs
                - VideoDAO:
                    - add
                    - get
                    - delete
                    - list
                    - getByTitle
            - Models: Define os modelos de entidades do banco de dados
                - VideoModel:
                    - id (Integer)
                    - title (String)
                    - description(String)
                    - blob (Binary)
                    - size (Integer)
                    - created_at(String)
    - Banco de dados SQL;
        
        Armazena os vídeos de acordo com o modelo definido no Servidor;
        
        - Decisões de projeto
            - Banco de dados SQLite para facilitar a configuração do banco de dados;

## Módulos

### Express

Módulo desenvolvido para facilitar a implementação de servidores que utilizem o módulo Communikate para a comunicação entre dois hosts;

### Classes

- Dispatcher
    
    É a classe responsável por instanciar uma porta Socket e lidar com as requisições. Deve ser instanciado com o host e porta do socket;
    
    - Função
        - Cada requisição instancia um objeto Worker para tratar a requisição;
        - Gerencia todos endpoints disponíveis no servidor. Utiliza uma instância de Router que gerencia qual o método é disparado para cada endpoint;
- Worker
    - Classe responsável por lidar com as requisições. Utiliza o módulo Communikate para receber e evniar as mensagens das requisições.
- Router
    
    É a classe responsável por mapear os endpoints para as referências dos métodos a serem disparados;
    

### Fetch

Módulo responsável por ser uma abstração do módulo Communikate para enviar e receber requisições.

O Fetch cria as mensagens de requisições e oferece os métodos semelhantes ao HTTP para lidar com as requisições.

- Métodos
    - post
    - get
    - put
    - delete

### Communikate

Módulo que abstrai toda a comunicação via socket;

### Classes

- Communication
    
    Classe envia e recebe mensagens determinadas pelo protocolo da classe Protocol;
    
    Oferece os métodos:
    
    - send
    - receive
    - send_error
- Protocol
    
    
- Config
    
    Arquivo com as variáveis de configuração. Define o tamanho máximo da mensagem; O tamanho a ser transmitido pelo Communication
    

### Message

Define as abstrações de mensagens de Request e Response;

### Classes

- Request
    - Atributos:
        - method
        - path
        - data
    - *dict(): Constrói um dicionário a partir de um objeto Request*
    - from(): Constrói um objeto Request a partir de um dicionário
- Response
    - Atributos:
        - status
        - data
    - *dict(): Constrói um dicionário a partir de um objeto Response*
    - from(): Constrói um objeto *Response* a partir de um dicionário
    

### Playkite

Módulo responsável (Facade) para a comunicação com os serviços de video disponíveis nos servidores que manipulam vídeos:

- VideoService: Serviço para lidar com os vídeos;
- DataNodeService: Serviço para registro de datanodes;

Métodos:

- store_video
- index_videos
- delete_video
- read_video
- stream_video

### Datanoodle

Módulo responsável (Facade) para a comunicação com os serviços de video disponíveis nos servidores que manipulam vídeos:

- VideoService: Serviço para lidar com os vídeos;
- DataNodeService: Serviço para registro de datanodes;

Métodos:

- register_datanode
- delete_datanode


### Statistikal

Módulo responsável (Facade) para a comunicação com os serviços de estatística disponíveis nos servidores que manipulam vídeos:

Métodos:

- register: Registrar estatística por tópico, valor e autor;
- retreive: Retorna todas as estatísticas;
- reset: Remove todas as estatísticas;