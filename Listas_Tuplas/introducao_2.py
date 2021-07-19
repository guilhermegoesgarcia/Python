#contador de letras
from collections import Counter

texto1 = ''' Nesse artigo, vamos entender como funcionam os conceitos de Box Model e Box Sizing do CSS.

Você já se deparou com algum site ou aplicação web onde os elementos parecem estar desalinhados, com tamanho desproporcional, componentes que não seguem um padrão, ou até o clássico problema da responsividade, de quando abrimos um mesmo site em diferentes dispositivos (smartphone, tablet) e o layout aparece todo desordenado?

Nesse artigo, explicarei um dos motivos desse erro acontecer e como fazemos para resolvê-lo.Em seguida, com o CSS, adicionamos a fonte que será utilizada, as cores dos elementos e definimos uma largura e altura para a nossa tag div, a fim de facilitar sua visualização.
É notável que, apesar da aplicação de alguns estilos, o resultado ainda está longe do que foi proposto no layout. A distância entre a nossa caixa (margem) e a tela é muito pequena. O texto está colado na lateral da caixa e isso é um problema.

Devemos lembrar, que mesmo não declarando a propriedade margem no CSS, o próprio navegador adiciona valores para a margem padrão aos elementos na tela. Veja isso na prática: abra o DevTools do Google Chrome (pode ser pelo atalho ctrl + shift + I ou clique com o botão direito do mouse e escolha a opção inspecionar) e confira a tag h1:
 Como foi destacado no canto inferior direito da imagem anterior, temos a frase sublinhada: user agent stylesheet e, logo abaixo, algumas propriedades.

Como mencionado anteriormente, estas são as propriedades padrão que o navegador aplica na tag h1. Lembrando que cada tag tem seu próprio estilo padrão, ou seja, se eu escolhesse a tag p veríamos certamente diferentes propriedades e valores sendo utilizados.

A propriedade Margin do Box Model
Para darmos início ao ajuste do nosso layout, começamos adicionando a propriedade **margin** à nossa tag div, pois ela é o nosso elemento primário e as tags h1 e p que estão dentro dela são as secundárias. A propriedade margin é o espaçamento externo do elemento (distância entre o elemento e o canto da tela, ou se tivermos mais elementos na tela, poderíamos dizer também que é a distância entre um elemento e outro). Ela aceita valores absolutos (px, cm, mm...) ou valores relativos (rem, vh, vw, %...). Ao utilizar a propriedade margin, temos 4 valores: margin-top é a distância entre o elemento e o canto superior da tela; margin-right, distância entre o elemento e o canto direito da tela; margin-bottom, distância entre o elemento e o canto inferior da tela, e margin-left, distância entre o elemento e o canto esquerdo da tela.

Se declararmos somente a propriedade margin, estaremos usando um shorthand, ou seja, uma propriedade abreviada, que nos permite escrever menos código.
'''


