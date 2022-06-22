console.log("sim")
console.table([1,3,4])
console.warn("Será removido futuramente")
console.error("Erro")
console.exeption("")


const maiorString = (array) => {
    let maior = "";
    for (string of array){
        if (string.length > maior.length){
            maior = string;
        }
    }
    return maior;
}

const map = (string) => {
    let map = {};
    for (let i = 0; i < string.length; i ++){
        let letter = string[i];
        if (map[letter]){
            map[letter].push(i);
        }else{
            map[letter] = [i];
        }
    }
    return map;
}

const letras = (string,map) => {
    for (letter of string){
        if (map[letter]){
        }else{
            return false;
        }
    }
}

const proxIndice = (letterMap, minIndice) => {
    for (indice of letterMap){
        if (indice >= minIndice){
            return minIndice + 1;
        }
    }
    return false;
}

const sequencia = (string,map) => {
    let minIndice = 0;
    for (letter of string){
        if (map[letter]){
            minIndice = proxIndice(map[letter],minIndice);
            if (minIndice === false){
                return false;
            }
        }else{
            return false;
        }
    }
    return false;
}

const maiorSequencia = (string,dicionario) => {
    let mapa = map(string);
    let lista = [];
    for (elemento of dicionario){
        if (sequencia(elemento,mapa)){
            lista.push(elemento);
        }
    }
    return maiorString(lista);
}
