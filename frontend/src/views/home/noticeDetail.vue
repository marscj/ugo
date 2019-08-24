
<template>
  <a-spin :spinning="loading">
    <a-back-top />
    <a-card>
      <div v-html="data.content" />
    </a-card>
  </a-spin>
</template>

<script>
import { getFrontNotice } from "@/api/notice";

export default {
  loading: false,
  mounted() {
    const id = this.$route.params && this.$route.params.id;
    this.fetch(id);
  },
  data() {
    return {
      data: {
        content: ""
      },
      loading: false
    };
  },
  methods: {
    fetch(id) {
      this.loading = true;
      getFrontNotice(id)
        .then(res => {
          this.data = res.result;
        })
        .finally(() => {
          this.loading = false;
        });
    }
  }
};
</script>
<style>
</style>