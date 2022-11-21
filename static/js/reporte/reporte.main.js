const ctx = document.getElementById('myChart');



const get_reporte=()=>{
    
    const options={
        method:'GET'
    }
    fetch('/respuesta/api/detalles/',options)
        .then(response => response.json())
        .then(data =>{
            set_reporte(data)
        })
}

const set_reporte = (data) => {
    const respuestas = new Array(data.detalles)
    const detalles=[]
    console.log(respuestas)
    respuestas[0].forEach(respuesta => {
        if(respuesta.pregunta_id==19)
        detalles.push(respuesta.detalle)
    })
    console.log(detalles)
    const detalles_n = detalles.reduce((det,item)=>{
        if(!det.includes(item)){
            det.push(item)
        }
        return det
    },[])
    console.log(detalles_n)
    //grafica.data['labels']=detalles_n
    //console.log(grafica.data['labels'])
    var cantidades = []
    detalles_n.forEach(det => {
        var cantidad = 0
        respuestas[0].forEach(re => {
            console.log(det)
            if(re.detalle==det)
            cantidad+=1
        })
        cantidades.push(cantidad)
    })
    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: detalles_n,
            datasets: [{
                label: ['TOTAL'],
                data: cantidades,
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                beginAtZero: true
                }
            },
            plugins: {
                legend: true,
                tooltip: true,
            },
        }
    });
}
get_reporte()