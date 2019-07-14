<template>
  <div class="content">
    <div class="page-header-index-wide">
      <a-card>
        <page-view :loading="loading" :data="data"/>
      </a-card>
    </div>
  </div>
    
</template>

<script>
import PageView from './PageView'
import { getProductList } from '@/api/product'

export default {
  components: {
    PageView
  },
  data() {
    return {
      data: [],
      loading: false
    }
  },
  mounted() {
    this.fetch()
  },
  methods: {
    fetch() {
      this.loading = true
      getProductList().then((res) => {
        const { result } = res
        this.data = result
      }).finally(() => {
        this.loading = false
      })
    }
  },
}
</script>

<style lang="less" scoped>
  .content {
    margin: 24px 24px 0;
    .link {
      margin-top: 16px;
      &:not(:empty) {
        margin-bottom: 16px;
      }
      a {
        margin-right: 32px;
        height: 24px;
        line-height: 24px;
        display: inline-block;
        i {
          font-size: 24px;
          margin-right: 8px;
          vertical-align: middle;
        }
        span {
          height: 24px;
          line-height: 24px;
          display: inline-block;
          vertical-align: middle;
        }
      }
    }
  }
</style>