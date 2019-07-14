<template>
  <list-view :loading="loading" :data="data" align="center" @onClick="onClick" @onSearch="onSearch"/>
</template>

<script>
import ListView from './ListView'
import PageView from '@/views/layouts/PageView'
import { getProductList } from '@/api/product'

export default {
  components: {
    ListView,
    PageView
  },
  data() {
    return {
      data: [],
      loading: false,
      description: ' ',
      extraImage: require('@/assets/car.svg'),
    }
  },
  mounted() {
    this.fetch(null)
  },
  methods: {
    fetch(search) {
      this.loading = true
      getProductList({category: 4, search: search}).then((res) => {
        const { result } = res
        this.data = result
      }).finally(() => {
        this.loading = false
      })
    },
    onClick(data) {
    },
    onSearch(value) {
      this.fetch(value)
    }
  },
}
</script>