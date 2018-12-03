function getVirtulData(year,tickerData) {
    year = year || '2018';
    var date = +echarts.number.parseDate(year + '-01-01');
    var end = +echarts.number.parseDate((+year + 1) + '-01-01');
    var dayTime = 3600 * 24 * 1000;
    var data = [];
    console.log(tickerData);
    for (var time = date; time < end; time += dayTime) {
        var dateString = echarts.format.formatTime('yyyy-MM-dd', time);
        var value = -1;
        console.log(dateString);
        if(tickerData && tickerData[dateString])
        {
            console.log(dateString);
            console.log(tickerData[dateString]);
            value = 9000;
        }
        data.push([
            echarts.format.formatTime('yyyy-MM-dd', time),
            //Math.floor(Math.random() * 10000)
            value
        ]);
    }
    return data;
}

function checkDate(dateList){
    dList = []
    for(var i in dateList)
    {
        var d = new Date(parseInt(dateList[i])*1000);
        var day = d.getDate();
        console.log(day);
        a = false;
        for(var key in dList)
        {
            if(key == d)
            {
              a = true;
              break;
            }
        }
        if(a)
        {
            continue;
        }

        dList.push(d);

    }
    return dList
}

var calendarTicker = {
  option : {
      title: {
          top: 30,
          left: 'center',
          text: 'ticker state'
      },
      tooltip : {},
      visualMap: {
          min: 0,
          max: 10000,
          type: 'piecewise',
          orient: 'horizontal',
          left: 'center',
          top: 65,
          textStyle: {
              color: '#000'
          }
      },
      calendar: {
          top: 120,
          left: 30,
          right: 30,
          cellSize: ['auto', 13],
          range: '2018',
          itemStyle: {
              normal: {borderWidth: 0.5}
          },
          yearLabel: {show: false}
      },
      series: {
          type: 'heatmap',
          coordinateSystem: 'calendar',
          data: getVirtulData()
      }
  },
  getStat:function(handle){
      this.myChart.setOption({
          series: {
              data: handle()
          }
      });
  },
  myChart: {},
  onclick:function(handle){
      this.myChart.on('click', handle);
  },
  init: function(dom){
        charC = echarts.init(dom);
        this.myChart = charC;
        this.myChart.setOption(this.option);
        return this;
  }
}

function rectclick(date,hour){

}


var HourTicker = {
    onclick:function(hanle){
        $("rect").on("click",function(e){//注册时间
            hanle($(this));
        });
    },
    tickerdata:{},
    init:function(dom,data,tdata){
        var rowOffset = 11;
        this.tickerdata = tdata;
        var g = $('<g translate(0, 0)></g>')
        var svg = $('<svg xmlns="http://www.w3.org/2000/svg" width="100" height="88" \
            class="js-calendar-graph-svg">');
        var cg = $("<g transform='translate(0,0)'></g>")
        for(var i=0; i<4;i++)
        {
            g = $("<g transform='translate("+ i * rowOffset + ",0)'></g>")
            for(var j=0; j<6; j++)
            {
                var key = data[0]+' '+(i*6+j+1);
                var color = "#c1c1c1";
                if(this.tickerdata && this.tickerdata[key])
                    color = "#c6e48b";
                var h = $('<rect class="day active" width="16" \
                  height="16" x="'+(16+i*rowOffset)+'" y="'+(20+j*(16+rowOffset))+'" fill="'+color+'" \
                  data-count="1" data-date="'+data[0]+'" data-hour="'+(i*6+j+1)+'"></rect>');
                var t = $('<text x="'+(16+i*rowOffset)+'" y="'+(20+j*(16+rowOffset) + 14)+'" width="16" \
                height="16" fill="#777777">'+(i*6+j + 1)+'</text>');
                //h.attr("onclick","rectclick("+data[0]+","+(i*6+j+1)+")");

                //h.append(t);
                $(g).append(h);
                //$(g).append(t);
            }
            $(cg).append(g);
        }
        $(svg).append(cg);
        $(dom).append(svg);
        $(dom).html($(dom).html());
        return this;
    }
}
