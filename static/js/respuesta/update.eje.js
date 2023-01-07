let producto = document.querySelector('#producto')
let subproducto = document.querySelector('#subproducto')
let cantidad_personas = document.querySelector('#cantidad_personas')
let ninios = document.querySelector('#ninios')
let ninias = document.querySelector('#ninias')
let adolecentes_m = document.querySelector('#adolecentes_masculinos')
let adolecentes_f = document.querySelector('#adolecentes_femeninas')
let jovenes_m = document.querySelector('#jovenes_masculinos')
let jovenes_f = document.querySelector('#jovenes_femeninas')
let adultos = document.querySelector('#adultos')
let adultas = document.querySelector('#adultas')
let adultos_mayores = document.querySelector('#adultos_mayores')
let adultas_mayores = document.querySelector('#adultas_mayores')
let xincas = document.querySelector('#xincas')
let mayas = document.querySelector('#mayas')
let garifunas = document.querySelector('#garifunas')
let ladinos = document.querySelector('#ladinos')

let aviso_especifico=document.querySelector('#aviso_especifico')
let aviso_edades=document.querySelector('#aviso_edades')
let aviso_etnias=document.querySelector('#aviso_etnias')
let aviso_personas=document.querySelector('#aviso_personas')

let id_res=document.querySelector('#id-res').value

var latitud='',
    longitud=''

const positioned=(geolocationPosition)=>{
    let coords= geolocationPosition.coords
    latitud=coords.latitude
    longitud=coords.longitude
    console.log(latitud+'  '+longitud)
    
}

const get_position=()=>{
    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(positioned)
    }
}

get_position()


const list_sub=()=>{
    const options={
        method:'GET'
    }
    
    fetch(`/eje_prevencion/api/subproductos/${producto.value}`,options)
        .then(response => response.json())
        .then(data =>{
            set_subproductos(data)
        })
}

const set_subproductos=(data)=>{
    if(subproducto.firstChild){
        while(subproducto.firstChild){
            subproducto.removeChild(subproducto.firstChild)
        }
    }
    const subproductos=data.subproductos
    subproductos.forEach(sub => {
        opcion=document.createElement('option')
        opcion.value=sub.id
        opcion.innerText=sub.nombre
        subproducto.appendChild(opcion)
    })
}

list_sub()

const validate=()=>{
    var total_personas=parseInt(ninios.value|0)+parseInt(ninias.value|0)+parseInt(adolecentes_m.value)+
                        parseInt(adolecentes_f.value|0)+parseInt(jovenes_m.value|0)+parseInt(jovenes_f.value|0)+
                        parseInt(adultos.value|0)+parseInt(adultas.value|0)+parseInt(adultos_mayores.value|0)+ parseInt(adultas_mayores.value|0)
    var total_etnias=parseInt(xincas.value|0)+parseInt(garifunas.value|0)+parseInt(mayas.value|0)+parseInt(ladinos.value|0)
    var total_iguales=total_personas===total_etnias
    if(total_iguales){
        guardar(total_personas)
    }else{
        swal.fire({
            title: 'Los datos de personas y etnias no coinciden',
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

const insert_respuesta=async(detalles)=>{
    const options={
        method:'PUT',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(detalles),
    }
    try {
        const response = await fetch('/respuesta/api/respuestas/eje_prevencion/',options)
        response.json().then(data=>{
            console.log(data.ingresado)
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
                    location.href="/respuesta/respuestas/eje_prevencion/"
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
            
        }).then((isConfirm)=>{
                if(isConfirm){
                    location.href="#inicio"
                }
            })
    }
}

const guardar=(total)=>{
    let lugar_priorizado=document.querySelector('#lugar_priorizado').value
    let lugar_no_priorizado=document.querySelector('#lugar_no_priorizado').value
    let plan=document.querySelector('#plan').value
    let eje=document.querySelector('#eje').value
    let producto=document.querySelector('#producto').value
    let subproducto=document.querySelector('#subproducto').value
    let observaciones=document.querySelector('#observaciones').value
    let cantidad = document.querySelector('#cantidad')
    let especifico=lugar_especifico.value

    const jd={
        'id':parseInt(id_res),
        'latitud':latitud,
        'longitud':longitud,
        'lugar_priorizado':parseInt(lugar_priorizado|0),
        'lugar_no_priorizado':lugar_no_priorizado.trim(),
        'lugar_especifico':especifico.trim(),
        'plan':parseInt(plan),
        'eje':parseInt(eje),
        'producto':parseInt(producto),
        'subproducto':parseInt(subproducto),
        'cantidad':parseInt(cantidad.value|0),
        'observaciones':observaciones.trim(),
        'cantidad_personas':parseInt(total|0),
        'ninios':parseInt(ninios.value|0),
        'ninias':parseInt(ninias.value|0),
        'adolecentes_masculinos':parseInt(adolecentes_m.value|0),
        'adolecentes_femeninas':parseInt(adolecentes_f.value|0),
        'jovenes_masculinos':parseInt(jovenes_m.value|0),
        'jovenes_femeninas':parseInt(jovenes_f.value|0),
        'adultos':parseInt(adultos.value|0),
        'adultas':parseInt(adultas.value|0),
        'adultos_mayores':parseInt(adultos_mayores.value|0),
        'adultas_mayores':parseInt(adultas_mayores.value|0),
        'xincas':parseInt(xincas.value|0),
        'garifunas':parseInt(garifunas.value|0),
        'mayas':parseInt(mayas.value|0),
        'ladinos':parseInt(ladinos.value|0),
    }
    insert_respuesta(jd)
}

producto.addEventListener('change',list_sub)