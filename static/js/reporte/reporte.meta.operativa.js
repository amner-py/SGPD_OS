let reportes_container=document.querySelector('#reportes')
let anio_option=document.querySelector('#anio')
let delegacion_option=document.querySelector('#delegacion')
let aviso=document.querySelector('#aviso')


const graficar=({nombre_delegacion,anio,metas,alcanzadas})=>{
    Highcharts.chart(`contenedor`, {
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
          pointPadding: 0,
          pointPlacement: 0
        }, {
          name: 'Meta Alcanzada',
          color: 'rgba(126,86,134,.9)',
          data: alcanzadas,
          pointPadding: 0,
          pointPlacement: 0
        }]
      });
}

const get_metas=({anio,delegacion})=>{
    const options={
        method:'GET'
    }
    fetch(`/asignacion/api/metas_operativa/anio/${anio}/dele/${delegacion}`,options)
        .then(response => response.json())
        .then(data =>{
            console.log(data)
            set_metas(data)
        })
}

const set_metas=(data)=>{
    const contenedor_grafica=document.createElement('div')
    contenedor_grafica.id=`contenedor`
    reportes_container.appendChild(contenedor_grafica)
    graficar({
        nombre_delegacion:data.delegacion,
        metas:data.metas,
        alcanzadas:data.alcanzadas,
        anio:data.anio
    })  
}

const search=()=>{
    const anio=parseInt(anio_option.options[anio_option.selectedIndex].value)
    const delegacion=parseInt(delegacion_option.options[delegacion_option.selectedIndex].value)
    if(anio>0 && delegacion>0){
        aviso.setAttribute('hidden',true)
        get_metas({anio:anio,delegacion:delegacion})
    }else{
        aviso.removeAttribute('hidden')
    }
}