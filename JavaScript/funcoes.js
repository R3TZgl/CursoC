const testeLogin = (login, senha) => {
    const msg1 = document.getElementById("superior");
    const msg2 = document.getElementById("credenciais")
    if(login == "gretzlaff13@gmail.com" && senha == "senhabraba"){
        msg1.innerHTML = "Bem Vindo";
        msg2.innerHTML = "";
        
        document.getElementById("login").style.backgroundColor = "rgb(232, 192, 255)";
        document.getElementById("senha").style.backgroundColor = "rgb(232, 192, 255)";
    }else{
        msg2.innerHTML = "Não cadastrado";
        msg1.innerHTML = "";
    }
}


const validarInput = (login, senha, inputLogin, inputSenha) => {
    
    if (!login.includes("@") || !login.includes(".") || login == ""){
        alert("Login inválido");
        inputLogin.style.backgroundColor = "red";
    }

    if (senha.length < 6){
        alert("senha inválida");
        inputSenha.style.backgroundColor = "red";
    }
}


const realizarLogin = () => {
    const inputLogin = document.getElementById("login");
    const inputSenha = document.getElementById("senha");
    const login = inputLogin.value.toLowerCase();
    const senha = inputSenha.value;

    alert(login, senha);
    
    validarInput(login, senha, inputLogin, inputSenha);

    testeLogin(login, senha);

    inputSenha.value = "";
    inputLogin.value = "";

}