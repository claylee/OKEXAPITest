function randomData() {
    now = new Date(+now + oneDay);
    value = value + Math.random() * 21 - 10;
    return {
        name: now.toString(),
        value: [
            [now.getFullYear(), now.getMonth() + 1, now.getDate()].join('/'),
            Math.round(value)
        ]
    }
}

function formChartData(data) {
    now = new Date(+now + oneDay);
    value = value + Math.random() * 21 - 10;
    return {
        name: now.toString(),
        value: [
            [now.getFullYear(), now.getMonth() + 1, now.getDate()].join('/'),
            data[8]
        ]
    }
}

var now = +new Date(1997, 9, 3);
var oneDay = 24 * 3600 * 1000;
var value = Math.random() * 1000;
//for (var i = 0; i < 1000; i++) {
//    data.push(randomData());
//}

var linechart = {
  data : [],
  option : {
      title: {
          text: '动态数据 + 时间坐标轴'
      },
      tooltip: {
          trigger: 'axis',
          formatter: function (params) {
              params = params[0];
              var date = new Date(params.name);
              return date.getDate() + '/' + (date.getMonth() + 1) + '/' + date.getFullYear() + ' : ' + params.value[1];
          },
          axisPointer: {
              animation: false
          }
      },
      xAxis: {
          type: 'time',
          splitLine: {
              show: true
          }
      },
      yAxis: {
          type: 'value',
          boundaryGap: [0, '100%'],
          min:'dataMin',
          splitLine: {
              show: true
          }
      },
      series: [{
          name: '模拟数据',
          type: 'line',
          showSymbol: false,
          hoverAnimation: false,
          data: this.data
      }]
  },
  myChart:{},
  init:function(domchart){
    this.myChart = echarts.init(domchart);
    this.myChart.setOption(this.option);
    return this;
  },
};
