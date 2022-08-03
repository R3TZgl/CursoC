const calculadora = {
    duplicar: duplicar = (numero) => {
        return numero * 2
    },
    somar: somar = (num1, num2) => {
        return num1 + num2
    }
}

const botaoVezesDois = true;
const botaoSomar = true;
let dobro = 0;
let soma = 0;

if (botaoVezesDois){
    dobro = calculadora["duplicar"];
}
if (botaoSomar){
    soma = calculadora["somar"];
}

console.log(dobro(5));
console.log(soma(5, 3));




let array = [5, 6, 7];

const max = (array) => {
    return Math.max.apply(null, array);
}

console.log(max(array));

console.log(Math.max(...array))