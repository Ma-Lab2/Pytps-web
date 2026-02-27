<template>
  <div class="dir-browser">
    <el-input
      v-model="currentPath"
      size="small"
      placeholder="图像目录路径"
      @keyup.enter="browse"
    >
      <template #append>
        <el-button @click="browse" :icon="FolderOpened" />
      </template>
    </el-input>
    <div v-if="parentDir" class="parent-link">
      <el-link type="primary" @click="goUp">..</el-link>
    </div>
    <div v-for="dir in dirs" :key="dir" class="dir-item">
      <el-link type="primary" @click="enterDir(dir)">{{ dir }}/</el-link>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import { FolderOpened } from '@element-plus/icons-vue'
import { useSessionStore } from '../../stores/session'
import api from '../../api/index'

const sessionStore = useSessionStore()
const currentPath = ref('')
const dirs = ref([])
const parentDir = ref(null)

watch(() => sessionStore.imagePath, (val) => {
  currentPath.value = val
  browse()
})

onMounted(() => {
  if (sessionStore.imagePath) {
    currentPath.value = sessionStore.imagePath
    browse()
  }
})

async function browse() {
  try {
    const res = await api.browseDirectory(currentPath.value)
    dirs.value = res.data.dirs
    parentDir.value = res.data.parent
    sessionStore.imagePath = res.data.current
  } catch (e) {
    console.error('Browse failed:', e)
  }
}

function enterDir(dir) {
  currentPath.value = currentPath.value + '/' + dir
  browse()
}

function goUp() {
  if (parentDir.value) {
    currentPath.value = parentDir.value
    browse()
  }
}
</script>

<style scoped>
.dir-browser {
  padding: 8px;
}

.parent-link, .dir-item {
  padding: 2px 8px;
}
</style>
