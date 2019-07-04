<template>
  <div class="card-list" ref="content">
    <a-list
      :grid="{gutter: 24, lg: 3, md: 2, sm: 1, xs: 1}"
      :dataSource="dataSource"
    >
      <a-list-item slot="renderItem" slot-scope="item">
        <template v-if="item === null">
          <a-button class="new-btn" type="dashed" @click="$refs.createModal.add()">
            <a-icon type="plus"/>
            Add Category
          </a-button>
        </template>
        <template v-else>
          <a-card :hoverable="true">
            <a-card-meta>
              <div style="margin-bottom: 3px" slot="title">{{ item.name }}</div>
            </a-card-meta>
            <template class="ant-card-actions" slot="actions">
              <a @click="$refs.createModal.edit(item)">change</a>
              <a>delete</a>
            </template>
          </a-card>
        </template>
      </a-list-item>
    </a-list>
    <category-form ref="createModal" @ok="handleOk" />
  </div>
</template>

<script>
import { getCategoryList } from '@/api/product'
import CategoryForm from './CategoryForm'

export default {
  name: 'CardList',
  components: {
    CategoryForm,
  },
  data () {
    return {
      description: '产品类别',
      dataSource: [],
    }
  },
  created() {
    this.dataSource.push(null)
    this.fetch()
  },
  methods: {
    fetch() {
      getCategoryList().then(res => {
        const { result } = res
        this.dataSource = result
        this.dataSource.unshift(null)
      })
    },
    handleOk (value) {
      
    },
  },
}
</script>

<style lang="less" scoped>
  .card-avatar {
    width: 48px;
    height: 48px;
    border-radius: 48px;
  }

  .ant-card-actions {
    background: #f7f9fa;
    li {
      float: left;
      text-align: center;
      margin: 12px 0;
      color: rgba(0, 0, 0, 0.45);
      width: 50%;

      &:not(:last-child) {
        border-right: 1px solid #e8e8e8;
      }

      a {
        color: rgba(0, 0, 0, .45);
        line-height: 22px;
        display: inline-block;
        width: 100%;
        &:hover {
          color: #1890ff;
        }
      }
    }
  }

  .new-btn {
    background-color: #fff;
    border-radius: 2px;
    width: 100%;
    height: 116px;
  }

  .meta-content {
    position: relative;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    height: 64px;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
  }
</style>
