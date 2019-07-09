<template>
  <a-card :bordered="false">
    <component @onEdit="handleEdit" @onGoBack="handleGoBack" :record="data" :is="currentComponet"></component>
  </a-card>
</template>

<script>

import ATextarea from 'ant-design-vue/es/input/TextArea'
import AInput from 'ant-design-vue/es/input/Input'
// 动态切换组件
import List from '@/views/admin/product/product/table/List'
import Edit from '@/views/admin/product/product/table/Edit'

export default {
  name: 'TableListWrapper',
  components: {
    AInput,
    ATextarea,
    List,
    Edit
  },
  data () {
    return {
      currentComponet: 'List',
      data: {}
    }
  },
  created () {

  },
  methods: {
    handleEdit (data) {
      this.data = data || ''
      this.currentComponet = 'Edit'
    },
    handleGoBack () {
      this.data = ''
      this.currentComponet = 'List'
    }
  },
  watch: {
    '$route.path' () {
      this.data = {}
      this.currentComponet = 'List'
    }
  }
}
</script>
