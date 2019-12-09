<template>
  <div class="chart-box">
    <div class="date-box">
      <br>
      <span class = hot> 热点社区</span>
<!--      <span class="cc">请输入日期 &nbsp; </span>-->
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
        :picker-options="pickerOptions"
        :default-value="timeDefaultShow"
        @change="getMyDateTime()"
      />
    </div>
    <!--    <div :id="id" :class="className" :style="{height:height,width:width}">-->
    <!--    </div>-->
    <!--    <baidu-map class="map" :center="center" :zoom="map_zoom" @ready="handler">-->
    <!--      <template v-for="it in list">-->
    <!--        <bm-marker-->
    <!--          :key="it.id"-->
    <!--          :position="{lng:it.lng,lat: it.lat}"-->
    <!--          animation="BMAP_ANIMATION_BOUNCE"-->
    <!--          @click="infoWindowOpen"-->
    <!--        >-->
    <!--          <bm-label content="this.value1" :label-style="{color: 'red', fontSize : '24px'}" :offset="{width: -35, height: 30}" />-->
    <!--        </bm-marker>-->

    <!--      </template>-->
    <!--    </baidu-map>-->
    <div :id="id" :class="className" :style="{height:height,width:width}" />
  </div>
</template>

<script>
import resize from './mixins/resize'
import { getmap } from '@/api/charts'
import axios from 'axios'
// import { BaiduMap, BmScale, BmGeolocation, BmMarker } from 'vue-baidu-map'
var data = [
  { name: '南布社区', value: 0 },
  { name: '和平社区', value: 0 },
  { name: '坪山社区', value: 0 },
  { name: '汤坑社区', value: 0 },
  { name: '金沙社区', value: 0 },
  { name: '江岭社区', value: 0 },
  { name: '石井社区', value: 0 },
  { name: '六和社区', value: 0 },
  { name: '沙湖社区', value: 0 },
  { name: '老坑社区', value: 0 },
  { name: '竹坑社区', value: 0 },
  { name: '秀新社区', value: 0 },
  { name: '沙田社区', value: 0 },
  { name: '六联社区', value: 0 },
  { name: '坪环社区', value: 0 },
  { name: '龙田社区', value: 0 },
  { name: '坑梓社区', value: 0 },
  { name: '沙坣社区', value: 0 },
  { name: '田头社区', value: 0 },
  { name: '田心社区', value: 0 },
  { name: '碧岭社区', value: 0 },
  { name: '金龟社区', value: 0 },
  { name: '马峦社区', value: 0 }
]
var geoCoordMap = {
  '南布社区': [114.375607, 22.70534],
  '和平社区': [114.355590, 22.698584],
  '坪山社区': [114.355590, 22.694636],
  '汤坑社区': [114.331079, 22.678805],
  '金沙社区': [114.408079, 22.743131],
  '江岭社区': [114.362596, 22.69202],
  '石井社区': [114.390978, 22.697625],
  '六和社区': [114.349914, 22.707919],
  '沙湖社区': [114.326552, 22.67909],
  '老坑社区': [114.369312, 22.734866],
  '竹坑社区': [114.395074, 22.715773],
  '秀新社区': [114.381223, 22.746873],
  '沙田社区': [114.404444, 22.761764],
  '六联社区': [114.332971, 22.795219],
  '坪环社区': [114.355763, 22.687757],
  '龙田社区': [114.372841, 22.753347],
  '坑梓社区': [114.390013, 22.753031],
  '沙坣社区': [114.373122, 22.692444],
  '田头社区': [114.410837, 22.697197],
  '田心社区': [114.421943, 22.700351],
  '碧岭社区': [114.295663, 22.67342],
  '金龟社区': [114.406461, 22.663744],
  '马峦社区': [114.338203, 22.644538],
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
      axios.get('/api/get_hotcommunity', {
        params: {
          'date1': this.value1[0],
          'date2': this.value1[1],
        }
      }).then(response => {
        this.chart = echarts.init(document.getElementById(this.id))
        for (var i = 0; i < 22; i++) {
          data[i].value = response.data[data[i].name]
        }
        var convertData = function(data) { // 处理数据函数
          var res = []
          for (var i = 0; i < data.length; i++) {
            var geoCoord = geoCoordMap[data[i].name]
            if (geoCoord) {
              res.push({
                name: data[i].name,
                value: geoCoord.concat(data[i].value)
              })
            }
          }
          return res
        }
        var tmp = convertData(data)
        console.log(tmp)
        this.chart.setOption({
          backgroundColor: 'transparent',
          // title: {
          //   text: '热点社区',
          //   left: 'center',
          //   textStyle: {
          //     color: '#fff'
          //   }
          // },
          tooltip: {
            trigger: 'item',
            formatter: function(params, ticket, callback) {
              var res = params.name + '<br/>'
              // for (let i = 0, l = params.length; i < l; i++) {
              //   res += '<br/>' + params[i].marker + params[i].seriesName + ' : ' + params[i].value + 'KB/s'
              // }
              res = res + '事件数量: ' + params.value[2]
              return res
            }
          },
          bmap: {
            center: [114.34632, 22.7084],
            zoom: 13,
            roam: true,
            mapStyle: {
              styleJson: [
                {
                  'featureType': 'land',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on',
                    'color': '#091220ff'
                  }
                }, {
                  'featureType': 'water',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on',
                    'color': '#113549ff'
                  }
                }, {
                  'featureType': 'green',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on',
                    'color': '#0e1b30ff'
                  }
                }, {
                  'featureType': 'building',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'building',
                  'elementType': 'geometry.fill',
                  'stylers': {
                    'color': '#aaaaacb3'
                  }
                }, {
                  'featureType': 'building',
                  'elementType': 'geometry.stroke',
                  'stylers': {
                    'color': '#dadadab3'
                  }
                }, {
                  'featureType': 'subwaystation',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on',
                    'color': '#b15454B2'
                  }
                }, {
                  'featureType': 'education',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on',
                    'color': '#e4f1f1ff'
                  }
                }, {
                  'featureType': 'medical',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on',
                    'color': '#f0dedeff'
                  }
                }, {
                  'featureType': 'scenicspots',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on',
                    'color': '#e2efe5ff'
                  }
                }, {
                  'featureType': 'highway',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on',
                    'weight': 3
                  }
                }, {
                  'featureType': 'highway',
                  'elementType': 'geometry.fill',
                  'stylers': {
                    'color': '#f7c54dff'
                  }
                }, {
                  'featureType': 'highway',
                  'elementType': 'geometry.stroke',
                  'stylers': {
                    'color': '#fed669ff'
                  }
                }, {
                  'featureType': 'highway',
                  'elementType': 'labels',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'highway',
                  'elementType': 'labels.text.fill',
                  'stylers': {
                    'color': '#8f5a33ff'
                  }
                }, {
                  'featureType': 'highway',
                  'elementType': 'labels.text.stroke',
                  'stylers': {
                    'color': '#ffffffff'
                  }
                }, {
                  'featureType': 'highway',
                  'elementType': 'labels.icon',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'arterial',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on',
                    'weight': 2
                  }
                }, {
                  'featureType': 'arterial',
                  'elementType': 'geometry.fill',
                  'stylers': {
                    'color': '#d8d8d8ff'
                  }
                }, {
                  'featureType': 'arterial',
                  'elementType': 'geometry.stroke',
                  'stylers': {
                    'color': '#ffeebbff'
                  }
                }, {
                  'featureType': 'arterial',
                  'elementType': 'labels',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'arterial',
                  'elementType': 'labels.text.fill',
                  'stylers': {
                    'color': '#525355ff'
                  }
                }, {
                  'featureType': 'arterial',
                  'elementType': 'labels.text.stroke',
                  'stylers': {
                    'color': '#ffffffff'
                  }
                }, {
                  'featureType': 'local',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on',
                    'weight': 1
                  }
                }, {
                  'featureType': 'local',
                  'elementType': 'geometry.fill',
                  'stylers': {
                    'color': '#d8d8d8ff'
                  }
                }, {
                  'featureType': 'local',
                  'elementType': 'geometry.stroke',
                  'stylers': {
                    'color': '#ffffffff'
                  }
                }, {
                  'featureType': 'local',
                  'elementType': 'labels',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'local',
                  'elementType': 'labels.text.fill',
                  'stylers': {
                    'color': '#979c9aff'
                  }
                }, {
                  'featureType': 'local',
                  'elementType': 'labels.text.stroke',
                  'stylers': {
                    'color': '#ffffffff'
                  }
                }, {
                  'featureType': 'railway',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on',
                    'weight': 1
                  }
                }, {
                  'featureType': 'railway',
                  'elementType': 'geometry.fill',
                  'stylers': {
                    'color': '#123c52ff'
                  }
                }, {
                  'featureType': 'railway',
                  'elementType': 'geometry.stroke',
                  'stylers': {
                    'color': '#12223dff'
                  }
                }, {
                  'featureType': 'subway',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on',
                    'weight': 1
                  }
                }, {
                  'featureType': 'subway',
                  'elementType': 'geometry.fill',
                  'stylers': {
                    'color': '#d8d8d8ff'
                  }
                }, {
                  'featureType': 'subway',
                  'elementType': 'geometry.stroke',
                  'stylers': {
                    'color': '#ffffff00'
                  }
                }, {
                  'featureType': 'subway',
                  'elementType': 'labels',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'subway',
                  'elementType': 'labels.text.fill',
                  'stylers': {
                    'color': '#979c9aff'
                  }
                }, {
                  'featureType': 'subway',
                  'elementType': 'labels.text.stroke',
                  'stylers': {
                    'color': '#ffffffff'
                  }
                }, {
                  'featureType': 'continent',
                  'elementType': 'labels',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'continent',
                  'elementType': 'labels.icon',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'continent',
                  'elementType': 'labels.text.fill',
                  'stylers': {
                    'color': '#333333ff'
                  }
                }, {
                  'featureType': 'continent',
                  'elementType': 'labels.text.stroke',
                  'stylers': {
                    'color': '#ffffffff'
                  }
                }, {
                  'featureType': 'city',
                  'elementType': 'labels.icon',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'city',
                  'elementType': 'labels',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'city',
                  'elementType': 'labels.text.fill',
                  'stylers': {
                    'color': '#454d50ff'
                  }
                }, {
                  'featureType': 'city',
                  'elementType': 'labels.text.stroke',
                  'stylers': {
                    'color': '#ffffffff'
                  }
                }, {
                  'featureType': 'town',
                  'elementType': 'labels.icon',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'town',
                  'elementType': 'labels',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'town',
                  'elementType': 'labels.text.fill',
                  'stylers': {
                    'color': '#454d50ff'
                  }
                }, {
                  'featureType': 'town',
                  'elementType': 'labels.text.stroke',
                  'stylers': {
                    'color': '#ffffffff'
                  }
                }, {
                  'featureType': 'road',
                  'elementType': 'geometry.fill',
                  'stylers': {
                    'color': '#12223dff'
                  }
                }, {
                  'featureType': 'poilabel',
                  'elementType': 'labels',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'districtlabel',
                  'elementType': 'labels',
                  'stylers': {
                    'visibility': 'off'
                  }
                }, {
                  'featureType': 'road',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'road',
                  'elementType': 'labels',
                  'stylers': {
                    'visibility': 'off'
                  }
                }, {
                  'featureType': 'road',
                  'elementType': 'geometry.stroke',
                  'stylers': {
                    'color': '#ffffff00'
                  }
                }, {
                  'featureType': 'district',
                  'elementType': 'labels',
                  'stylers': {
                    'visibility': 'off'
                  }
                }, {
                  'featureType': 'poilabel',
                  'elementType': 'labels.icon',
                  'stylers': {
                    'visibility': 'off'
                  }
                }, {
                  'featureType': 'poilabel',
                  'elementType': 'labels.text.fill',
                  'stylers': {
                    'color': '#2dc4bbff'
                  }
                }, {
                  'featureType': 'poilabel',
                  'elementType': 'labels.text.stroke',
                  'stylers': {
                    'color': '#ffffff00'
                  }
                }, {
                  'featureType': 'manmade',
                  'elementType': 'geometry',
                  'stylers': {
                    'color': '#12223dff'
                  }
                }, {
                  'featureType': 'districtlabel',
                  'elementType': 'labels.text.stroke',
                  'stylers': {
                    'color': '#ffffffff'
                  }
                }, {
                  'featureType': 'entertainment',
                  'elementType': 'geometry',
                  'stylers': {
                    'color': '#ffffffff'
                  }
                }, {
                  'featureType': 'shopping',
                  'elementType': 'geometry',
                  'stylers': {
                    'color': '#12223dff'
                  }
                }
              ]
            }
          },
          series: [
            {
              name: 'Top 5',
              type: 'effectScatter',
              coordinateSystem: 'bmap',
              data: convertData(data.sort(function(a, b) {
                return b.value - a.value
              }).slice(0, 12)),
              symbolSize: function(val) {
                if (val[2] > 100){
                  return val[2] / 20}
                else if (val[2] <= 40){
                  return val[2] }
                else {
                  return val[2]/5 }
              },
              showEffectOn: 'render',
              rippleEffect: {
                period: 4, // 动画时间，值越小速度越快
                brushType: 'fill', // 波纹绘制方式 stroke, fill
                scale: 2 // 波纹圆环最大限制，值越大波纹越大
              },
              hoverAnimation: true,
              label: {
                normal: {
                  formatter: '{b}',
                  position: 'right',
                  show: true
                },
                emphasis: {
                  formatter: '{b}: {@[2]}'
                }
              },
              itemStyle: {
                normal: {
                  color: '#f4e925',
                  shadowBlur: 10,
                  shadowColor: '#333'
                }
              },
              zlevel: 1
            }
          ]
        })
      })
    },
    initChart() {
      axios.get('/api/get_hotcommunity', {
        params: {
          'date1': 20180208,
          'date2': 20181201,
        }
      }).then(response => {
        this.chart = echarts.init(document.getElementById(this.id))
        for (var i = 0; i < 22; i++) {
          data[i].value = response.data[data[i].name]
        }
        var convertData = function(data) { // 处理数据函数
          var res = []
          for (var i = 0; i < data.length; i++) {
            var geoCoord = geoCoordMap[data[i].name]
            if (geoCoord) {
              res.push({
                name: data[i].name,
                value: geoCoord.concat(data[i].value)
              })
            }
          }
          return res
        }
        var tmp = convertData(data)
        console.log(tmp)
        this.chart.setOption({
          backgroundColor: 'transparent',
          // title: {
          //   text: '热点社区',
          //   left: 'center',
          //   textStyle: {
          //     color: '#fff'
          //   }
          // },
          tooltip: {
            trigger: 'item',
            formatter: function(params, ticket, callback) {
              var res = params.name + '<br/>'
              // for (let i = 0, l = params.length; i < l; i++) {
              //   res += '<br/>' + params[i].marker + params[i].seriesName + ' : ' + params[i].value + 'KB/s'
              // }
              res = res + '事件数量: ' + params.value[2]
              return res
            }
          },
          bmap: {
            center: [114.34632, 22.7084],
            zoom: 13,
            roam: true,
            mapStyle: {
              styleJson: [
                {
                  'featureType': 'land',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on',
                    'color': '#091220ff'
                  }
                }, {
                  'featureType': 'water',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on',
                    'color': '#113549ff'
                  }
                }, {
                  'featureType': 'green',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on',
                    'color': '#0e1b30ff'
                  }
                }, {
                  'featureType': 'building',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'building',
                  'elementType': 'geometry.fill',
                  'stylers': {
                    'color': '#aaaaacb3'
                  }
                }, {
                  'featureType': 'building',
                  'elementType': 'geometry.stroke',
                  'stylers': {
                    'color': '#dadadab3'
                  }
                }, {
                  'featureType': 'subwaystation',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on',
                    'color': '#b15454B2'
                  }
                }, {
                  'featureType': 'education',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on',
                    'color': '#e4f1f1ff'
                  }
                }, {
                  'featureType': 'medical',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on',
                    'color': '#f0dedeff'
                  }
                }, {
                  'featureType': 'scenicspots',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on',
                    'color': '#e2efe5ff'
                  }
                }, {
                  'featureType': 'highway',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on',
                    'weight': 3
                  }
                }, {
                  'featureType': 'highway',
                  'elementType': 'geometry.fill',
                  'stylers': {
                    'color': '#f7c54dff'
                  }
                }, {
                  'featureType': 'highway',
                  'elementType': 'geometry.stroke',
                  'stylers': {
                    'color': '#fed669ff'
                  }
                }, {
                  'featureType': 'highway',
                  'elementType': 'labels',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'highway',
                  'elementType': 'labels.text.fill',
                  'stylers': {
                    'color': '#8f5a33ff'
                  }
                }, {
                  'featureType': 'highway',
                  'elementType': 'labels.text.stroke',
                  'stylers': {
                    'color': '#ffffffff'
                  }
                }, {
                  'featureType': 'highway',
                  'elementType': 'labels.icon',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'arterial',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on',
                    'weight': 2
                  }
                }, {
                  'featureType': 'arterial',
                  'elementType': 'geometry.fill',
                  'stylers': {
                    'color': '#d8d8d8ff'
                  }
                }, {
                  'featureType': 'arterial',
                  'elementType': 'geometry.stroke',
                  'stylers': {
                    'color': '#ffeebbff'
                  }
                }, {
                  'featureType': 'arterial',
                  'elementType': 'labels',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'arterial',
                  'elementType': 'labels.text.fill',
                  'stylers': {
                    'color': '#525355ff'
                  }
                }, {
                  'featureType': 'arterial',
                  'elementType': 'labels.text.stroke',
                  'stylers': {
                    'color': '#ffffffff'
                  }
                }, {
                  'featureType': 'local',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on',
                    'weight': 1
                  }
                }, {
                  'featureType': 'local',
                  'elementType': 'geometry.fill',
                  'stylers': {
                    'color': '#d8d8d8ff'
                  }
                }, {
                  'featureType': 'local',
                  'elementType': 'geometry.stroke',
                  'stylers': {
                    'color': '#ffffffff'
                  }
                }, {
                  'featureType': 'local',
                  'elementType': 'labels',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'local',
                  'elementType': 'labels.text.fill',
                  'stylers': {
                    'color': '#979c9aff'
                  }
                }, {
                  'featureType': 'local',
                  'elementType': 'labels.text.stroke',
                  'stylers': {
                    'color': '#ffffffff'
                  }
                }, {
                  'featureType': 'railway',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on',
                    'weight': 1
                  }
                }, {
                  'featureType': 'railway',
                  'elementType': 'geometry.fill',
                  'stylers': {
                    'color': '#123c52ff'
                  }
                }, {
                  'featureType': 'railway',
                  'elementType': 'geometry.stroke',
                  'stylers': {
                    'color': '#12223dff'
                  }
                }, {
                  'featureType': 'subway',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on',
                    'weight': 1
                  }
                }, {
                  'featureType': 'subway',
                  'elementType': 'geometry.fill',
                  'stylers': {
                    'color': '#d8d8d8ff'
                  }
                }, {
                  'featureType': 'subway',
                  'elementType': 'geometry.stroke',
                  'stylers': {
                    'color': '#ffffff00'
                  }
                }, {
                  'featureType': 'subway',
                  'elementType': 'labels',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'subway',
                  'elementType': 'labels.text.fill',
                  'stylers': {
                    'color': '#979c9aff'
                  }
                }, {
                  'featureType': 'subway',
                  'elementType': 'labels.text.stroke',
                  'stylers': {
                    'color': '#ffffffff'
                  }
                }, {
                  'featureType': 'continent',
                  'elementType': 'labels',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'continent',
                  'elementType': 'labels.icon',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'continent',
                  'elementType': 'labels.text.fill',
                  'stylers': {
                    'color': '#333333ff'
                  }
                }, {
                  'featureType': 'continent',
                  'elementType': 'labels.text.stroke',
                  'stylers': {
                    'color': '#ffffffff'
                  }
                }, {
                  'featureType': 'city',
                  'elementType': 'labels.icon',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'city',
                  'elementType': 'labels',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'city',
                  'elementType': 'labels.text.fill',
                  'stylers': {
                    'color': '#454d50ff'
                  }
                }, {
                  'featureType': 'city',
                  'elementType': 'labels.text.stroke',
                  'stylers': {
                    'color': '#ffffffff'
                  }
                }, {
                  'featureType': 'town',
                  'elementType': 'labels.icon',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'town',
                  'elementType': 'labels',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'town',
                  'elementType': 'labels.text.fill',
                  'stylers': {
                    'color': '#454d50ff'
                  }
                }, {
                  'featureType': 'town',
                  'elementType': 'labels.text.stroke',
                  'stylers': {
                    'color': '#ffffffff'
                  }
                }, {
                  'featureType': 'road',
                  'elementType': 'geometry.fill',
                  'stylers': {
                    'color': '#12223dff'
                  }
                }, {
                  'featureType': 'poilabel',
                  'elementType': 'labels',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'districtlabel',
                  'elementType': 'labels',
                  'stylers': {
                    'visibility': 'off'
                  }
                }, {
                  'featureType': 'road',
                  'elementType': 'geometry',
                  'stylers': {
                    'visibility': 'on'
                  }
                }, {
                  'featureType': 'road',
                  'elementType': 'labels',
                  'stylers': {
                    'visibility': 'off'
                  }
                }, {
                  'featureType': 'road',
                  'elementType': 'geometry.stroke',
                  'stylers': {
                    'color': '#ffffff00'
                  }
                }, {
                  'featureType': 'district',
                  'elementType': 'labels',
                  'stylers': {
                    'visibility': 'off'
                  }
                }, {
                  'featureType': 'poilabel',
                  'elementType': 'labels.icon',
                  'stylers': {
                    'visibility': 'off'
                  }
                }, {
                  'featureType': 'poilabel',
                  'elementType': 'labels.text.fill',
                  'stylers': {
                    'color': '#2dc4bbff'
                  }
                }, {
                  'featureType': 'poilabel',
                  'elementType': 'labels.text.stroke',
                  'stylers': {
                    'color': '#ffffff00'
                  }
                }, {
                  'featureType': 'manmade',
                  'elementType': 'geometry',
                  'stylers': {
                    'color': '#12223dff'
                  }
                }, {
                  'featureType': 'districtlabel',
                  'elementType': 'labels.text.stroke',
                  'stylers': {
                    'color': '#ffffffff'
                  }
                }, {
                  'featureType': 'entertainment',
                  'elementType': 'geometry',
                  'stylers': {
                    'color': '#ffffffff'
                  }
                }, {
                  'featureType': 'shopping',
                  'elementType': 'geometry',
                  'stylers': {
                    'color': '#12223dff'
                  }
                }
              ]
            }
          },
          series: [
            {
              name: 'Top 5',
              type: 'effectScatter',
              coordinateSystem: 'bmap',
              data: convertData(data.sort(function(a, b) {
                return b.value - a.value
              }).slice(0, 12)),
              symbolSize: function(val) {
                if (val[2] > 100){
                  return val[2] / 20}
                else if (val[2] <= 40){
                  return val[2] }
                else {
                  return val[2]/5 }
              },
              showEffectOn: 'render',
              rippleEffect: {
                period: 4, // 动画时间，值越小速度越快
                brushType: 'fill', // 波纹绘制方式 stroke, fill
                scale: 2 // 波纹圆环最大限制，值越大波纹越大
              },
              hoverAnimation: true,
              label: {
                normal: {
                  formatter: '{b}',
                  position: 'right',
                  show: true
                },
                emphasis: {
                  formatter: '{b}: {@[2]}'
                }
              },
              itemStyle: {
                normal: {
                  color: '#f4e925',
                  shadowBlur: 10,
                  shadowColor: '#333'
                }
              },
              zlevel: 1
            }
          ]
        }
        )
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
  .hot{
    color: #ffffff;
    display:block;
    text-align: center;
    font-size: 30px;
  }
  .map{
    width: 100%;
    height: 100%;
  }
</style>

