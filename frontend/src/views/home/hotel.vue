<template>
  <list-view :loading="loading" :data="data" @onClick="onClick" @onSearch="onSearch" align="center"/>
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
      data: {
        data: []
      },
      loading: false,
      description: ' ',
      extraImage: require('@/assets/hotel.svg'),
    }
  },
  methods: {
    onFetch(search, pagination) {
      this.loading = true
      getProductList({category: 5, search: search, sorter:'sort_by', pageNo: pagination.pageNo, pageSize:pagination.pageSize}).then((res) => {
        const { result } = res
        this.data = result
      }).finally(() => {
        this.loading = false
      })
    },
    onSearch(value, pagination) {
      this.onFetch(value, pagination)
    },
    onClick(data) {
      this.$router.push({name: 'HotelDetail', params: { id: data.id }})
    },
  },
}
</script>