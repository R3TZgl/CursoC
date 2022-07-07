const vetorProduto =
[
    {
        "produto": "Pc",
        "preco": 2600,
        "descricao": "loren",
        "em_estoque": true,
        "img": "assets/imgs/img0001.jpg"
    },
    {
        "produto": "mouse",
        "preco": 26,
        "descricao": "loren",
        "em_estoque": false,
        "img": "assets/imgs/img0002.jpg" 
    },
    {
        "produto": "teclado",
        "preco": 350,
        "descricao": "loren",
        "em_estoque": true,
        "img": "assets/imgs/img0003.jpg" 
    }
];
/**
 * filter, map, reduce
 */

const produtos_em_estoque = vetorProduto.filter((element) => {
    return element.em_estoque === true;
});
console.log("filter:", produtos_em_estoque)

/**
 * map - transformar um valor em outro
 */
let statusDolar = false;
const converterDolar = (elemento) => {
    statusDolar = !statusDolar
    const newElemento = {...elemento};
    if(statusDolar){
        newElemento.preco = newElemento.preco / 10;       
    }else{
        newElemento.preco = {...elemento}.preco
    }    
    return newElemento;
}

const btnDolar = document.getElementById("dolar");

btnDolar.onclick = () => {
    const produtos_em_dolar = vetorProduto.map(converterDolar);
    exibirProdutos(produtos_em_dolar);
}




const retornaNomeProdutos = (elemento) => {
    return elemento.produto;
}

const nomesProdutos = vetorProduto.map(retornaNomeProdutos);

/**
 * reduce - fazer um cálculo com todos os elementos retornando 
 * um único valor
 */

const somaPrecos = (totalizador, elemento) => {
    return totalizador + elemento.preco;
}

const media_preco = vetorProduto.reduce(somaPrecos, 0);


/**
 * for(value of vector)
 * for(index in vector)
 */
 const divListaProdutos = document.getElementById("lista-produtos");

 const emEstoque = (element) => {
    return element.em_estoque === true;
};

const exibirProdutos = (vetor) => {
    divListaProdutos.innerText = "";
    for(let element of vetor){
        const divProduto = `<div class="produto">
        <h1>${element.produto}</h1>
        <p>${element.descricao}</p>
        <h5>${element.preco}</h5>
        </div>`;
        divListaProdutos.innerHTML += divProduto;
    }
}
exibirProdutos(vetorProduto)

let estadoBotao = false;

const btnFiltraApenasEstoque = document.getElementById("filtro01")

btnFiltraApenasEstoque.onclick = () => {
    estadoBotao = !estadoBotao;
    if(estadoBotao){
        const vetorFiltrado = vetorProduto.filter(emEstoque);
        exibirProdutos(vetorFiltrado);
        btnFiltraApenasEstoque.innerText = "Remover Filtro"
    }else{
        exibirProdutos(vetorProduto);
        btnFiltraApenasEstoque.innerText = "Filtrar por Estoque"
    }
    
    
}