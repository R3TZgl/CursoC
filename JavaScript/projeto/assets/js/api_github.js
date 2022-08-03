let produtos = [];

const renderiza_foto = (foto) =>{
    const img_foto = document.getElementById("foto");
    img_foto.src=`${foto}`;
}

const renderiza_nome = (nome) => {
    const nick = document.getElementById()    
}

fetch('https://api.github.com/users/R3TZgl')
    .then((response => response.json()))
    .then(data => {
        console.log(data);
        renderiza_foto(data.avatar_url)
    })
    .catch( error => {  // Para status de erro
        console.error("Algo deu errado na requisição", error)}
    )

    .finally((finalizar) => {
        console.warn("sempre cai aqui")
    })
