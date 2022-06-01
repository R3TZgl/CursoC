var dados = {};
var info = ["Nome", "Endereço", "Cidade", "UF", "CEP", "Telefone", "CEP",
            "RG", "Data de Nascimento", "Grau de Escolaridade", "Curso"];

for(c of info){ 
    while (true){
        dados.c = prompt(c + ":")
        if (dados.c != ""){
            break
        }
        else{
            alert("Erro, insira os dados corretamente.")
        };
    };
};
for (c of info){
    alert(c + ": " + dados.c)
};


var objeto = {cachorro: ["pinscher", "bulldog"]}
console.log(objeto.cachorro[1])