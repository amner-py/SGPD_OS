
const ver_asignados= () => {
    const options={
        method:'GET'
    }
    
    fetch('/asignacion/api/asignaciones',options)
        .then(response => response.json())
        .catch(err => console.error(err));
}

ver_asignados()