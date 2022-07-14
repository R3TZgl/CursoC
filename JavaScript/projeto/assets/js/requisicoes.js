let produtos = [];
fetch('../json/hobbyes.json')
    .then((response => response.json()))
    .then(data => {
        produtos = data;
        exibirProdutos(produtos);
        console.log(data);
    })
    .catch( error => {  // Para status de erro
        console.error("Algo deu errado na requisição", error)}
    )

    .finally((finalizar) => {
        console.warn("sempre cai aqui")
    })

