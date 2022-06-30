let elemento_usuario = document.getElementById("usuario_Logado");

const nome_usuario = localStorage.getItem("usuarioLogado");
const sobrenome = localStorage.getItem("sobrenome");
elemento_usuario.innerText = `${nome_usuario} ${sobrenome}`;


const voltar =() => {
    window.location.assign("/projeto/index.html")
}