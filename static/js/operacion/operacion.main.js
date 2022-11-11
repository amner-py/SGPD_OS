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
        operaciones[0].forEach(operacion=>{
            item=document.createElement('li')
            enlace=document.createElement('a')
            enlace.className="dropdown-item"
            enlace.href="/formulario/formularios/"+operacion.id
            enlace.innerText=operacion.nombre
            item.appendChild(enlace)
            menu.appendChild(item)
            contenedor_operaciones.appendChild(menu)
        })
    }
}

get_operaciones()