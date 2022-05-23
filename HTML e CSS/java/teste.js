var teste = [{nome: 'Gabriel', idade: '17', cidade: 'Joinville'},
  {nome: 'Gustavo', idade: '19', cidade: 'Joinville'}];
var lista = [];

for (var elemento of teste){
  var escolha = elemento.nome
  lista.push(escolha)
  console.log(escolha);
};
