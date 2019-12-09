<template>
  <el-table
    :data="tableData"
    class="Tabel"
    >
    <el-table-column
      prop="id"
      label="Rec_id"
      width="auto"
      align="center">
    </el-table-column>
    <el-table-column
      prop="date"
      label="时间"
      sortable
      width="auto"
      align="center">
    </el-table-column>
    <el-table-column
      prop="address"
      label="所在街道"
      width="auto"
      align="center">
    </el-table-column>
    <el-table-column
      prop="type"
      label="问题类型"
      width="auto"
      column-key="type"
      :filters="[{text: '道路破损', value: '道路破损'},
      {text: '其他区域堆放施工废弃料', value: '其他区域堆放施工废弃料'},
      {text: '下水井盖', value: '下水井盖'},
      {text: '公共交通管理', value: '公共交通管理'},
      {text: '无照经营游商', value: '无照经营游商'},
      {text: '工业红线内噪声', value: '工业红线内噪声'},
      {text: '工业废气', value: '工业废气'},
      {text: '饲养宠物家禽扰民', value: '饲养宠物家禽扰民'},
      {text: '店外经营', value: '店外经营'},
      {text: '城市管理', value: '城市管理'},
      {text: '超时施工', value: '超时施工'}]"
      :filter-method="filterType"
      align="center"
    >
    </el-table-column>
    <el-table-column
      prop="from"
      label="问题来源"
      width="auto"
      align="center">
    </el-table-column>
    <el-table-column
      fixed="right"
      label="操作"
      width="200">
      <template slot-scope="scope">
        <el-button
          @click.native.prevent="complete(scope.$index, tableData)"
          type="text"
          size="large">
          结办完成
        </el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
import axios from 'axios'

var i = 0
const totalDuration = 500;

export default {
  data() {
    return {
      tableData: [{
        id: '无',
        date: '无',
        address: '无',
        type: '无',
        from: '无'
      }]
      // tableData: [{
      //   id: 120901,
      //   date: '2018-11-02',
      //   address: '龙田街道',
      //   type: '道路破损',
      //   from: '@12356'
      // }, {
      //   id: 120903,
      //   date: '2018-11-03',
      //   address: '龙田街道',
      //   type: '其他区域堆放施工废弃料',
      //   from: '@12356'
      // }, {
      //   id: 120903,
      //   date: '2018-11-04',
      //   address: '龙田街道',
      //   type: '下水井盖',
      //   from: '@12356'
      // }, {
      //   id: 120903,
      //   date: '2018-11-05',
      //   address: '龙田街道',
      //   type: '公共交通管理',
      //   from: '@12356'
      // }, {
      //   id: 120903,
      //   date: '2018-11-06',
      //   address: '龙田街道',
      //   type: '工业红线内噪声',
      //   from: '@12356'
      // }, {
      //   id: 120903,
      //   date: '2018-11-07',
      //   address: '龙田街道',
      //   type: '工业废气',
      //   from: '@12356'
      // }, {
      //   id: 120903,
      //   date: '2018-10-02',
      //   address: '龙田街道',
      //   type: '工业废气',
      //   from: '@12356'
      // }, {
      //   id: 120903,
      //   date: '2019-11-02',
      //   address: '龙田街道',
      //   type: '饲养宠物家禽扰民',
      //   from: '@12356'
      // }, {
      //   id: 120903,
      //   date: '2018-11-09',
      //   address: '龙田街道nm',
      //   type: '无照经营游商',
      //   from: '@12356'
      // }, {
      //   id: 120903,
      //   date: '2018-11-09',
      //   address: '龙田街道nm',
      //   type: '店外经营',
      //   from: '@12356'
      // }, {
      //   id: 120903,
      //   date: '2018-11-09',
      //   address: '龙田街道nm',
      //   type: '城市管理',
      //   from: '@12356'
      // }, {
      //   id: 120903,
      //   date: '2018-11-09',
      //   address: '龙田街道nmd',
      //   type: '超时施工',
      //   from: '@12356'
      // }, {
      //   id: 120903,
      //   date: '2018-11-09',
      //   address: '龙田街道dnm',
      //   type: '超时施工',
      //   from: '@12356'
      // }, {
      //   id: 120903,
      //   date: '2018-11-11',
      //   address: '龙田街道ndm',
      //   type: '超时施工',
      //   from: '@12356'
      // }, {
      //   id: 120903,
      //   date: '2018-11-10',
      //   address: '龙田街道nddm',
      //   type: '杀人放火',
      //   from: '@12356'
      // }]
    }
  },
  created() {
    this.getdata()
  },
  mounted() {
    this.getdata(),
    this.startMove()
  },
  methods: {
    complete(index, rows) {
      this.$confirm('此操作将使问题结办状态改为已结办, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        axios.get('/api/finish_rec_id', {
          params: {
            'rec_id': this.tableData[index].id,
          }
        }).then(response => { this.getdata() })
        this.$message({
          type: 'success',
          message: '更改成功!'
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '取消更改'
        })
      })
    },
    filterType(value, row) {
      return row.type === value
    },
    startMove() {
      let timer = setTimeout(() => {
        this.startMove();
        this.getdata();
      }, totalDuration)
    },
    getdata() {
      axios.get('/api/get_abnormal_form').then(response => {
        var tmp = response.data.cnt
        if (tmp > 200) {
          tmp = 200
        }
        for (i = 0; i < tmp; i++) {
          this.tableData[i] = {
            id: response.data.REC_ID[i],
            date: response.data.CREATE_TIME[i],
            address: response.data.STREET_NAME[i],
            type: response.data.SUB_TYPE_NAME[i],
            from: response.data.EVENT_SRC_NAME[i]
          }
        }
      })
    }
  }
}
</script>

<style scoped>
.Tabel {
  background: #031f2d;
  top: 5%;
  bottom: 5%;
  margin: 0 auto;
  width: 100%;
  font-size: 15px;
}
</style>

