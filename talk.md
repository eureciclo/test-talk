# Talk Testes

0. introducão
    - pq ouvir o Baptista?
        - 10 anos testando tudo que coda
        - meu codigo melhorou muito
            - funcoes menores
            - desacoplamento
            - delimitacão de responsabilidades mais claras
        - pra mim teste é o melhor custo beneficio em relacão a "como melhorar sendo dev" 
    - o que vamos falar hj?
        - Testes!
        - Focado em como testar uma aplicacão backend
        - Teste unitário
        - Teste de controller (unitário/integracão)
        - Factories
        - Mocks / stubs
        - Regras de boa convivência

1. github_service - url_for
    - teste simples
        - Arrange, Act, Assert
    - **1a regra:** Teste vários casos
        - testar casos de excecao
    - **2a regra:** Valide que seu teste acusa erros
        - copiar e colar teste de cima
        - forcar falha para ter certeza que o teste esta ok

2. github_service - repositories_for
    - teste sem mock. batendo na API do github
        - depende da internet
        - perde confianca
        - demora - muito importante os testes serem rapidos
    - Mock de request
        - **3a regra:** Nunca bata na internet.
        - Mock as vezes é chamado de stub
        - cada linguagem/framework de teste tem seu jeito de fazer
        - se apeguem ao conceito, que é o mesmo em todo lugar

3. model - testes envolvendo banco
    - discussão:
        - tem gente que fala deve salvar no banco e tem gente que não
        - eu sou da opinião que banco de dados faz parte da aplicacão
        - então tem que testar salvando no banco.
            - o único ponto contra é que testes ficam um pouco mais lentos
            - mas não é muito e geralmente se paga
            - ex: lógica que fica no banco, como campos GENERATED
    - save and find_all
        - os dois juntos pq 1 depende do outro.
        - se eu executo o teste mais de uma vez, ele falha.
        - estamos testando que existe 1 obj no banco,
            - mas já tinhamos salvo 1 da primeira vez
            - **4a regra**: Testes devem rodar com o ambiente limpo, toda vez.
            - pra isso, vou habilitar uma funcão que deixei pré-escrita - MUDAR CONFTEST
    - statistics
        - precisamos criar vários GithubRepo para ter estatistica
        - mas criar tudo na mão é muito repetitivo
        - pra evitar isso, exitem as Factories ou Fixtures (similar)
        - cria a factory - FACTORIES

4. controller
    - nos testes de controller temos que fazer algumas escolhas
    - retestar funcionalidades ou garantir que chamamos uma funcao já testada
    - exemplo: metodo import
        - o metodo import chama o github_service.repositories_for que já testamos
        - podemos ou copiar o mock do request para API do github
        - ou mockar a chamada da repositories_for, passando o que esperamos de retorno
        - ATENCAO - **5a regra:** Só pode mockar o que é seu e request web.
            - Ou de uma forma mais explicita: Não pode mockar metodo de outras libs
            - Pq se a lib atualizar e mudar, seu testes não pega
    - testa http code
    - testa resposta
    - testa se o que foi importado está no banco
    - o que faltou aqui? teste da requisicão falhando - mas fica pra outra hora.


## Recapitulando

Vimos:

- Teste de modelo
- Teste de controller
- Mockar chamadas web
- Factories

e as Regras:

1. Teste vários casos.
2. Tenha certeza que seu teste acuse falhas.
3. Não bata em ninguém, nem na internet.
4. Testes devem rodar com ambiente limpo.
5. Só pode mockar código seu e request web.
