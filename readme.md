SSSumo
S3 - Lambda - Sumológico

Cerca de
Este repo contém o código AWS Lambda que observa um bucket do S3 para novos objetos de entrada. Em seguida, executa o código para enviar esses novos objetos para o SumoLogic.

Configuração do AWS Lambda
A função Lambda usada neste exemplo precisa ter uma configuração de gatilho para procurar objetos recém-criados para um determinado intervalo s3 e prefixo. Assim que novos objetos forem descartados, um gatilho disparará um evento na função Lambda e o código será executado. Sua função Lambda precisará ter o privilégio correto para o balde s3. Neste caso, as permissões de leitura são suficientes.

SumoLogic
Para permitir que os objetos sejam colocados no Sumologic, um coletor http precisa ser configurado na plataforma. Depois que esse coletor estiver configurado, você receberá uma URL secreta que pode ser usada para postar seus objetos. Veja a documentação Sumologic aqui

Implantação AWS
Este código depende do pacote de solicitações para postar dados na Sumologic. Este pacote não pertence à biblioteca python padrão nem à biblioteca AWS (como o boto3 faz). Para capturar essa dependência, o código-fonte das solicitações é colocado na pasta do projeto e compactado junto com o código-fonte. Quando implantada na AWS, a biblioteca ficará em seu caminho Python e pode ser usada normalmente. NOTA: Quaisquer dependências de biblioteca devem ser colocadas no nível superior da página inicial do seu projeto. Documentação da AWS aqui