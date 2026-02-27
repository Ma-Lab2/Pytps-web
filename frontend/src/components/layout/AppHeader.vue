<template>
  <el-header class="app-header">
    <div class="header-left">
      <h1 class="title">PyTPS Web</h1>
      <el-tag type="info" size="small">Thomson Parabola Spectrometer</el-tag>
    </div>
    <div class="header-center">
      <el-radio-group v-model="sessionStore.mode" size="small">
        <el-radio-button value="offline">离线分析</el-radio-button>
        <el-radio-button value="batch">批处理</el-radio-button>
        <el-radio-button value="online">在线模式</el-radio-button>
      </el-radio-group>
    </div>
    <div class="header-right">
      <el-tag :type="sessionStore.connected ? 'success' : 'danger'" size="small">
        {{ sessionStore.connected ? '已连接' : '未连接' }}
      </el-tag>
      <el-tag v-if="sessionStore.computing" type="warning" size="small">计算中...</el-tag>
    </div>
  </el-header>
</template>

<script setup>
import { useSessionStore } from '../../stores/session'

const sessionStore = useSessionStore()
</script>

<style scoped>
.app-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #2c3e50;
  color: white;
  height: 50px;
  padding: 0 20px;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.title {
  font-size: 18px;
  font-weight: bold;
}

.header-right {
  display: flex;
  gap: 8px;
}
</style>
