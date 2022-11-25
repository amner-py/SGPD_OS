let contenedor_operaciones=document.getElementById('lista_operaciones')

const get_operaciones=() => {
    const options={
        method:'GET'
    }
    
    fetch('/operacion/api/operaciones',options)
        .then(response => response.json())
        .then(data =>{
            console.log(data)
            set_operaciones(data)
        })
}

const set_operaciones=(data)=>{
    const operaciones = new Array(data.operaciones)
    console.log(operaciones[0])
    if(data.hay_operacion){
        const menu=document.createElement('ul')
        menu.classList="dropdown-menu dropdown-menu-dark"
        eje=document.createElement('li')
        enlace_eje=document.createElement('a')
        enlace_eje.className="dropdown-item"
        enlace_eje.href="/respuesta/respuestas/eje_prevencion/"
        enlace_eje.innerText="Eje de Prevención"
        eje.appendChild(enlace_eje)
        menu.appendChild(eje)

        operativa=document.createElement('li')
        enlace_operativa=document.createElement('a')
        enlace_operativa.className="dropdown-item"
        enlace_operativa.href="/respuesta/respuestas/area_operativa/"
        enlace_operativa.innerText="Área Operativa"
        operativa.appendChild(enlace_operativa)
        menu.appendChild(operativa)
        contenedor_operaciones.appendChild(menu)
        
    }
}

get_operaciones()