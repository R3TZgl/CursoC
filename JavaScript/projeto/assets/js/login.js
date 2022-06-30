let elementoLogin = document.getElementById("login");
let elementoSobrenome = document.getElementById("sobrenome")
let elementoSenha = document.getElementById("senha");


const vereficar = (login, senha) => {
    if(login == "maria" && senha == "123"){
        localStorage.setItem("usuarioLogado", "Maria");
        localStorage.setItem("sobrenome", `${elementoSobrenome.value}`)
        return true;
    }
    return false;
};


const msgErro = () => {
    alert("Não foi possível logar")
};


const realizar = () => {
    const login = elementoLogin.value;
    const senha = elementoSenha.value;
    if(vereficar(login, senha)){
        window.location.assign("./views/home.html")
    }else{
        msgErro()
    }
};


const fazerLogin = () =>{
    alert("clicou");
};