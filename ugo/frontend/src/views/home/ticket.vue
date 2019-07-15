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
      extraImage: require('@/assets/ticket.svg'),
    }
  },
  mounted() {
    this.fetch(null)
  },
  methods: {
    fetch(search) {
      this.loading = true
      getProductList({category: 1, search: search, sorter:'-id'}).then((res) => {
        const { result } = res
        this.data = result
      }).finally(() => {
        this.loading = false
      })
    },
    onClick(data) {
      console.log(data)
      this.$router.push({name: 'TicketDetail', params: { id: data.id }})
    },
    onSearch(value) {
      this.fetch(value)
    }
  },
}
</script>