# Blockchain

#### Uma blockchain é uma tecnologia de registro distribuído que permite a criação de um banco de dados seguro e transparente, onde as informações são armazenadas em blocos encadeados de forma cronológica. Cada bloco contém um conjunto de transações ou dados, um timestamp (marca temporal) e um hash que conecta o bloco ao anterior, formando uma cadeia. Essa estrutura garante que, uma vez que um bloco é adicionado à cadeia, ele não pode ser alterado sem modificar todos os blocos subsequentes, o que torna a blockchain altamente resistente a fraudes e manipulações.


## Como Funciona uma Blockchain?

- ####  Criação de Blocos: Quando uma nova transação ocorre, ela é agrupada com outras transações em um bloco. Cada bloco contém informações como o hash do bloco anterior, um timestamp e os dados da transação.

 - ####  Validação: Antes de um bloco ser adicionado à blockchain, ele precisa ser validado. Isso geralmente é feito por meio de um processo de consenso, onde os nós da rede (computadores que participam da blockchain) concordam que a transação é válida. Existem diferentes métodos de consenso, como Proof of Work (PoW) e Proof of Stake (PoS).

 - ####   Adição à Cadeia: Uma vez validado, o novo bloco é adicionado à cadeia existente. O hash do bloco anterior é incluído no novo bloco, criando uma ligação entre eles. Isso garante a integridade da cadeia, pois qualquer alteração em um bloco exigiria a alteração de todos os blocos subsequentes.

 - #### Distribuição: A blockchain é mantida por uma rede de nós que possuem uma cópia completa do registro. Quando um novo bloco é adicionado, essa informação é distribuída para todos os nós da rede, garantindo que todos tenham a mesma versão da blockchain.

 - #### Segurança e Transparência: A natureza descentralizada da blockchain, combinada com a criptografia, torna as transações seguras e transparentes. Todos os participantes da rede podem verificar as transações, mas não podem alterá-las sem o consenso da maioria.

- ***Em resumo, a blockchain é uma tecnologia inovadora que permite o registro seguro e transparente de informações, sendo a base para diversas aplicações, como criptomoedas, contratos inteligentes e sistemas de rastreamento de produtos.***

## Como Funciona no código

- #### Classe Block: Define a estrutura de um bloco, que contém um índice, o hash do bloco anterior, um timestamp, os dados do bloco e o hash do próprio bloco.

- #### Função calculate_hash: Calcula o hash de um bloco com base em seu índice, hash anterior, timestamp e dados. Utiliza o algoritmo SHA-256.

 - #### Função create_genesis_block: Cria o bloco gênesis (o primeiro bloco da blockchain).

 - #### Função create_new_block: Cria um novo bloco com base no bloco anterior e nos dados fornecidos.

 - #### Inicialização da Blockchain: A blockchain é inicializada com o bloco gênesis.

 - #### Adição de Novos Blocos: Um loop adiciona novos blocos à blockchain, gerando dados fictícios para cada bloco.

 - #### Exibição da Blockchain: Após a adição dos blocos, a blockchain é exibida no console.
