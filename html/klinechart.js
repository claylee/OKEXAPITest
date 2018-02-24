
function calculateMA(data0, dayCount) {
    var result = [];
    console.log("calculateMA");
    console.log(data0);
    for (var i = 0, len = data0.values.length; i < len; i++) {
        if (i < dayCount) {
            result.push('-');
            continue;
        }
        var sum = 0;
        for (var j = 0; j < dayCount; j++) {
            sum += parseFloat(data0.values[i - j][1]);
        }
        console.log('sum:'+sum);
        console.log(sum / dayCount);
        result.push(sum / dayCount);
    }
    return result;
}

function  formatDate(dateObj)   {
    var str,colorhead,colorfoot;

    str =dateObj.getUTCFullYear() + '/' + (dateObj.getUTCMonth() +1 )
    + '/' + dateObj.getUTCDate() + " " +dateObj.getUTCHours()
    +":"+dateObj.getUTCMinutes() + ":" + dateObj.getUTCSeconds();//
    //str = dateObj.toLocaleString();//
    // + " " + hh + ":" + mm + ":" + ss;
    return(str);
}
/*
var dates = rawData.map(function (item) {
    return item[0];
});
*/
var data0 = [];
var option = {
};
var upColor = '#ec0000';
var upBorderColor = '#8A0000';
var downColor = '#00da3c';
var downBorderColor = '#008F28';

function splitData(rawData) {
  console.log("-----------------------");
  //console.log(rawData);
    var categoryData = [];
    var values = []
    for (var i = 0; i < rawData.length; i++) {
        //console.log(i);
        //console.log(rawData[i]);
        //console.log(rawData[i].splice(0, 1)[0]);
        categoryData.push(rawData[i][0]);
        values.push([rawData[i][1],rawData[i][2],rawData[i][5],rawData[i][6]]);
    }
    //console.log(values);
    return {
        categoryData: categoryData,
        values: values
      };
}


  function AddKandleItem(item)
  {
    var kItem = new Array();
    var timestamp = item[0];
    var date = new Date(timestamp*1);
    console.log(timestamp);
    //kdata[0][0] = formatDate(date);
    kItem.push(formatDate(date));
    kItem.push(item[1]);
    kItem.push(item[4]);
    kItem.push("-=");
    kItem.push("-+");
    kItem.push(item[3]);
    kItem.push(item[2]);
    kItem.push(item[5]);
    kItem.push(item[6]);
    kItem.push("-");
    console.log("===============");
    //console.log(kItem);
    //console.log(kItem.length + ":" + kItem[0]);
    rawData.push(kItem);
    //console.log(kItem.length);
    //console.log(rawData.length);
    //console.log(rawData);
      RefreshChartOpt();
      myChart.setOption(option);
  }

//myChart.setOption(option);

