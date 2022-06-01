function cont(numero){
    if(numero === 1){
        return 1;
    }
    return numero + cont(numero - 1)
}   
console.log(cont(3));



var listaA = []
var listaC = []

for (i = 0;i < 2; i++){
    listaA = []
    for (b = 0;b < 2; b++){
        listaA.push(parseInt(prompt("Digite um número: ")))
        listaC.push(listaA[b])
    }
}
console.log(listaC)