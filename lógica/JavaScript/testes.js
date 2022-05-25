function cont(numero){
    if(numero === 1){
        return 1;
    }
    return numero + cont(numero - 1)
}   
console.log(cont(3))

