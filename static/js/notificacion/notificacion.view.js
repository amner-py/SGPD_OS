let contenedor_notificaciones=document.getElementById("notificaciones-contenedor")
let uname=document.getElementById("usuario").value

console.log(uname)
const view_notificaciones= async() => {
    const options={
        method:'GET'
    }
    
    const response = await fetch('/notificacion/notificacion',options)
    const data = await response.json()
    mostrar_notificacion(data,uname)
}

const mostrar_notificacion=(data,user)=>{
    const notificaciones = new Array(data.notificaciones)
    console.log(notificaciones[0])
    notificaciones[0].forEach(notificacion=>{
        if(notificacion.receptor_id==user){
            const notificacion_card=document.createElement('div')
            notificacion_card.classList="card mb-3 col-sm-12 bg-light"
            if(notificacion.leido){
                const header=document.createElement('div')
                header.classList="card-header bg-secondary text-white hstack"
                const motivo=document.createElement('div')
                motivo.innerText=notificacion.motivo
                
                header.appendChild(motivo)
                
                const leido_div=document.createElement('div')
                leido_div.classList="form-check form-switch form-check-reverse ms-auto"
                const leido_input=document.createElement('input')
                leido_input.classList="form-check-input"
                leido_input.type="checkbox"
                leido_input.setAttribute("role","switch")
                leido_input.setAttribute("id","notificacion_leido"+notificacion.id)
                leido_input.setAttribute("checked","")
                leido_input.setAttribute("value",notificacion.id)
                leido_input.setAttribute("onchange",`actualizar(notificacion_leido${notificacion.id})`)
                //leido_input.onclick=actualizar("notificacion_leido"+notificacion.id)
                
                leido_div.appendChild(leido_input)
                
                const leido_label=document.createElement('label')
                leido_label.classList="form-check-label"
                leido_label.setAttribute("for","notificacion_leido"+notificacion.id)
                leido_label.innerText="Leído"
                
                leido_div.appendChild(leido_label)
                
                header.appendChild(leido_div)

                notificacion_card.appendChild(header)
                contenedor_notificaciones.appendChild(notificacion_card)
                
                const body=document.createElement('div')
                body.classList="card-body text-dark"
                const mensaje=document.createElement('p')
                mensaje.className="card-text"
                mensaje.innerText=notificacion.mensaje
                
                body.appendChild(mensaje)

                notificacion_card.appendChild(body)
            }else{
                const header=document.createElement('div')
                header.classList="card-header bg-warning text-white hstack"
                const motivo=document.createElement('div')
                motivo.innerText=notificacion.motivo
                
                header.appendChild(motivo)
                
                const leido_div=document.createElement('div')
                leido_div.classList="form-check form-switch form-check-reverse ms-auto"
                const leido_input=document.createElement('input')
                leido_input.classList="form-check-input"
                leido_input.type="checkbox"
                leido_input.setAttribute("role","switch")
                leido_input.setAttribute("id","notificacion_leido"+notificacion.id)
                leido_input.setAttribute("value",notificacion.id)
                leido_input.setAttribute("onchange",`actualizar(notificacion_leido${notificacion.id})`)
                //leido_input.onclick=actualizar("notificacion_leido"+notificacion.id)
                
                leido_div.appendChild(leido_input)
                
                const leido_label=document.createElement('label')
                leido_label.classList="form-check-label"
                leido_label.setAttribute("for","notificacion_leido"+notificacion.id)
                leido_label.innerText="Leído"
                
                leido_div.appendChild(leido_label)
                
                header.appendChild(leido_div)

                notificacion_card.appendChild(header)
                contenedor_notificaciones.appendChild(notificacion_card)

                const body=document.createElement('div')
                body.classList="card-body text-dark"
                const mensaje=document.createElement('p')
                mensaje.className="card-text"
                mensaje.innerText=notificacion.mensaje
                
                body.appendChild(mensaje)

                notificacion_card.appendChild(body)
            }

            
        }

    })
}

const actualizar=async(id)=>{
    let leido=false
    if(id.checked){
        leido=id.checked
    }
    console.log('leido: '+leido)
    const data={
        'leido':leido
    }

    const options={
        method:'PUT',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(data)
    }
    
    const response = await fetch(`/notificacion/notificacion/${id.value}`,options)

    location.reload()
}

view_notificaciones()