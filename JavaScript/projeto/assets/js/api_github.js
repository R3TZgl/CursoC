const headers = new Headers();
headers.append("Authorization", "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");



const renderiza_foto = (foto) =>{
    const img_foto = document.getElementById("foto");
    img_foto.src=`${foto}`;
}

const renderiza_nome = (nome) => {
    const nick = document.getElementById("nome");
    nick.innerText = `${nome}`;    
}

const renderiza_link = (html_url) => {
    const link = document.getElementById("linkGitHub");
    link.href=`${html_url}`;
}

const upar_bio = (dataBio) => {
    const bio = document.getElementById("bio");
    bio.innerText = `${dataBio}`;
}

const upar_repositorio = (data) => {
    const repositorio = document.getElementById("repo");
    repositorio.innerHTML += `<a href="${data.html_url}" target="_blank">${data.name}</a><br><br>`;
}


fetch('https://api.github.com/users/R3TZgl', {headers: headers})
    .then((response => response.json()))
    .then(data => {
        console.log(data);
        renderiza_foto(data.avatar_url)
        renderiza_nome(data.name)
        renderiza_link(data.html_url)
        upar_bio(data.bio)
    })
    .catch( error => {  // Para status de erro
        console.error("Algo deu errado na requisição", error)}
    )

    .finally((finalizar) => {
        console.warn("sempre cai aqui")
    })


fetch("https://api.github.com/users/R3TZgl/repos", {headers: headers})
    .then((response => response.json()))
    .then(data => {
        console.log(data);
        data.forEach(upar_repositorio)
        
    })
    .catch( error => {  // Para status de erro
        console.error("Algo deu errado na requisição", error)}
    )

    .finally((finalizar) => {
        console.warn("sempre cai aqui")
    })