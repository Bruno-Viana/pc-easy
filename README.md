<img src="https://img.shields.io/static/v1?label=Django&message=framework&color=blue&style=for-the-badge&logo=DJANGO"/> <img src="https://img.shields.io/static/v1?label=Python&message=language&color=yellow&style=for-the-badge&logo=PYTHON"/>

### Desktop:
<div>
    <img src="https://raw.githubusercontent.com/Bruno-Viana/pc-easy/master/previews/preview1.webp" width="500px"</img>
    <img src="https://raw.githubusercontent.com/Bruno-Viana/pc-easy/master/previews/preview2.webp" width="500px"</img>
</div>



# :pushpin: PC Easy - Django e Python

@Sob licença GNU 3.0.

# :memo: O que é:
<p align="justify">Em 2020 eu precisava melhorar meu PC então ao invés de pesquisar entre Pichau/Kabum/Terabyteshop eu criei um algoritmo em Python <3.6.5 para pegar os dados de
placas de vídeos e processadores e os armazenassem em um JSON. A partir disso fui criando uma interface na web através do Django e utilizando MongoDB que depois mudei para o SQLite padrão já que
era apenas um projeto pessoa e não iria dar deploy. <br/>
A aplicação permite pesquisar produtos por nome ex: "GTX 1660 6GB" e encontrar o melhor preço dentre os modelos e redirecionar ao link do produto no site da loja.</p> 

#  :star: Features:
* Barra de pesquisa 100% funcional baseada em queries.
* Paginação quando excede o treshold de 30 itens.
* Itens fora de estoque ou indisponíveis nos sites são filtrados.
* Ordenação crescente e decrescente.
* :warning: OBS: DB local SQLite3, pode ser adaptado para MongoDB ou MySQL.
* :warning: OBS²: Não responsivo para mobile.


# :memo: Utilizando em sua máquina:
Clone o repositório:
`git clone https://github.com/Bruno-Viana/pc-easy.git`

Instale o selenium/chromewebdriver/schedule pelo pip ou conda e execute:
`cd teste`


Para iniciar o servidor web:
 `python manage.py runserver`
 
Para iniciar os crawlers assim como o refresh do DB use:
 `python Pack_starter.py` <br/>
Nota: Os updates estão programados para começaram às 6 da manhã diariamente.
 
 O Django irá iniciar [http://localhost:8000/](http://localhost:8000/)

