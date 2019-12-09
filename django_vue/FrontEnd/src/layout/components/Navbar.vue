<template>
  <div class="navbar">
    <hamburger
      :is-active="sidebar.opened"
      class="hamburger-container"
      @toggleClick="toggleSideBar"
    />

    <breadcrumb class="breadcrumb-container" />

    <div class="right-menu">
      <el-dropdown class="avatar-container" trigger="click">
        <div class="avatar-wrapper">
          <img :src="require('@/assets/yanghao.png')" class="user-avatar" v-if="status===0"/>
          <img :src="require('@/assets/lijiangnan.jpeg')" class="user-avatar" v-if="status===1"/>
          <i class="el-icon-caret-bottom" />
        </div>
        <el-dropdown-menu slot="dropdown" class="user-dropdown">
          <el-dropdown-item >用户: {{name}}</el-dropdown-item>
          <router-link to="/">
            <el-dropdown-item divided>Home</el-dropdown-item>
          </router-link>
          <el-dropdown-item divided>
            <span style="display:block;" @click="logout">Log Out</span>
          </el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
    <div class="test-container">
      <transition class="inner-container" name="slide" mode="out-in">
        <p class="text" :key="text.id">{{text.val}}</p>
      </transition>
    </div>

  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import Breadcrumb from '@/components/Breadcrumb'
import Hamburger from '@/components/Hamburger'
import axios from 'axios'
const totalDuration = 2000;
var totalnum = 2;
export default {
  components: {
    Breadcrumb,
    Hamburger
  },
  computed: {
    ...mapGetters([
      'sidebar',
      'avatar'
    ]),
    text() {
      return {
        id: this.number,
        val: this.arr[this.number]
      }
    },
  },
  created(){
    //this.Getuser()
  },
  mounted() {
    this.startMove()
    this.Getuser()
  },
  data() {
    return {
      arr: [],
      number: 0,
      name: 'yanghao',
      status: 0
    }
  },
  methods: {
    Getuser() {
      axios.get('/api/get_name').then(response => {
        console.log(response.data['name'])
        console.log(this.status)
        this.name = response.data['name']
        if (this.name === 'yanghao'){
          this.status = 0
        }
        else if (this.name === 'lijiangnan'){
          this.status = 1
        }
      })
    },
    toggleSideBar() {
      this.$store.dispatch('app/toggleSideBar')
    },
    logout() {
      self.location.href = 'http://10.250.40.61:8000'
    },
    startMove() {
      let timer = setTimeout(() => {
        if (this.number === totalnum-1) {
          this.number = 0;
        } else {
          this.number += 1;
        }
        this.startMove();
        this.getdata_abnormal()
      }, totalDuration)
    },
    getdata_abnormal() {
      axios.get('/api/getdata_abnormal').then(response => {
        console.log(response.data)
        this.arr = response.data['data']
        totalnum = response.data['number']
      })
    },
  }
}
</script>

<style lang="scss" scoped>
.navbar {
  height: 50px;
  overflow: hidden;
  position: relative;
  background: #fff;
  box-shadow: 0 1px 4px rgba(0, 21, 41, 0.08);

  .hamburger-container {
    line-height: 46px;
    height: 100%;
    float: left;
    cursor: pointer;
    transition: background 0.3s;
    -webkit-tap-highlight-color: transparent;

    &:hover {
      background: rgba(0, 0, 0, 0.025);
    }
  }


  .breadcrumb-container {
    float: left;
  }

  .right-menu {
    float: right;
    height: 100%;
    line-height: 50px;

    &:focus {
      outline: none;
    }

    .right-menu-item {
      display: inline-block;
      padding: 0 8px;
      height: 100%;
      font-size: 18px;
      color: #5a5e66;
      vertical-align: text-bottom;

      &.hover-effect {
        cursor: pointer;
        transition: background 0.3s;

        &:hover {
          background: rgba(0, 0, 0, 0.025);
        }
      }
    }

    .avatar-container {
      margin-right: 30px;

      .avatar-wrapper {
        margin-top: 5px;
        position: relative;

        .user-avatar {
          cursor: pointer;
          width: 40px;
          height: 40px;
          border-radius: 10px;
        }

        .el-icon-caret-bottom {
          cursor: pointer;
          position: absolute;
          right: -20px;
          top: 25px;
          font-size: 12px;
        }
      }
    }
  }
  .slide-enter-active, .slide-leave-active {
    transition: all 0.5s linear;
  }
  .slide-leave-to {
    transform: translateY(-20px);
  }
  .slide-enter {
    transform: translateY(20px);
  }
  // .test-container {
  //   float: right;
  // }
  .text{
    text-align: center;
    padding-right: 90px;
  }
  .username{
    text-align: left;
    /*padding-right: 10px;*/
  }
}
</style>
