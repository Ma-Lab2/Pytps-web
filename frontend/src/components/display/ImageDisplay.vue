<template>
  <div class="image-display">
    <div v-if="analysisStore.imagePng" class="image-container">
      <img :src="'data:image/png;base64,' + analysisStore.imagePng" alt="TPS Image" class="tps-image" />
    </div>
    <el-empty v-else description="请选择图像文件" :image-size="80" />
  </div>
</template>

<script setup>
import { useAnalysisStore } from '../../stores/analysis'

const analysisStore = useAnalysisStore()
</script>

<style scoped>
.image-display {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f5f5f5;
  border: 1px solid #e4e7ed;
  border-radius: 4px;
  overflow: hidden;
}

.image-container {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.tps-image {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}
</style>
