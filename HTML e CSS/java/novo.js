function novo(){
    var numero = document.getElementById("input").value;
    alert(numero * 2)
}


function iniciar(){
    var numero1 = parseInt(document.getElementById("num1").value)
    var numero2 = parseInt(document.getElementById("num2").value)

    if (document.getElementById("escolha").value === "+"){
        let valor =  numero1 + numero2 
        alert(valor)
    }
    else if(document.getElementById("escolha").value === "-"){
        let valor = numero1 - numero2
        alert(valor)
    }
    else if(document.getElementById("escolha").value === 'x'){
        let valor = numero1 * numero2
        alert(valor)
    }
    else if(document.getElementById("escolha").value === "/"){
        let valor = numero1 / numero2
        alert(valor)
    }
}

for (i = 0; i < 10; i ++){
    console.log(i)
};  