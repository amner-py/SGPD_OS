let reportes=document.getElementById('reportes')
let filtro=document.getElementById('filtro')
let btn_filtro=document.getElementById('btn-filtro')
var data=[]
const get_metas=() => {
    const options={
        method:'GET'
    }
    
    fetch('/asignacion/api/metas_operativa/',options)
        .then(response => response.json())
        .then(data =>{
            set_metas(data)
        })
}

const set_metas=(data) => {
    this.data=data
    const delegaciones = data.delegaciones
    let temp=[]
    let anios=[]
    let anios_tmp=[]
    delegaciones.forEach(delegacion => {
        var m=delegacion.metas
        
        m.forEach(meta =>{
            anios_tmp.push(meta.anio)
        })
        temp = new Set(anios_tmp)
        anios = [...temp]
        
    })
    console.log(anios)
    anios.forEach(anio=>{
        const opciones_filtro=document.createElement('option')
        opciones_filtro.value=anio
        opciones_filtro.innerText=anio
        filtro.appendChild(opciones_filtro)
    })
}

const grafica=(id_delegacion,nombre_delegacion,anio,metas,alcanzadas)=>{
    Highcharts.chart(`contenedor${id_delegacion}`, {
        chart: {
            type: 'column'
        },
        title: {
            text: `METAS PARA AREA OPERATIVA DE ${nombre_delegacion.toUpperCase()}`
        },
        subtitle: {
            text: ''
        },
        xAxis: {
            categories: [
                'ENE',
                'FEB',
                'MAR',
                'ABR',
                'MAY',
                'JUN',
                'JUL',
                'AGO',
                'SEP',
                'OCT',
                'NOV',
                'DIC'
            ],
            crosshair: true
        },
        yAxis: {
            title: {
                useHTML: true,
                text: `METAS PARA AREA OPERATIVA DEL AÑO ${anio}`
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                '<td style="padding:0"><b>{point.y:.1f}</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            }
        },
        series: [{
            name: 'Meta asignada',
            data: metas
    
        }, {
            name: 'Meta alcanzada',
            data: alcanzadas
    
        }]
    })
}

const grafica2=(id_delegacion,nombre_delegacion,anio,metas,alcanzadas)=>{
    Highcharts.chart(`contenedor${id_delegacion}`, {
        chart: {
          type: 'column'
        },
        title: {
          text: `METAS PARA EJE DE PREVENCION DE ${nombre_delegacion.toUpperCase()}`
        },
        xAxis: {
            categories: [
                'ENE',
                'FEB',
                'MAR',
                'ABR',
                'MAY',
                'JUN',
                'JUL',
                'AGO',
                'SEP',
                'OCT',
                'NOV',
                'DIC'
            ],
        },
        yAxis: [{
          min: 0,
          title: {
            text: `METAS PARA EJE DE PREVENCION DEL AÑO ${anio}`
          }
        }, {
          title: {
            text: `METAS PARA EJE DE PREVENCION DEL AÑO ${anio}`
          },
          opposite: true
        }],
        legend: {
          shadow: false
        },
        tooltip: {
          shared: true
        },
        plotOptions: {
          column: {
            grouping: false,
            shadow: false,
            borderWidth: 0
          }
        },
        series: [{
          name: 'Meta Asignada',
          color: 'rgba(165,170,217,1)',
          data: metas,
          pointPadding: 0.3,
          pointPlacement: -0.2
        }, {
          name: 'Meta Alcanzada',
          color: 'rgba(126,86,134,.9)',
          data: alcanzadas,
          pointPadding: 0.4,
          pointPlacement: -0.2
        }]
      });
}
const buscar=()=>{
    const filtro_anio=filtro.value
    if(filtro_anio>0){
        const consulta=this.data.hay_metas
        if(consulta){
            let metas=[0,0,0,0,0,0,0,0,0,0,0,0]
            let alcanzadas=[0,0,0,0,0,0,0,0,0,0,0,0]
            const delegaciones=this.data.delegaciones
            delegaciones.forEach(delegacion => {
                console.log(delegacion)
                const cont = document.createElement('div')
                cont.id=`contenedor${delegacion.id}`
                reportes.appendChild(cont)
                const m=delegacion.metas
                var index=0
                m.forEach(meta =>{
                    console.log(`ANIO META: ${meta.anio}`)
                    console.log(`ANIO SELECT: ${parseInt(filtro_anio)}`)
                        if(meta.anio==parseInt(filtro_anio)){
                            for(;index<12;){
                                if(meta.mes==index+1){
                                    console.log(metas[index])
                                    metas[index]=meta.meta
                                    console.log(metas[index])
                                    alcanzadas[index]=meta.alcanzado
                                }
                                index++
                            } 
                        
                    }
                    grafica2(delegacion.id,delegacion.nombre,filtro_anio,metas,alcanzadas)
                })
                
            })
        }
    }
}

get_metas()

    