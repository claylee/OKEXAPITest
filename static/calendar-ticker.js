function getVirtulData(year,tickerData) {
    year = year || '2018';
    var date = +echarts.number.parseDate(year + '-01-01');
    var end = +echarts.number.parseDate((+year + 1) + '-01-01');
    var dayTime = 3600 * 24 * 1000;
    var data = [];
    for (var time = date; time < end; time += dayTime) {
        data.push([
            echarts.format.formatTime('yyyy-MM-dd', time),
            //Math.floor(Math.random() * 10000)
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
        if(a){continue;}

        dList.push(d);

    }
    return dList
}

var calendarTicker = {
  option : {
      title: {
          top: 30,
          left: 'center',
          text: '2016年某人每天的步数'
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
  myChart: {},
  init: function(dom){
        charC = echarts.init(dom);
        this.myChart = charC;
        this.myChart.setOption(this.option);
        return this;
  }

}
