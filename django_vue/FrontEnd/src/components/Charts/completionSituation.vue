<template>
  <div class="chart-box">
    <div class="date-box">
      <br>
      <br>
      <br>
      <el-select v-model="value2" placeholder="所有季度" @change=Change2>
        <el-option
          v-for="item in options2"
          :key="item.value2"
          :label="item.label"
          :value="item.value2">
        </el-option>
      </el-select>
      <span>&nbsp;&nbsp;&nbsp;</span>
      <el-select v-model="value" placeholder="所有月份" @change=Change>
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
      <span>&nbsp;&nbsp;&nbsp;</span>
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
      <br>
    </div>
    <div :id="id" :class="className" :style="{height:height,width:width}" />
  </div>
</template>

<script>
import echarts from 'echarts'
import resize from './mixins/resize'
import { GetCompletion } from '@/api/charts'
import axios from 'axios'

var scale = 1
var data1 = ['超期结办','按期结办','处置中','市容城管','工业噪声','占道经营','绿化养护','公用部件','公共交通管理']
var data2 = [
  { value: 10, name: '超期结办' },
  { value: 10, name: '按期结办' },
  { value: 10, name: '处置中' }
]
// 总的事件数量
var data3 = [
  { value: 10, name: '市容城管' },
  { value: 10, name: '工业噪声' },
  { value: 10, name: '占道经营' },
  { value: 10, name: '绿化养护' },
  { value: 10, name: '公用部件' },
  { value: 10, name: '公共交通管理' }
]
// 按期
var data4 = [
  { value: 10, name: '市容城管' },
  { value: 10, name: '工业噪声' },
  { value: 10, name: '占道经营' },
  { value: 10, name: '绿化养护' },
  { value: 10, name: '公用部件' },
  { value: 10, name: '公共交通管理' }
]
// 超期
var data5 = [
  { value: 10, name: '市容城管' },
  { value: 10, name: '工业噪声' },
  { value: 10, name: '占道经营' },
  { value: 10, name: '绿化养护' },
  { value: 10, name: '公用部件' },
  { value: 10, name: '公共交通管理' }
]
// 处置中
var data6 = [
  { value: 10, name: '市容城管' },
  { value: 10, name: '工业噪声' },
  { value: 10, name: '占道经营' },
  { value: 10, name: '绿化养护' },
  { value: 10, name: '公用部件' },
  { value: 10, name: '公共交通管理' }
]
export default {
  name: 'CompletionSituation',
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
      value2: '',
      options2: [{
        value2: ['20180101', '20180331'],
        label: '第1季度'
      }, {
        value2: ['20180401', '20180630'],
        label: '第2季度'
      }, {
        value2: ['20180701', '20180930'],
        label: '第3季度'
      }, {
        value2: ['20181001', '20181230'],
        label: '第4季度'
      }],
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
      },
      i: 0
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
    Change2() {
      this.value1 = this.value2,
      this.getMyDateTime()
    },
    getMyDateTime() {
      axios.get('/api/get_problem_handled', {
        params: {
          'date1': this.value1[0],
          'date2': this.value1[1],
        }
      }).then(response => {
        console.log(response.data.data3.in_time)
        data2[0].value = response.data.data1.over_time
        data2[1].value = response.data.data1.in_time
        data2[2].value = response.data.data1.processing

        for (var i = 0; i < 6; i++) {
          data3[i].value = response.data.data2[data3[i].name]
        }
        for (i = 0; i < 6; i++) {
          data4[i].value = response.data.data3.in_time[i]
        }
        for (i = 0; i < 6; i++) {
          data5[i].value = response.data.data3.over_time[i]
        }
        for (i = 0; i < 6; i++) {
          data6[i].value = response.data.data3.processing[i]
        }
        var colors = ['#9b92fe', '#7ba5c6', '#1f62ea', '#1990e9', '#49ddfc', '#6bdafe', '#39f381', '#e9e37c']
        var myid = this.id
        var mychart = echarts.init(document.getElementById(myid))
        mychart.setOption({
          backgroundColor: '#031f2d',
          title: {
            text: '总览',
            textStyle: {
              color: '#f2f2f2',
              fontSize: 40,
              align: 'center',
              fontStyle: 'italic'
            },
            x: 'center'
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
            textStyle: {
              color: '#eeeeee',
              fontSize: '18'
            },
            data: data1
          },
          series: [
            {
              name: '结办情况',
              type: 'pie',
              selectedMode: 'single',
              radius: [0, '35%'],
              label: {
                position: 'inner',
                fontSize: '20'
              },
              labelLine: {
                normal: {
                  show: false
                }
              },
              color: colors,
              data: data2
            },
            {
              name: '问题性质',
              type: 'pie',
              radius: ['45%', '60%'],
              color: colors,
              labelLine: {
                normal: {
                  show: true
                }
              },
              label: {
                show: true,
                fontSize: '15'
              },
              data: data3
            }
          ]
        })
      })
    },
    initChart() {
      axios.get('/api/get_problem_handled', {
        params: {
          'date1': 20180208,
          'date2': 20181201,}
      }).then(response => {
        console.log(response.data.data3.in_time)
        data2[0].value = response.data.data1.over_time
        data2[1].value = response.data.data1.in_time
        data2[2].value = response.data.data1.processing

        for (var i = 0; i < 6; i++) {
          data3[i].value = response.data.data2[data3[i].name]
        }
        for (i = 0; i < 6; i++) {
          data4[i].value = response.data.data3.in_time[i]
        }
        for (i = 0; i < 6; i++) {
          data5[i].value = response.data.data3.over_time[i]
        }
        for (i = 0; i < 6; i++) {
          data6[i].value = response.data.data3.processing[i]
        }
        var colors = ['#9b92fe', '#7ba5c6', '#1f62ea', '#1990e9', '#49ddfc', '#6bdafe', '#39f381', '#e9e37c']
        var myid = this.id
        var mychart = echarts.init(document.getElementById(myid))
        var flag1 = 0
        var flag2 = 0
        var flag3 = 0
        mychart.setOption({
          backgroundColor: '#031f2d',
          title: {
            text: '总览',
            textStyle: {
              color: '#f2f2f2',
              fontSize: 40,
              align: 'center',
              fontStyle: 'italic'
            },
            x: 'center'
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
            textStyle: {
              color: '#eeeeee',
              fontSize: '18'
            },
            data: data1
          },
          series: [
            {
              name: '结办情况',
              type: 'pie',
              selectedMode: 'single',
              radius: [0, '35%'],
              label: {
                position: 'inner',
                fontSize: '20'
              },
              labelLine: {
                normal: {
                  show: false
                }
              },
              color: colors,
              data: data2
            },
            {
              name: '问题性质',
              type: 'pie',
              radius: ['45%', '60%'],
              color: colors,
              labelLine: {
                normal: {
                  show: true
                }
              },
              label: {
                show: true,
                fontSize: '15'
              },
              data: data3
            }
          ]
        })
        mychart.on('click', { seriesName: '结办情况' }, function(params) {
          if (params.name === '处置中') {
            if (!flag1) {
              mychart.setOption({
                title: {
                  text: '处置中',
                  textStyle: {
                    color: '#f2f2f2',
                    fontSize: 40,
                    align: 'center',
                    fontStyle: 'italic'
                  },
                  x: 'center'
                },
                series: [
                  {
                    name: '问题性质',
                    type: 'pie',
                    radius: ['45%', '60%'],
                    color: colors,
                    labelLine: {
                      normal: {
                        show: true
                      }
                    },
                    label: {
                      show: true
                    },
                    data: data6
                  }
                ]
              })
            } else if (flag1) {
              mychart.setOption({
                title: {
                  text: '总览',
                  textStyle: {
                    color: '#f2f2f2',
                    fontSize: 40,
                    align: 'center',
                    fontStyle: 'italic'
                  },
                  x: 'center'
                },
                series: [
                  {
                    name: '问题性质',
                    type: 'pie',
                    radius: ['45%', '60%'],
                    color: colors,
                    labelLine: {
                      normal: {
                        show: true
                      }
                    },
                    label: {
                      show: true
                    },
                    data: data3
                  }
                ]
              })
            }
            flag1 = !flag1
            flag2 = 0
            flag3 = 0
          } else if (params.name === '超期结办') {
            if (!flag2) {
              mychart.setOption({
                title: {
                  text: '超期结办',
                  textStyle: {
                    color: '#f2f2f2',
                    fontSize: 40,
                    align: 'center',
                    fontStyle: 'italic'
                  },
                  x: 'center'
                },
                series: [
                  {
                    name: '问题性质',
                    type: 'pie',
                    radius: ['45%', '60%'],
                    color: colors,
                    labelLine: {
                      normal: {
                        show: true
                      }
                    },
                    label: {
                      show: true
                    },
                    data: data5
                  }
                ]
              })
            } else if (flag2) {
              mychart.setOption({
                title: {
                  text: '总览',
                  textStyle: {
                    color: '#f2f2f2',
                    fontSize: 40,
                    align: 'center',
                    fontStyle: 'italic'
                  },
                  x: 'center'
                },
                series: [
                  {
                    name: '问题性质',
                    type: 'pie',
                    radius: ['45%', '60%'],
                    color: colors,
                    labelLine: {
                      normal: {
                        show: true
                      }
                    },
                    label: {
                      show: true
                    },
                    data: data3
                  }
                ]
              })
            }
            flag2 = !flag2
            flag1 = 0
            flag3 = 0
          } else if (params.name === '按期结办') {
            if (!flag3) {
              mychart.setOption({
                title: {
                  text: '按期结办',
                  textStyle: {
                    color: '#f2f2f2',
                    fontSize: 40,
                    align: 'center',
                    fontStyle: 'italic'
                  },
                  x: 'center'
                },
                series: [
                  {
                    name: '问题性质',
                    type: 'pie',
                    radius: ['45%', '60%'],
                    color: colors,
                    labelLine: {
                      normal: {
                        show: true
                      }
                    },
                    label: {
                      show: true
                    },
                    data: data4
                  }
                ]
              })
            } else if (flag3) {
              mychart.setOption({
                title: {
                  text: '总览',
                  textStyle: {
                    color: '#f2f2f2',
                    fontSize: 40,
                    align: 'center',
                    fontStyle: 'italic'
                  },
                  x: 'center'
                },
                series: [
                  {
                    name: '问题性质',
                    type: 'pie',
                    radius: ['45%', '60%'],
                    color: colors,
                    labelLine: {
                      normal: {
                        show: true
                      }
                    },
                    label: {
                      show: true
                    },
                    data: data3
                  }
                ]
              })
            }
            flag3 = !flag3
            flag1 = 0
            flag2 = 0
          }
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
