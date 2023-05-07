let btn_noti=document.getElementById("notificaciones")
let lista_noti=document.getElementById("menu-notificacion")
let bday=document.getElementById('fnacimiento').value
let bday_container=document.getElementById('bday')
const fecha = new Date();

const fecha_actual=`${fecha.getFullYear()}-0${fecha.getMonth()+1}-${fecha.getDate()}`
const fecha_actual_f=`${fecha.getDate()}-${fecha.getMonth()+1}-${fecha.getFullYear()}`

const get_meta=()=>{
    
    const options={
        method:'GET'
    }
    
    fetch('/asignacion/notificar/metas_eje/',options)
        .then(response => response.json())
        .then(data =>{
            set_meta(data)
        })
}

const set_meta=(data)=>{
    const mensaje_meta=`<span onclick="get_bday_msn(${data})">&#127874;</span>`
    btn_meta = document.querySelector("#meta")
    btn_meta.innerHTML=mensaje_bday
}

const get_meta_msn=(data)=>{
swal.fire({
    title: 'SU META',
    html:`META`,
    showClass: {
      popup: 'animate__animated animate__fadeInDown'
    },
    hideClass: {
      popup: 'animate__animated animate__fadeOutUp'
    }
  })
}

get_meta()

const get_bday=()=>{
    if(bday==fecha_actual){
        const mensaje_bday='<span onclick="get_bday_msn()">&#127874;</span>'
        bday_container.innerHTML=mensaje_bday
    }
}


const get_bday_msn=()=>{
    const nombre=document.getElementById('name_person').value
    swal.fire({
        title: '¡FELIZ CUMPLEAÑOS!',
        html:`${nombre}<br><span>&#127881;</span>El día de hoy ${fecha_actual_f}<br>¡Te deseamos felicidades!<span>&#127881;</span><br><span>&#127874;</span><span>&#129395;</span><span>&#128110;</span>`,
        showClass: {
          popup: 'animate__animated animate__fadeInDown'
        },
        hideClass: {
          popup: 'animate__animated animate__fadeOutUp'
        }
      })
}

get_bday()

const get_notificaciones= () => {
    const options={
        method:'GET'
    }
    
    fetch('/notificacion/api/notificaciones',options)
        .then(response => response.json())
        .then(data =>{
            set_notificacion(data)
        })
}

const set_notificacion=(data)=>{
    const no_leidos = parseInt(data.no_leidos)
    
    if(no_leidos>0){
        const signal=document.createElement('span')
        signal.classList="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger"
        signal.innerText=no_leidos
        btn_noti.appendChild(signal)
    }
}

get_notificaciones()
