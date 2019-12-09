<template>
  <div class="block">
    <span class="demonstration">默认</span>
    <el-date-picker
      v-model="value1"
      type="daterange"
      range-separator="至"
      @change="getMyDateTime()"
      start-placeholder="开始日期"
      end-placeholder="结束日期"
      value-format="yyyyMMdd">
    </el-date-picker>
    <h1>site : {{value1}}</h1>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'datepicker',
  data () {
    return {
      value1: ''
    }
  },
  methods: {
    getMyDateTime () {
      axios.get('/api/get_date', {
        params: {
          'date1': this.value1[0],
          'date2': this.value1[1],
        }
      }).then()
    }
  }
}
</script>

<style scoped>

</style>
