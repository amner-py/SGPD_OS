let btn_noti=document.getElementById("notificaciones")
let lista_noti=document.getElementById("menu-notificacion")
let username=document.getElementById("usuario").value

console.log(username)
const get_notificaciones= () => {
    const options={
        method:'GET'
    }
    
    fetch('/notificacion/api/notificaciones',options)
        .then(response => response.json())
        .then(data =>{
                set_notificacion(data,username)
        })
}

const set_notificacion=(data,user)=>{
    const notificaciones = new Array(data.notificaciones)
    console.log(notificaciones[0])
    let no_leidos=0
    notificaciones[0].forEach(notificacion=>{
        if(notificacion.leido==false && notificacion.receptor_id==user){
            no_leidos++
        }
    })
    
    console.log(no_leidos)
    if(no_leidos>0){
        const signal=document.createElement('span')
        signal.classList="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger"
        signal.innerText=no_leidos
        btn_noti.appendChild(signal)
    }
}

get_notificaciones()
