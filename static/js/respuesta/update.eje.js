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
    const cantidad_etnias=(total_etnias==parseInt(cantidad_personas.value|0))
    const cantidad_edades=(total_personas==parseInt(cantidad_personas.value|0))
    const personas_mayor_cero=(parseInt(cantidad_personas.value|0))>0

    var edades_confirm=false,etnias_confirm=false

    if(!personas_mayor_cero){
        aviso_personas.removeAttribute('hidden')
    }else{
        aviso_personas.setAttribute('hidden',true)
    }
    if(!cantidad_edades){
        aviso_edades.removeAttribute('hidden')
    }else{
        aviso_edades.setAttribute('hidden',true)
        edades_confirm=true
    }
    if(!cantidad_etnias){
        aviso_etnias.removeAttribute('hidden')
    }else{
        aviso_etnias.setAttribute('hidden',true)
        etnias_confirm=true
    }

    const especifico_campo=lugar_especifico.value
    const especifico=(especifico_campo.trim().length==0)
    var especifico_confirm
    if(especifico){
        aviso_especifico.removeAttribute('hidden')
    }else{
        aviso_especifico.setAttribute('hidden',true)
        especifico_confirm=true
    }


    if(edades_confirm && edades_confirm && etnias_confirm && especifico_confirm && personas_mayor_cero){
        guardar()
    }else{
        location.href="#inicio"
        window.navigator.vibrate([1000]);
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

const guardar=()=>{
    let lugar_asignado=document.querySelector('#lugar_asignado').value
    let plan=document.querySelector('#plan').value
    let eje=document.querySelector('#eje').value
    let producto=document.querySelector('#producto').value
    let subproducto=document.querySelector('#subproducto').value
    let observaciones=document.querySelector('#observaciones').value
    let personas=cantidad_personas.value
    let especifico=lugar_especifico.value

    const jd={
        'id':parseInt(id_res),
        'latitud':latitud,
        'longitud':longitud,
        'lugar_asignado':parseInt(lugar_asignado),
        'lugar_especifico':especifico.trim(),
        'plan':parseInt(plan),
        'eje':parseInt(eje),
        'producto':parseInt(producto),
        'subproducto':parseInt(subproducto),
        'observaciones':observaciones.trim(),
        'cantidad_personas':parseInt(personas),
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