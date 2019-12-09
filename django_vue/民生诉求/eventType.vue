<template>
  <div class="chart-box">
    <div class="date-box">
      <br>
      <br>
      <br>
      <span class="cc">请输入日期 &nbsp; </span>
      <el-date-picker
        v-model="value1"
        type="daterange"
        align="right"
        value-format="yyyyMMdd"
        start-placeholder="开始日期"
        end-placeholder="结束日期"
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
var scale = 1
var rich = {
  yellow: {
    color: '#ffc72b',
    fontSize: 30 * scale,
    padding: [5, 4],
    align: 'center'
  },
  total: {
    color: '#ffc72b',
    fontSize: 40 * scale,
    align: 'center'
  },
  white: {
    color: '#fff',
    align: 'center',
    fontSize: 14 * scale,
    padding: [21, 0]
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
      chart: null,
      value1: "['20191114', '20191210']"
    }
  },
  mounted() {
    this.initChart()
  },
  beforeDestroy() {
    if (!this.chart) {
      return
    }
    this.chart.dispose()
    this.chart = null
  },
  methods: {
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
        this.chart.setOption({
          backgroundColor: '#031f2d',
          title: {
            text: '事件总数',
            left: 'center',
            top: '53%',
            padding: [24, 0],
            textStyle: {
              color: '#fff',
              fontSize: 18 * scale,
              align: 'center'
            }
          },
          legend: {
            selectedMode: false,
            formatter: function(name) {
              var total = 0 // 各科正确率总和
              // var averagePercent // 综合正确率
              echartData.forEach(function(value, index, array) {
                total += value.value
              })
              return '{total|' + total + '}'
            },
            data: [echartData[0].name],
            // data: ['高等教育学'],
            // itemGap: 50,
            left: 'center',
            top: 'center',
            icon: 'none',
            align: 'center',
            textStyle: {
              color: '#fff',
              fontSize: 16 * scale,
              rich: rich
            }
          },
          series: [{
            name: '事件总数',
            type: 'pie',
            radius: ['42%', '50%'],
            hoverAnimation: false,
            color: ['#c487ee', '#deb140', '#49dff0', '#034079', '#6f81da', '#00ffb4'],
            label: {
              normal: {
                formatter: function(params, ticket, callback) {
                  var total = 0 // 考生总数量
                  var percent = 0 // 考生占比
                  echartData.forEach(function(value, index, array) {
                    total += value.value
                  })
                  percent = ((params.value / total) * 100).toFixed(1)
                  return '{white|' + params.name + '}\n{hr|}\n{yellow|' + params.value + '}\n{blue|' + percent + '%}'
                },
                rich: rich
              }
            },
            labelLine: {
              normal: {
                length: 55 * scale,
                length2: 0,
                lineStyle: {
                  color: '#0b5263'
                }
              }
            },
            data: echartData
          }]
        })
      })
    },
    initChart() {
      axios.get('/api/get_date_event', {
        params: {
          'date1': 20180208,
          'date2': 20181030,
        }
      }).then(response => {
        var tmpdata = response.data
        echartData[0].value = tmpdata['投诉']
        echartData[1].value = tmpdata['咨询']
        echartData[2].value = tmpdata['感谢']
        echartData[3].value = tmpdata['建议']
        echartData[4].value = tmpdata['求决']
        this.chart = echarts.init(document.getElementById(this.id))
        this.chart.setOption({
          backgroundColor: '#031f2d',
          title: {
            text: '事件总数',
            left: 'center',
            top: '53%',
            padding: [24, 0],
            textStyle: {
              color: '#fff',
              fontSize: 18 * scale,
              align: 'center'
            }
          },
          legend: {
            selectedMode: false,
            formatter: function(name) {
              var total = 0 // 各科正确率总和
              // var averagePercent // 综合正确率
              echartData.forEach(function(value, index, array) {
                total += value.value
              })
              return '{total|' + total + '}'
            },
            data: [echartData[0].name],
            // data: ['高等教育学'],
            // itemGap: 50,
            left: 'center',
            top: 'center',
            icon: 'none',
            align: 'center',
            textStyle: {
              color: '#fff',
              fontSize: 16 * scale,
              rich: rich
            }
          },
          series: [{
            name: '事件总数',
            type: 'pie',
            radius: ['42%', '50%'],
            hoverAnimation: false,
            color: ['#c487ee', '#deb140','#49dff0', '#034079', '#6f81da', '#00ffb4'],
            label: {
              normal: {
                formatter: function(params, ticket, callback) {
                  var total = 0 // 考生总数量
                  var percent = 0 // 考生占比
                  echartData.forEach(function(value, index, array) {
                    total += value.value
                  })
                  percent = ((params.value / total) * 100).toFixed(1)
                  return '{white|' + params.name + '}\n{hr|}\n{yellow|' + params.value + '}\n{blue|' + percent + '%}'
                },
                rich: rich
              }
            },
            labelLine: {
              normal: {
                length: 70 * scale,
                lineStyle: {
                  color: '#0b5263'
                }
              }
            },
            data: echartData
          }]
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
