const formulario=document.getElementById('formulario-res').value
const usname=document.getElementById('usuario').value
const respuesta_id=document.getElementById('respuestas-size').value

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

const insert_respuesta=async(detalles)=>{
    const jdr={
        'latitud':latitud,
        'longitud':longitud,
        'delegacion':parseInt(usname),
        'formulario':parseInt(formulario),
        'respuestas':detalles
    }
    // debugger
    console.log('PRIMERO')
    const options={
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(jdr),
    }
    
    const response = await fetch('/respuesta/api/respuestas/',options)
    return 'SEGUNDO'
    
}

const get_preguntas=() => {
    const options={
        method:'GET'
    }
    
    fetch(`/formulario/api/preguntas/${formulario}`,options)
        .then(response => response.json())
        .then(data =>{
            console.log(data)
            set_respuesta(data)
        })
}

const set_respuesta=async(data)=>{
    var detalles=[]
    const preguntas = new Array(data.preguntas)
    console.log(preguntas[0])
    if(data.hay_pregunta){
        preguntas[0].forEach(pregunta=>{
            const respuestas_ch=document.getElementsByName(`ch${pregunta.id}`)
            const respuesta_n=document.getElementById(`${pregunta.id}`)
            
            var valor=''
            var res_size=0
            var index=1
            respuestas_ch.forEach(respuesta=>{
                if(respuesta.checked){
                    res_size++
                }
            })
            respuestas_ch.forEach(respuesta=>{
                if(respuesta.checked){
                    valor+=respuesta.value
                    if(index<res_size){
                    valor+=','
                    res_size--
                    }
                }
                console.log(valor)
            })
            if(respuesta_n!=null){
                //console.log(respuesta)
                valor=respuesta_n.value
                console.log(respuesta_n.value)
            }
            console.log(respuesta_id)
            const jd={
                'detalle':valor,
                'respuesta':parseInt(respuesta_id),
                'pregunta':parseInt(pregunta.id)
            }
            detalles.push(jd)
            console.log(detalles)
        })
    }
    insert_respuesta(detalles)
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
}