texto2 = ''' Com o advento da internet, o volume de dados gerados ao redor do mundo cresceu de forma inesperada conforme os anos foram se passando. A utilização em larga escala de dispositivos móveis ampliou ainda mais a quantidade de dados gerados diariamente.

Os métodos tradicionais para armazenamento e processamento de dados em grandes empresas começaram a não ser suficientes, gerando problemas e gastos cada vez maiores para suprir suas necessidades.

Devido a esses acontecimentos, surgiu o conceito de Big Data, uma área do conhecimento que tem como intuito estudar maneiras de tratar, analisar e gerar conhecimento através de grandes conjuntos de dados que não conseguem ser trabalhados em sistemas tradicionais.

Para entender melhor esse conceito, podemos pensar na forma como esse sistema tradicional de armazenamento e processamento de dados é realizado. Perceba que é colocado aqui no presente como “é realizado”, porque os processos de trabalho com o Big Data não excluem a forma de trabalhar no sistema tradicional em grande parte dos casos, uma vez que muitas empresas não necessitam da utilização de ferramentas do Big Data para manipular os dados, e mesmo as grandes empresas utilizam um sistema híbrido. Dessa forma, as duas maneiras de trabalhar com os dados coexistem.

O sistema tradicional utiliza os famosos SGBDs, ou sistemas gerenciais de banco de dados, que guardam informações de forma estruturada, no formato de tabelas, com linhas e colunas. Utilizam máquinas com grande capacidade de armazenamento e processamento. Quando há a necessidade de expandir a capacidade dessas máquinas, é necessário introduzir novos componentes de hardware, para que tenham mais memória e processamento.

Os problemas que começam a aparecer quando se alcança um grande volume de dados usando esse sistema tradicional são relacionados à escalabilidade, disponibilidade e flexibilidade. Como exemplos, podemos mencionar que é muito custoso o aprimoramento dessas máquinas de maneira vertical a cada vez que é necessário realizar um upgrade, corriqueiramente nesse momento o sistema fica indisponível, já que a máquina está em processo de manutenção.

De forma a compreender a definição de Big Data, é necessário introduzir os conceitos dos V’s do Big Data. Inicialmente, a definição era composta por 3 V’s, mas hoje podemos encontrar definições expandidas com 5, 7 ou mais V’s. Os 7 V’s são: volume, variedade, velocidade, valor, veracidade, variabilidade e visualização.

Mas, vamos concentrar aqui nos principais dentre os 7 mencionados anteriormente:
 Volume
O volume é a principal característica quando pensamos a respeito de Big Data. Ele diz respeito a uma grande quantidade de dados para ser armazenada e processada, na casa de terabytes, petabytes ou mesmo zettabytes.

Há afirmações de que a quantidade de dados dobra a cada dois anos e a quantidade de dados gerada por dia e acumulada ao longo dos anos é tão grande que não seria interessante a colocação de valores aqui, uma vez que no momento em que você estiver lendo esse artigo esses valores já terão se alterado.

Na Internet live stats, é possível ter uma ideia da quantidade de dados gerados diariamente e a rapidez com que esses números estão crescendo a cada segundo. Alguns dados impactam bastante por se tratarem de valores em um intervalo de apenas 24 horas.

Já nesse vídeo denominado “Size of internet: bytes perspective”, são comparados os dados com uma escala física, mostrando a diferença entre a quantidade de dados existente na internet em 2001 e 2020.

Variedade
Outra característica importante no Big Data é a variedade dos dados que são armazenados e processados. Além dos famosos dados estruturados, o conceito de Big Data trabalha com dados semi-estruturados e não estruturados.

Os dados estruturados são os dados com estrutura rígida em formato tabular, com linhas e colunas.

Os dados semi-estruturados possuem certo tipo de estrutura, mas são mais flexíveis, os arquivos do tipo XML e JSON são exemplos de dados semi-estruturados.

Já os dados não estruturados são dados sem nenhuma estrutura pré-definida, correspondendo à maior parcela dos dados circulantes no mundo atualmente, em uma proporção bem maior do que os outros tipos de dados. Arquivos de texto, de áudio, vídeo e imagens são exemplos de dados não estruturados.

Velocidade
A velocidade se refere a rapidez com que os dados são gerados. A todo instante e-mails, mensagens de texto e áudio são enviados, tweets são publicados, registros em bancos de dados são inseridos e atualizados. Tudo isso em uma escala global.

Não podemos nos esquecer dos dados gerados por máquinas, através de sensores a cada instante de tempo e de serviços de streaming que enviam e recebem dados em uma velocidade surpreendente.

A solução encontrada
Para que fosse possível resolver os problemas que surgiram, foi necessário criar novas ferramentas para suprir todas as necessidades. A escalabilidade vertical, no qual aprimoramos uma máquina adicionando mais recursos como memória e processamento, não garante uma efetividade quando se trata de Big Data.

Para contornar os problemas, grandes empresas pesquisaram um novo sistema que fosse escalável, surgindo então o Hadoop, uma forma de armazenamento e processamento distribuído. A ideia é utilizar cluster de máquinas ou agrupamento de computadores. De forma isolada, um único computador nesse cluster não tem um poder de processamento muito poderoso, mas, em conjunto, conseguem fornecer poder de processamento e armazenamento capazes de suprir as necessidades.

Nesse cluster, existe uma máquina principal conhecida como Name Node que é responsável por gerenciar o restante das outras máquinas, conhecidas como Data Nodes. Os dados possuem réplicas em Data Nodes diferentes para que, caso uma máquina venha a falhar, os dados não serão perdidos e estarão sempre disponíveis. Esse conceito é conhecido em Big Data como disponibilidade.

O mais interessante é que no momento em que necessite ampliar as capacidades, novas máquinas podem ser integradas ao cluster, crescendo de maneira indefinida. Essa é a escalabilidade horizontal, a solução encontrada para os problemas de Big Data.
A partir do surgimento do Hadoop, diversas outras tecnologias foram sendo desenvolvidas em paralelo, criando assim um ecossistema de ferramentas que se expande a cada dia. Dando destaque para a utilização de bancos de dados NoSQL para trabalhar com dados não estruturados.'''

cont_1 = Counter(texto1.lower())
print(cont_1)

def analisando_freq_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia/total_de_caracteres) for letra,frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere,proporcoes in mais_comuns:
        print('{} => {:.2f}%'.format(caractere,proporcoes*100))

analisando_freq_de_letras(texto1)