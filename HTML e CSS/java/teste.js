var teste = [{nome: 'Gabriel', idade: '17', cidade: 'Joinville'},
  {nome: 'Gustavo', idade: '19', cidade: 'Joinville'}];
var lista = [];

for (var elemento of teste){
  var escolha = elemento.nome
  lista.push(escolha)
  console.log(escolha);
};

function soma(numero1, numero2){
    return numero1 + numero2
}
console.log(soma(1,4))

for (i = 0; i <= 10; i ++){
    console.log(i)
};

var total = 0
while (true){
    console.log(1)
    total ++
    if (total === 3){
        break
    }
}

function somaTot(num){
    if (num === 1){
        return 1
    }
    return num + somaTot(num - 1)
}
somaTot(3)