<template>
  <a-card :bordered="false" v-action:query>
    <div class="table-operator">
      <a-button v-action:add type="primary" icon="plus" @click="handleCreate">Add</a-button>
    </div>

    <s-table
      ref="table"
      size="default"
      :rowKey="(item) => item.id"
      :columns="columns"
      :data="loadData"
      fixed
    >
      <span slot="create_at" slot-scope="text">
        <template>
          <span>{{text | moment('YYYY-MM-DD HH:mm')}}</span>
        </template>
      </span>
      <span slot="action" slot-scope="text, data">
        <template>
          <router-link v-action:edit :to="{ name: 'NoticeEdit', params: { id: data.id } }">Edit</router-link>
          <a-divider v-action:edit type="vertical" />
        </template>
        <a v-action:delete @click="handleDelete(data)">Delete</a>
      </span>
    </s-table>
  </a-card>
</template>

<script>
import { STable, Ellipsis } from "@/components";
import { getNoticeList, deleteNotice } from "@/api/notice";

export default {
  name: "NoticeList",
  components: {
    STable,
    Ellipsis
  },
  data() {
    return {
      columns: [
        {
          key: "#",
          title: "#",
          dataIndex: "id",
          width: 100
        },
        {
          key: "1",
          title: "Title",
          dataIndex: "title"
        },
        {
          key: "2",
          title: "SubTitle",
          dataIndex: "subtitle"
        },
        {
          key: "3",
          title: "CreateTime",
          dataIndex: "create_at",
          scopedSlots: { customRender: "create_at" }
        },
        {
          key: "action",
          title: "操作",
          dataIndex: "action",
          scopedSlots: { customRender: "action" },
          width: '140px'
        }
      ],
      loadData: parameter => {
        return getNoticeList(Object.assign(parameter, this.queryParam)).then(
          res => {
            return res.result;
          }
        );
      }
    };
  },
  methods: {
    handleCreate(data) {
      this.$router.push({
        name: "NoticeCreate"
      });
    },
    handleDelete(data) {
      var _this = this;

      _this.$confirm({
        title: "alert",
        content: `Are you sure delete?`,
        okText: "delete",
        okType: "danger",
        cancelText: "cancle",
        onOk() {
          _this.$refs.table.localLoading = true;
          return deleteNotice(data.id)
            .then(res => {
              _this.$refs.table.refresh(true);
            })
            .finally(() => {
              _this.$refs.table.localLoading = false;
            });
        }
      });
    }
  }
};
</script>
