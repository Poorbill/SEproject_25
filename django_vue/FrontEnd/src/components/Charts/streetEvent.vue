<template>
  <div class ="chart-box">
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
      <el-date-picker
        v-model="value1"
        type="daterange"
        align="right"
        value-format="yyyyMMdd"
        start-placeholder="2018-02-08"
        end-placeholder="2018-12-01"
        @change="getMyDateTime()"
        :picker-options="pickerOptions"
        :default-value="timeDefaultShow"
      />
    </div>
    <div :id="id" :class="className" :style="{height:height,width:width}"></div>
  </div>
</template>

<script>

import echarts from 'echarts'
import resize from './mixins/resize'
import axios from 'axios'
var data1 = [20, 30, 20, 30, 20, 30]
var data2 = [9, 30, 9, 60, 70, 20]
var data3 = [20, 30, 20, 30, 20, 30]
var data4 = [20, 30, 20, 30, 20, 30]
var data5 = [20, 30, 20, 30, 20, 30]
var data6 = [20, 30, 20, 30, 20, 30]
var event_name = ['市容城管', '工业噪声', '占道经营', '绿化养护', '工业部件', '公共交通管理']
var datacity = ['龙田街道', '坪山街道', '碧岭街道', '坑梓街道', '马峦街道', '石井街道']

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
      value1: '',
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
  },
  beforeDestroy() {
    if (!this.chart) {
      return
    }
    this.chart.dispose()
    this.chart = null
  },
  methods: {
    Change() {
      this.value1 = this.value,
      this.getMyDateTime()
    },
    getMyDateTime() {
      axios.get('/api/get_date_street', {
        params: {
          'date1': this.value1[0],
          'date2': this.value1[1],
        }
      }).then(response => {
        var tmpdata = response.data
        console.log(tmpdata)
        data1 = tmpdata['市容城管']
        data2 = tmpdata['工业噪声']
        data3 = tmpdata['占道经营']
        data4 = tmpdata['绿化养护']
        data5 = tmpdata['公用部件']
        data6 = tmpdata['公共交通管理']
        this.chart.setOption({
          backgroundColor: '#031f2d',
          color: ['#deb140','#c487ee', '#49dff0', '#cceee7', '#6f81da', '#00ffb4'],
          tooltip: {
            trigger: 'axis'
          },
          legend: {
            bottom: '8%',
            // data: ['市容城管', '禽畜养殖污染', '市政/公共设施'],
            icon: 'circle',
            textStyle: {
              fontSize: 15,
              color: 'rgba(255,255,255,1)'
            }
          },
          grid: { // 图表的位置
            top: '20%',
            left: '3%',
            right: '4%',
            bottom: '13%',
            containLabel: true
          },
          yAxis: [{
            type: 'value',
            axisLine: {
              lineStyle: {
                color: 'rgba(255,255,255,1)'
              }
            },
            axisTick: {
              show: false
            },
            splitLine: {
              show: false
            },
            axisLabel: {
              show: true,
              interval: '0',
              fontSize: 12,
              color: 'rgba(255,255,255,1)'
            }

          }],
          xAxis: [{
            // type: 'category',
            axisLine: {
              lineStyle: {
                color: 'rgba(255,255,255,1)'
              }
            },
            axisTick: {
              show: false
            },
            splitLine: {
              show: false
            },
            axisLabel: {
              show: true,
              interval: '0',
              fontSize: 15,
              color: 'rgba(255,255,255,1)'
            },
            data: datacity
          }],
          series: [{
            name: event_name[0],
            type: 'bar',
            stack: '1',
            barWidth: '35px',
            data: data1
          },
          {
            name: event_name[1],
            type: 'bar',
            barWidth: '35px',
            stack: '1',
            data: data2
          },
          {
            name: event_name[2],
            type: 'bar',
            color: '#F6931C',
            stack: '1',
            barWidth: '35px',
            data: data3
          },
          {
            name: event_name[3],
            type: 'bar',
            barWidth: '35px',
            stack: '1',
            fontSize: '15',
            data: data4
          },
          {
            name: event_name[4],
            type: 'bar',
            barWidth: '35px',
            stack: '1',
            data: data5
          },
          {
            name: event_name[5],
            type: 'bar',
            barWidth: '35px',
            stack: '1',
            data: data6
          },
          ]
        })
      })
    },
    initChart() {
      this.chart = echarts.init(document.getElementById(this.id))
      axios.get('/api/get_date_street', {
        params: {
          'date1': 20180208,
          'date2': 20181201,
        }
      }).then(response => {
        var tmpdata = response.data
        console.log(tmpdata)
        data1 = tmpdata['市容城管']
        data2 = tmpdata['工业噪声']
        data3 = tmpdata['占道经营']
        data4 = tmpdata['绿化养护']
        data5 = tmpdata['公用部件']
        data6 = tmpdata['公共交通管理']
        this.chart.setOption({
          backgroundColor: '#031f2d',
          color: ['#deb140','#c487ee', '#49dff0', '#cceee7', '#6f81da', '#00ffb4'],
          tooltip: {
            trigger: 'axis'
          },
          legend: {
            bottom: '8%',
            // data: ['市容城管', '禽畜养殖污染', '市政/公共设施'],
            icon: 'circle',
            textStyle: {
              fontSize: 15,
              color: 'rgba(255,255,255,1)'
            }
          },
          grid: { // 图表的位置
            top: '20%',
            left: '3%',
            right: '4%',
            bottom: '13%',
            containLabel: true
          },
          yAxis: [{
            type: 'value',
            axisLine: {
              lineStyle: {
                color: 'rgba(255,255,255,1)'
              }
            },
            axisTick: {
              show: false
            },
            splitLine: {
              show: false
            },
            axisLabel: {
              show: true,
              interval: '0',
              fontSize: 15,
              color: 'rgba(255,255,255,1)'
            }
          }],
          xAxis: [{
            // type: 'category',
            axisLine: {
              lineStyle: {
                color: 'rgba(255,255,255,1)'
              }
            },
            axisTick: {
              show: false
            },
            splitLine: {
              show: false
            },
            axisLabel: {
              show: true,
              interval: '0',
              fontSize: 20,
              color: 'rgba(255,255,255,1)'
            },
            data: datacity
          }],
          series: [{
            name: event_name[0],
            type: 'bar',
            stack: '1',
            barWidth: '35px',
            data: data1
          },
          {
            name: event_name[1],
            type: 'bar',
            barWidth: '35px',
            stack: '1',
            data: data2
          },
          {
            name: event_name[2],
            type: 'bar',
            color: '#F6931C',
            stack: '1',
            barWidth: '35px',
            data: data3
          },
          {
            name: event_name[3],
            type: 'bar',
            barWidth: '35px',
            stack: '1',
            data: data4
          },
          {
            name: event_name[4],
            type: 'bar',
            barWidth: '35px',
            stack: '1',
            data: data5
          },
          {
            name: event_name[5],
            type: 'bar',
            barWidth: '35px',
            stack: '1',
            data: data6
          },
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
