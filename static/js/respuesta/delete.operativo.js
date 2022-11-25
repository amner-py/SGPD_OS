const confirm_eliminar=(id)=>{
    Swal.fire({
        title: `¿Estás seguro de eliminar el registro número ${parseInt(id)}?`,
        text: "No se prodra recuperar una vez eliminado",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#51D23A',
        cancelButtonColor: '#F61B1B',
        cancelButtonText: 'Cancelar',
        confirmButtonText: 'Confirmar'
      }).then((result) => {
        if (result.isConfirmed) {
            eliminar(id)
        }
      })
}

const eliminar=async(id)=>{
    const jd={
        'id':parseInt(id)
    }
    const options={
        method:'DELETE',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(jd),
    }
    try {
        const response = await fetch('/respuesta/api/respuestas/area_operativa/',options)
        response.json().then(data=>{
            console.log(data.eliminado)
            show_message(data)
        })
    } catch (error) {
        console.log(error)
    }
}

const show_message=(data)=>{
    const eliminado=data.eliminado
    if(eliminado){
        swal.fire({
            title: 'Eliminado exitosamente',
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
                }
            })
    }
}