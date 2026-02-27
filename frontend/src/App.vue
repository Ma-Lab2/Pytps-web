<template>
  <el-container class="app-container">
    <AppHeader />
    <el-container class="main-content">
      <LeftPanel />
      <RightPanel />
    </el-container>
  </el-container>
</template>

<script setup>
import AppHeader from './components/layout/AppHeader.vue'
import LeftPanel from './components/layout/LeftPanel.vue'
import RightPanel from './components/layout/RightPanel.vue'
import { useSessionStore } from './stores/session'
import { onMounted } from 'vue'

const sessionStore = useSessionStore()

onMounted(() => {
  sessionStore.initialize()
})
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html, body, #app {
  height: 100%;
  font-family: 'Microsoft YaHei', 'Helvetica Neue', Helvetica, Arial, sans-serif;
}

.app-container {
  height: 100vh;
  flex-direction: column;
}

.main-content {
  flex: 1;
  overflow: hidden;
}
</style>
