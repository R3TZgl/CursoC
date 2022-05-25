var dados = {};
var info = ["Nome", "Endereço", "Cidade", "UF", "CEP", "Telefone", "CEP",
            "RG", "Data de Nascimento", "Grau de Escolaridade", "Curso"];

for (c of info){
    if (c === info[4] || c === info[5] || c === info[6] || c === info[7] || c === info[8]){
      dados.c = parseInt(prompt(c + ":"))  
    }
    else{
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
};
for (c of info){
    alert(c + ": " + dados.c)
};