<template>
  <a-card :bordered="false" v-action:query>
    <s-table
      ref="table"
      size="default"
      :rowKey="(item) => item.id"
      :columns="columns"
      :data="loadData"
      fixed
    >
      <span slot="remark" slot-scope="text" style="word-warp:break-word;word-break:break-all">
        <ellipsis :length="200" tooltip>{{ text }}</ellipsis>
      </span>
      <span slot="variant" slot-scope="text" style="word-warp:break-word;word-break:break-all">
        <ellipsis :length="60" tooltip>{{ text }}</ellipsis>
      </span>
      <span
        slot="customer_info"
        slot-scope="text"
        style="word-warp:break-word;word-break:break-all"
      >
        <ellipsis :length="160" tooltip>{{ text }}</ellipsis>
      </span>
      <span
        slot="customer_contact"
        slot-scope="text"
        style="word-warp:break-word;word-break:break-all"
      >
        <ellipsis :length="160" tooltip>{{ text }}</ellipsis>
      </span>
      <span slot="create_at" slot-scope="text">
        <template>
          <span>{{text | moment('YYYY-MM-DD HH:mm')}}</span>
        </template>
      </span>
      <span slot="action" slot-scope="text, data">
        <div v-action:edit>
          <router-link :to="{ name: 'OrderEdit', params: { id: data.id } }">Edit</router-link>
        </div>
      </span>
    </s-table>
  </a-card>
</template>

<script>
import { STable, Ellipsis } from "@/components";
import { getNotice } from "@/api/notice";

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
          dataIndex: "title",
        },
        {
          key: "2",
          title: "SubTitle",
          dataIndex: "subtitle",
        },
        {
          key: "3",
          title: "CreateTime",
          dataIndex: "create_at",
        },
        {
          key: "action",
          title: "操作",
          dataIndex: "action",
          scopedSlots: { customRender: "action" },
          width: 100,
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
    }
  }
};
</script>
