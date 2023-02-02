let lugar_priorizado = document.querySelector('#lugar_priorizado')
let lugar_no_priorizado = document.querySelector('#lugar_no_priorizado')
let lugar_apoyo = document.querySelector('#lugar_apoyo')
let plan = document.querySelector('#plan')
let operativo = document.querySelector('#operativo')
let cantidad = document.querySelector('#cantidad')
let observaciones = document.querySelector('#observaciones')

let hombres_identificados = document.querySelector('#hombres_identificados')
let mujeres_identificadas = document.querySelector('#mujeres_identificadas')
let autos_identificados = document.querySelector('#autos_identificados')
let motos_identificadas = document.querySelector('#motos_identificadas')
let armas_identificadas = document.querySelector('#armas_identificadas')

let hombres_consignados = document.querySelector('#hombres_consignados')
let mujeres_consignadas = document.querySelector('#mujeres_consignadas')
let autos_consignados = document.querySelector('#autos_consignados')
let motos_consignadas = document.querySelector('#motos_consignadas')
let armas_consignadas = document.querySelector('#armas_consignadas')

let hombres_conducidos = document.querySelector('#hombres_conducidos')
let mujeres_conducidas = document.querySelector('#mujeres_conducidas')

let hombres_solventes = document.querySelector('#hombres_solventes')
let mujeres_solventes = document.querySelector('#mujeres_solventes')
let autos_solventes = document.querySelector('#autos_solventes')
let motos_solventes = document.querySelector('#motos_solventes')
let armas_solventes = document.querySelector('#armas_solventes')

let hombres_recuperados = document.querySelector('#hombres_recuperados')
let mujeres_recuperadas = document.querySelector('#mujeres_recuperadas')
let menores_recuperados = document.querySelector('#menores_recuperados')
let autos_recuperados = document.querySelector('#autos_recuperados')
let motos_recuperadas = document.querySelector('#motos_recuperadas')
let armas_recuperadas = document.querySelector('#armas_recuperadas')

var identificados=0,consignados=0,conducidos=0,solventes=0,recuperados=0
var latitud='',longitud=''

const positioned=(geolocationPosition)=>{
    let coords= geolocationPosition.coords
    latitud=coords.latitude
    longitud=coords.longitude
}

const get_position=()=>{
    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(positioned)
    }
}

get_position()


const registrar=async(jd)=>{
    const options={
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(jd),
    }
    try {
        const response = await fetch('/respuesta/api/respuestas/area_operativa/',options)
        response.json().then(data=>{
            show_message(data)
        })
    } catch (error) {
        console.log(error)
    }
}

const show_message=(data)=>{
    const ingresado=data.ingresado
    if(ingresado){
        swal.fire({
            title: 'Ingreso exitoso',
            icon:"success",
            showClass: {
              popup: 'animate__animated animate__fadeInDown'
            },
            hideClass: {
              popup: 'animate__animated animate__fadeOutUp'
            }
            
        }).then((isConfirm)=>{
                if(isConfirm){
                  location.reload()
                }
            })
    }else{
        swal.fire({
            title: 'Ha salido algo mal, vuelve a intentar.',
            icon:"error",
            showClass: {
              popup: 'animate__animated animate__fadeInDown'
            },
            hideClass: {
              popup: 'animate__animated animate__fadeOutUp'
            }
            
        })
    }
}