var klinechart = {
   rawData : [
        //['2015/12/31','3570.47','3539.18','-33.69','-0.94%','3538.35','3580.6','176963664','25403106','-']
      ].reverse(),
    myChart:{},
        nameP:"papapa",
    init: function(domchart){
      myChart = echarts.init(domchart);
      return this;
    },
    ConvertItem:function(item){
      console.log(item instanceof Array);
      console.log(item);
      if(!(item instanceof Array))
      {
        console.log('item instanceof Array');
        return this.ConvertItemBithumb(item);
      }
        var kItem = new Array();
        var timestamp = item[0];
        var date = new Date(timestamp*1);
        console.log("===============");
        console.log(item);
        console.log(timestamp);
        //kdata[0][0] = formatDate(date);
        kItem.push(formatDate(date));
        kItem.push(item[1]);//open
        kItem.push(item[4]);//close
        kItem.push("-=");
        kItem.push("-+");
        kItem.push(item[3]);//lowest
        kItem.push(item[2]);//high
        kItem.push(item[5]);
        //kItem.push(item[6]);
        kItem.push("-");
        return kItem;
    },
    ConvertItemBithumb:function(item)
    {
      var kItem = new Array();
      var timestamp = item["date"];
      var date = new Date(timestamp*1);
      console.log("=======ConvertItemBithumb========");
      console.log(timestamp);
      //kdata[0][0] = formatDate(date);
      kItem.push(formatDate(date));
      kItem.push(item["opening_price"]);//open
      kItem.push(item["closing_price"]);//close
      kItem.push("-=");
      kItem.push("-+");
      kItem.push(item["buy_price"]);//lowest
      kItem.push(item["sell_price"]);//high
      kItem.push(item["sell_price"]);//
      //kItem.push(item[6]);
      kItem.push("-");
      return kItem;
    },
    AddKandleItem:function(item)
    {
      console.log("========AddKandleItem=======");
      //console.log(kItem);
      //console.log(kItem.length + ":" + kItem[0]);
      this.rawData.push(ConvertItem(item));
      this.refresh();
    },
    ExtendItem:function(itemList)
    {
      for(var i in itemList){
        var item = itemList[i];
        this.rawData.push(ConvertItem(item));
      }
      this.refresh();
    },
    resetData:function(itemList)
    {
      this.rawData = [];
      for(var i in itemList){
        var item = itemList[i];
        this.rawData.push(this.ConvertItem(item));
      }
      this.refresh();
        this.rawData.splice(0,this.rawData.length);;
    },
    addItem1:function(item){
        var kItem = new Array();
        var timestamp = item['timestamp'];
        var date = new Date(timestamp*1);
        console.log("===============");
        console.log(timestamp);
        console.log(item);
        //kdata[0][0] = formatDate(date);
        kItem.push(formatDate(date));
        kItem.push(item['open']);
        kItem.push(item['close']);
        kItem.push("-=");
        kItem.push("-+");
        kItem.push(item['buy']);
        kItem.push(item['sell']);
        kItem.push(item['high']);
        kItem.push(item['low']);
        kItem.push("-");
        console.log("===============");
        //console.log(kItem);
        //console.log(kItem.length + ":" + kItem[0]);
        this.rawData.push(kItem);
        //console.log(kItem.length);
        //console.log(rawData.length);
        //console.log(rawData);
        this.refresh();
    },
    refresh:function()
    {
      //rawData.map(function (item) {
      //  return [+item[1], +item[2], +item[5], +item[6]];
      //})
      //console.log(rawData);
      console.log('rowdata:');
      var data0 = splitData(this.rawData);
      //console.log(data0.values[1]);
      option = {
        title: {
            text: 'OKEX SPOT _KLine 3min',
            left: 0
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'cross'
            }
        },
        legend: {
            data: ['日K', 'MA5', 'MA10', 'MA20', 'MA30']
        },
        grid: {
            left: '10%',
            right: '10%',
            bottom: '15%'
        },
        xAxis: {
            type: 'category',
            data: data0.categoryData,
            scale: true,
            boundaryGap : false,
            axisLine: {onZero: false},
            splitLine: {show: false},
            splitNumber: 20,
            min: 'dataMin',
            max: 'dataMax'
        },
        yAxis: {
            scale: true,
            splitArea: {
                show: true
            }
        },
        dataZoom: [
            {
                type: 'inside',
                start: 50,
                end: 100
            },
            {
                show: true,
                type: 'slider',
                y: '90%',
                start: 50,
                end: 100
            }
        ],
        series: [
            {
                name: '日K',
                type: 'candlestick',
                data: data0.values,
                itemStyle: {
                    normal: {
                        color: upColor,
                        color0: downColor,
                        borderColor: upBorderColor,
                        borderColor0: downBorderColor
                    }
                },
                markPoint: {
                    label: {
                        normal: {
                            formatter: function (param) {
                                return param != null ? Math.round(param.value) : '';
                            }
                        }
                    },
                    data: [
                        {
                            name: 'XX标点',
                            coord: ['2013/5/31', 2300],
                            value: 2300,
                            itemStyle: {
                                normal: {color: 'rgb(41,60,85)'}
                            }
                        },
                        {
                            name: 'highest value',
                            type: 'max',
                            valueDim: 'highest'
                        },
                        {
                            name: 'lowest value',
                            type: 'min',
                            valueDim: 'lowest'
                        },
                        {
                            name: 'average value on close',
                            type: 'average',
                            valueDim: 'close'
                        }
                    ],
                    tooltip: {
                        formatter: function (param) {
                            return param.name + '<br>' + (param.data.coord || '');
                        }
                    }
                },
                markLine: {
                    symbol: ['none', 'none'],
                    data: [
                        [
                            {
                                name: 'from lowest to highest',
                                type: 'min',
                                valueDim: 'lowest',
                                symbol: 'circle',
                                symbolSize: 10,
                                label: {
                                    normal: {show: false},
                                    emphasis: {show: false}
                                }
                            },
                            {
                                type: 'max',
                                valueDim: 'highest',
                                symbol: 'circle',
                                symbolSize: 10,
                                label: {
                                    normal: {show: false},
                                    emphasis: {show: false}
                                }
                            }
                        ],
                        {
                            name: 'min line on close',
                            type: 'min',
                            valueDim: 'close'
                        },
                        {
                            name: 'max line on close',
                            type: 'max',
                            valueDim: 'close'
                        }
                    ]
                }
            },
            {
                name: 'MA5',
                type: 'line',
                data: calculateMA(splitData(this.rawData),5),
                smooth: true,
                lineStyle: {
                    normal: {opacity: 0.5}
                }
            },
            {
                name: 'MA10',
                type: 'line',
                data: calculateMA(splitData(this.rawData),10),
                smooth: true,
                lineStyle: {
                    normal: {opacity: 0.5}
                }
            },
            {
                name: 'MA20',
                type: 'line',
                data: calculateMA(splitData(this.rawData),20),
                smooth: true,
                lineStyle: {
                    normal: {opacity: 0.5}
                }
            },
            {
                name: 'MA30',
                type: 'line',
                data: calculateMA(splitData(this.rawData),30),
                smooth: true,
                lineStyle: {
                    normal: {opacity: 0.5}
                }
            },

        ]
      };
      myChart.setOption(option);
    }
}
