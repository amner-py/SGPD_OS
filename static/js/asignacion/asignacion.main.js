
const ver_asignados= () => {
    const options={
        method:'GET'
    }
    
    fetch('/asignacion/asignaciones',options)
        .then(response => response.json())
        .then(response => console.log(response))
        .then(err => console.error(err));
}

ver_asignados()