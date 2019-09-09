<template>
  <a-card>
    <s-table
      ref="table"
      size="default"
      :rowKey="(item) => item.id"
      :columns="columns"
      :data="loadData"
      bordered
    >
      <span slot="image" slot-scope="data">
        <template>
          <img v-if="data" :src="data.image.thumbnail" alt='photo'>
        </template>
      </span>
      <span slot="action" slot-scope="text, data">
        <template>
          <a @click="handleEdit(data)">Edit</a>
        </template>
      </span>
    </s-table>
  </a-card>
</template>

<script>
import { STable } from '@/components'
import { getSourceList } from '@/api/source'

export default {
  name: 'SourceList',
  components: {
    STable
  },
  data () {
    return {
      // 查询参数
      queryParam: {},
      // 表头
      columns: [
        {
          title: '#',
          dataIndex: 'id',
          width: 80
        },
        {
          title: 'Flag',
          dataIndex: 'flag',
        },
        {
          title: 'Title',
          dataIndex: 'title'
        },
        {
          title: 'Image',
          width: 200,
          scopedSlots: { customRender: 'image' }
        },
        {
          title: 'Action',
          dataIndex: 'action',
          width: '150px',
          scopedSlots: { customRender: 'action' }
        }
      ],
      loadData: parameter => {
        return getSourceList(Object.assign(parameter, this.queryParam))
          .then(res => {
            return res.result
          })
      },
    }
  },
  created () {

  },
  methods: {

    handleEdit (record) {
      this.$emit('onEdit', record)
    },
    handleOk () {

    },
  }
}
</script>
