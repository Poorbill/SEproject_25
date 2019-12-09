<template>
  <div class="chart-box">
    <div class="date-box">
      <br>
      <br>
      <br>
      <el-select v-model="value" placeholder="所有月份" @change=Change>
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
      <span>&nbsp;&nbsp;&nbsp;&nbsp;</span>
<!--      <span class="cc">请输入日期 &nbsp; </span>-->
      <el-date-picker
        v-model="value1"
        type="daterange"
        align="right"
        value-format="yyyyMMdd"
        start-placeholder="2018-02-08"
        end-placeholder="2018-12-01"
        :picker-options="pickerOptions"
        :default-value="timeDefaultShow"
        @change="getMyDateTime()"
      />
    </div>
    <div :id="id" :class="className" :style="{height:height,width:width}" />
  </div>
</template>

<script>
import echarts from 'echarts'
import resize from './mixins/resize'
import axios from 'axios'
const totalDuration = 2000;
var close = 0
var scale = 1
var echartData = [{
  value: 0,
  name: '投诉' }, {
  value: 0,
  name: '咨询' }, {
  value: 0,
  name: '建议' }, {
  value: 0,
  name: '感谢' }, {
  value: 0,
  name: '求决' }]
var rich = {
  yellow: {
    color: '#ffc72b',
    fontSize: 30 * scale,
    padding: [5, 4],
    align: 'center'
  },
  total: {
    color: '#ffc72b',
    fontSize: 30 * scale,
    align: 'center'
  },
  white: {
    color: '#fff',
    align: 'center',
    fontSize: 25 * scale,
    padding: [5, 0]
  },
  blue: {
    color: '#49dff0',
    fontSize: 16 * scale,
    align: 'center'
  },
  hr: {
    borderColor: '#0b5263',
    width: '100%',
    borderWidth: 1,
    height: 0
  }
}
export default {
  mixins: [resize],
  props: {
    className: {
      type: String,
      default: 'chart'
    },
    id: {
      type: String,
      default: 'chart'
    },
    width: {
      type: String,
      default: '200px'
    },
    height: {
      type: String,
      default: '200px'
    }
  },
  data() {
    return {
      value: '',
      options: [{
        value: ['20180101','20180131'],
        label: '1月份'
      }, {
        value: ['20180201','20180229'],
        label: '2月份'
      }, {
        value: ['20180301','20180331'],
        label: '3月份'
      }, {
        value: ['20180401','20180430'],
        label: '4月份'
      }, {
        value: ['20180501','20180531'],
        label: '5月份'
      }, {
        value: ['20180601','20180630'],
        label: '6月份'
      }, {
        value: ['20180701','20180731'],
        label: '7月份'
      }, {
        value: ['20180801','20180831'],
        label: '8月份'
      }, {
        value: ['20180901','20180930'],
        label: '9月份'
      }, {
        value: ['20181001','20181031'],
        label: '10月份'
      }, {
        value: ['20181101','20181130'],
        label: '11月份'
      }, {
        value: ['20181201','20181230'],
        label: '12月份'
      }],
      timeDefaultShow: new Date('2018-02-08'),
      chart: null,
      value1: ['20180208', '20181201'],
      pickerOptions: {
        disabledDate(time) {
          var utcDate1 = new Date(Date.UTC(2018, 1, 7, 0, 0, 0))
          var utcDate2 = new Date(Date.UTC(2018, 11, 30, 0, 0, 0))
          console.log(Date.now())
          console.log(utcDate1)
          return time.getTime() < utcDate1 || time.getTime() > utcDate2
        }
      }
    }
  },
  mounted() {
    this.initChart()
    this.startMove()
    close = 0
  },
  beforeDestroy() {
    if (!this.chart) {
      return
    }
    this.chart.dispose()
    this.chart = null
    close = 1
  },
  methods: {
    Change() {
      this.value1 = this.value,
      this.getMyDateTime()
    },
    startMove() {
      let timer = setTimeout(() => {
        if (close === 0 ){
          this.startMove();
          this.getMyDateTime();}
      }, totalDuration)
    },
    getMyDateTime() {
      axios.get('/api/get_date_event', {
        params: {
          'date1': this.value1[0],
          'date2': this.value1[1],
        }
      }).then(response => {
        var tmpdata = response.data
        echartData[0].value = tmpdata['投诉']
        echartData[1].value = tmpdata['咨询']
        echartData[2].value = tmpdata['感谢']
        echartData[3].value = tmpdata['建议']
        echartData[4].value = tmpdata['求决']
        this.chart = echarts.init(document.getElementById(this.id))
        var total_num = 0
        for (var i = 0; i < echartData.length; i++) {
          total_num += echartData[i].value
        }
        this.chart.setOption({
          backgroundColor: '#031f2d',
          title: {
            text: '事件总数',
            subtext: total_num,
            textStyle: {
              color: '#f2f2f2',
              fontSize: 40,
              align: 'center',
              fontStyle: 'italic'
            },
            subtextStyle: {
              fontSize: 30,
              color: ['#ff9d19']
            },
            x: 'center',
            y: 'center',
          },
          tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b}: {c} ({d}%)'
          },
          legend: {
            orient: 'vertical',
            itemWidth: 24,
            itemHeight: 18,
            align: 'left',
            right: '8%',
            top: '5%',
            data: [echartData[0].name, echartData[1].name, echartData[2].name, echartData[3].name, echartData[4].name],
            textStyle: {
              color: '#fff',
              fontSize: '18'
            }
          },
          series: [
            {
              name: '事件数',
              type: 'pie',
              radius: ['45%', '55%'],
              color: ['#deb140','#c487ee', '#49dff0', '#cceee7', '#6f81da', '#00ffb4'],
              label: {
                normal: {
                  formatter: function(params, ticket, callback) {
                    var percent = 0 // 考生占比
                    percent = ((params.value / total_num) * 100).toFixed(1)
                    return '{white|' + params.name + '}\n{hr|}\n{yellow|' + params.value + '}\n{blue|' + percent + '%}'
                  },
                  rich: rich,
                  show: false
                },
                emphasis:{
                  formatter: function(params, ticket, callback) {
                    var percent = 0 // 考生占比
                    percent = ((params.value / total_num) * 100).toFixed(1)
                    return '{white|' + params.name + '}\n{yellow|' + params.value + '}\n{blue|' + percent + '%}'
                  },
                  rich: rich,
                  show: true
                }
              },
              labelLine: {
                normal: {
                  length: 45,
                  length2: 40,
                }
              },
              data: echartData
            }
          ]
        })
      })
    },
    initChart() {
      axios.get('/api/get_date_event', {
        params: {
          'date1': 20180208,
          'date2': 20181201,
        }
      }).then(response => {
        var tmpdata = response.data
        echartData[0].value = tmpdata['投诉']
        echartData[1].value = tmpdata['咨询']
        echartData[2].value = tmpdata['感谢']
        echartData[3].value = tmpdata['建议']
        echartData[4].value = tmpdata['求决']
        this.chart = echarts.init(document.getElementById(this.id))
        var total_num = 0
        for (var i = 0; i < echartData.length; i++) {
          total_num += echartData[i].value
        }
        this.chart.setOption({
          backgroundColor: '#031f2d',
          title: {
            text: '事件总数',
            subtext: total_num,
            textStyle: {
              color: '#f2f2f2',
              fontSize: 40,
              align: 'center',
              fontStyle: 'italic'
            },
            subtextStyle: {
              fontSize: 30,
              color: ['#ff9d19']
            },
            x: 'center',
            y: 'center',
          },
          tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b}: {c} ({d}%)'
          },
          legend: {
            orient: 'vertical',
            itemWidth: 24,
            itemHeight: 18,
            align: 'left',
            right: '8%',
            top: '5%',
            data: [echartData[0].name, echartData[1].name, echartData[2].name, echartData[3].name, echartData[4].name],
            textStyle: {
              color: '#fff',
              fontSize: '18'
            }
          },
          series: [
            {
              name: '事件数',
              type: 'pie',
              radius: ['45%', '55%'],
              color: ['#deb140','#c487ee', '#49dff0', '#cceee7', '#6f81da', '#00ffb4'],
              label: {
                normal: {
                  formatter: function(params, ticket, callback) {
                    var percent = 0 // 考生占比
                    percent = ((params.value / total_num) * 100).toFixed(1)
                    return '{white|' + params.name + '}\n{hr|}\n{yellow|' + params.value + '}\n{blue|' + percent + '%}'
                  },
                  rich: rich,
                  show: false
                },
                emphasis:{
                  formatter: function(params, ticket, callback) {
                    var percent = 0 // 考生占比
                    percent = ((params.value / total_num) * 100).toFixed(1)
                    return '{white|' + params.name + '}\n{yellow|' + params.value + '}\n{blue|' + percent + '%}'
                  },
                  rich: rich,
                  show: true
                }
              },
              labelLine: {
                normal: {
                  length: 45,
                  length2: 40,
                }
              },
              data: echartData
            }
          ]
        })
      })
    }
  }
}
</script>

<style>
  .chart-box{
    width: 100%;
    height: 100%;
  }
  .date-box{
    position: relative;
    width: 100%;
    background: #031f2d;
    text-align: right;
    padding-right: 90px;
  }
  .cc{
    color: #20a0ff;
    font-size: 20px;
  }
</style>
