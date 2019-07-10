<template>
  <div class="card-list" ref="content">
    <a-list
      :grid="{gutter: 24, lg: 3, md: 2, sm: 1, xs: 1}"
      :dataSource="dataSource"
      :loading="loading"
    >
      <a-list-item slot="renderItem" slot-scope="item">
        <template v-if="item === null">
          <a-button class="new-btn" type="dashed" @click="$refs.modal.add()">
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
              <a @click="$refs.modal.edit(item)">Change</a>
              <a @click="$refs.modal.delete(item)">Delete</a>
            </template>
          </a-card>
        </template>
      </a-list-item>
    </a-list>
    <category-form ref="modal" @create="handleCreate"  @update="handleUpdate" @delete="handleDelete"/>
  </div>
</template>

<script>
import { getCategoryList } from '@/api/product'
import CategoryForm from './CategoryForm'

export default {
  name: 'CategoryList',
  components: {
    CategoryForm,
  },
  data () {
    return {
      description: '产品类别',
      dataSource: [],
      loading: false
    }
  },
  created() {
    this.dataSource.push(null)
    this.fetch()
  },
  methods: {
    fetch() {
      this.loading = true
      getCategoryList().then(res => {
        const { result } = res
        this.dataSource = result
        this.dataSource.unshift(null)
      }).catch((error) => {
        this.$notification['error']({
          message: 'error',
          description: 'get failure',
          duration: 4
        })
      }).finally(() => {
        this.loading = false
      })
    },
    handleCreate (value) {
      this.dataSource.push(value)
      this.sort()
    },  
    handleUpdate (value) {
      this.dataSource = this.dataSource.map(function (f) {
        if (f && f.id === value.id) {
          return value
        } 
        return f
      })
    },
    handleDelete(value) {
      this.fetch()
    }
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
