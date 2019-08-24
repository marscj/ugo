<template>
  <div>
    <a-back-top />
    <a-card>
      <a-list
        itemLayout="vertical"
        size="large"
        :pagination="pagination"
        :dataSource="listData"
        :loading="loading"
      >
        <a-list-item slot="renderItem" slot-scope="item" key="item.id">
          <a-list-item-meta :description="item.subtitle">
            <a slot="title" :href="getUrl(item.id)">{{item.title}}</a>
          </a-list-item-meta>
          {{item.create_at | moment('YYYY-MM-DD HH:mm:ss')}}
        </a-list-item>
      </a-list>
    </a-card>
  </div>
</template>

<script>
import { getFrontNoticeList } from "@/api/notice";

export default {
  loading: false,
  created() {
    this.fetch();
  },
  data() {
    return {
      listData: [],
      loading: false,
      pageNo: 1,
      pageSize: 20,
      pagination: {
        onChange: (page, size) => {
          this.pageNo = page;
          this.pageSize = size;
        },
        pageSize: 20
      }
    };
  },
  methods: {
    fetch() {
      this.loading = true;
      getFrontNoticeList({
        pageNo: this.pageNo,
        pageSize: this.pageSize
      })
        .then(res => {
          this.listData = res.result.data;
        })
        .finally(() => {
          this.loading = false;
        });
    },
    getUrl(id) {
      return `/home/notice/${id}`;
    }
  }
};
</script>
<style>
</style>