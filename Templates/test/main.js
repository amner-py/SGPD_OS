const check= document.getElementById("validar_con1")
const input_check=document.getElementById("numero_check")

function getValor(){
    const valor = input_check.value
    check.value=valor
    console.log(check.value)
}