const validation=()=>{
    var hombres=parseInt(hombres_conducidos.value|0)+parseInt(hombres_consignados.value|0)+parseInt(hombres_recuperados.value|0)+parseInt(hombres_solventes.value|0)
    var mujeres=parseInt(mujeres_conducidas.value|0)+parseInt(mujeres_consignadas.value|0)+parseInt(mujeres_recuperadas.value|0)+parseInt(mujeres_solventes.value|0)
    var autos=parseInt(autos_consignados.value|0)+parseInt(autos_recuperados.value|0)+parseInt(autos_solventes.value|0)
    var motos=parseInt(motos_consignadas.value|0)+parseInt(motos_recuperadas.value|0)+parseInt(motos_solventes.value|0)
    var armas=parseInt(armas_consignadas.value|0)+parseInt(armas_recuperadas.value|0)+parseInt(armas_solventes.value|0)

    identificados=parseInt(hombres_identificados.value|0)+parseInt(mujeres_identificadas.value|0)+parseInt(autos_identificados.value|0)+parseInt(motos_identificadas.value|0)+parseInt(armas_identificadas.value|0)

    consignados=parseInt(hombres_consignados.value|0)+parseInt(mujeres_consignadas.value|0)+parseInt(autos_consignados.value|0)+parseInt(motos_consignadas.value|0)+parseInt(armas_consignadas.value|0)

    conducidos=parseInt(hombres_conducidos.value|0)+parseInt(mujeres_conducidas.value|0)

    solventes=parseInt(hombres_solventes.value|0)+parseInt(mujeres_solventes.value|0)+parseInt(autos_solventes.value|0)+parseInt(motos_solventes.value|0)+parseInt(armas_solventes.value|0)

    recuperados=parseInt(hombres_recuperados.value|0)+parseInt(mujeres_recuperadas.value|0)+parseInt(autos_recuperados.value|0)+parseInt(motos_recuperadas.value|0)+parseInt(armas_recuperadas.value|0)+parseInt(menores_recuperados.value|0)
    var fecha = document.getElementById('respondido').value
    jd={
        'respondido':fecha,
        'latitud':latitud,
        'longitud':longitud,
        'lugar_priorizado':parseInt(lugar_priorizado.value|0),
        'lugar_no_priorizado':lugar_no_priorizado.value.trim(),
        'lugar_apoyo':lugar_apoyo.value.trim(),
        'plan':parseInt(plan.value),
        'operativo':parseInt(operativo.value),
        'cantidad':parseInt(cantidad.value|0),
        'observaciones':observaciones.value.trim(),
        'total_identificados':identificados,
        'hombres_identificados':hombres_identificados.value|0,
        'mujeres_identificadas':mujeres_identificadas.value|0,
        'autos_identificados':autos_identificados.value|0,
        'motos_identificadas':motos_identificadas.value|0,
        'armas_identificadas':armas_identificadas.value|0,
        'total_consignados':consignados,
        'hombres_consignados':hombres_consignados.value|0,
        'mujeres_consignadas':mujeres_consignadas.value|0,
        'autos_consignados':autos_consignados.value|0,
        'motos_consignadas':motos_consignadas.value|0,
        'armas_consignadas':armas_consignadas.value|0,
        'total_conducidos':conducidos,
        'hombres_conducidos':hombres_conducidos.value|0,
        'mujeres_conducidas':mujeres_conducidas.value|0,
        'total_solventes':solventes,
        'hombres_solventes':hombres_solventes.value|0,
        'mujeres_solventes':mujeres_solventes.value|0,
        'autos_solventes':autos_solventes.value|0,
        'motos_solventes':motos_solventes.value|0,
        'armas_solventes':armas_solventes.value|0,
        'total_recuperados':recuperados,
        'autos_recuperados':autos_recuperados.value|0,
        'motos_recuperados':motos_recuperadas.value|0,
        'armas_recuperados':armas_recuperadas.value|0,
        'hombres_recuperados':hombres_recuperados.value|0,
        'mujeres_recuperadas':mujeres_recuperadas.value|0,
        'menores_recuperados':menores_recuperados.value|0
    }

    var fecha = document.getElementById('respondido').value

    if(fecha!=''){
        Swal.fire({
            title: `¿Estás seguro de guardar el registro?`,
            text: "",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#51D23A',
            cancelButtonColor: '#F61B1B',
            cancelButtonText: 'Cancelar',
            confirmButtonText: 'Confirmar'
        }).then((result) => {
            if (result.isConfirmed) {
                registrar(jd)
            }
        })
    }else{
        swal.fire({
            title: 'La fecha es incorrecta',
            icon:"warning",
            showClass: {
            popup: 'animate__animated animate__fadeInDown'
            },
            hideClass: {
            popup: 'animate__animated animate__fadeOutUp'
            }
            
        }).then((isConfirm)=>{
                if(isConfirm){
                    location.href="#inicio"
                }
            })
    }
}