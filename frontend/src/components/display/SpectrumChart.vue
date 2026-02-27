<template>
  <div class="spectrum-chart" ref="chartContainer">
    <v-chart v-if="option" :option="option" autoresize style="width: 100%; height: 100%;" @click="onChartClick" />
    <el-empty v-else description="暂无能谱数据" :image-size="60" />
  </div>
</template>

<script setup>
import { computed, ref } from 'vue'
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { LineChart } from 'echarts/charts'
import {
  TitleComponent, TooltipComponent, GridComponent,
  LegendComponent, ToolboxComponent, DataZoomComponent
} from 'echarts/components'
import VChart from 'vue-echarts'
import { useAnalysisStore } from '../../stores/analysis'
import { useSessionStore } from '../../stores/session'
import wsClient from '../../api/websocket'

use([
  CanvasRenderer, LineChart,
  TitleComponent, TooltipComponent, GridComponent,
  LegendComponent, ToolboxComponent, DataZoomComponent,
])

const analysisStore = useAnalysisStore()
const sessionStore = useSessionStore()
const chartContainer = ref(null)

const option = computed(() => {
  const data = analysisStore.spectrumData
  if (!data || !data.energy) return null

  const series = [
    {
      name: '能谱',
      type: 'line',
      data: data.energy.map((e, i) => [e, data.dNdE[i]]),
      smooth: false,
      lineStyle: { width: 1.5 },
      symbol: 'none',
    },
  ]

  if (data.noise_energy) {
    series.push({
      name: '噪声',
      type: 'line',
      data: data.noise_energy.map((e, i) => [e, data.noise_dNdE[i]]),
      smooth: false,
      lineStyle: { width: 1, type: 'dashed' },
      symbol: 'none',
    })
  }

  // Add fit curve if available
  const fit = analysisStore.fitResult
  if (fit && fit.success && fit.fit_curve) {
    series.push({
      name: `拟合 (kT=${fit.kT.toFixed(2)} MeV)`,
      type: 'line',
      data: fit.fit_curve.energy.map((e, i) => [e, fit.fit_curve.dNdE[i]]),
      smooth: true,
      lineStyle: { width: 2, color: '#e6a23c' },
      symbol: 'none',
    })
  }

  return {
    title: { text: '能谱 dN/dE', left: 'center', textStyle: { fontSize: 14 } },
    tooltip: {
      trigger: 'axis',
      formatter: params => {
        const p = params[0]
        return `E = ${p.value[0].toFixed(2)} MeV<br/>dN/dE = ${p.value[1].toExponential(2)}`
      },
    },
    legend: { bottom: 0 },
    grid: { left: 80, right: 30, top: 40, bottom: 40 },
    xAxis: {
      type: 'value',
      name: 'E (MeV)',
      min: sessionStore.params.specEmin,
      max: sessionStore.params.specEmax,
    },
    yAxis: {
      type: 'log',
      name: 'dN/dE',
      min: sessionStore.params.specdNdEmin,
      max: sessionStore.params.specdNdEmax,
    },
    toolbox: {
      feature: {
        dataZoom: { yAxisIndex: 'none' },
        restore: {},
        saveAsImage: {},
      },
    },
    dataZoom: [
      { type: 'inside', xAxisIndex: 0 },
    ],
    series,
  }
})

function onChartClick(params) {
  if (params.value) {
    const energy = params.value[0]
    wsClient.setCursor(energy)
  }
}
</script>

<style scoped>
.spectrum-chart {
  flex: 1;
  min-height: 250px;
  border: 1px solid #e4e7ed;
  border-radius: 4px;
  background: white;
}
</style>
