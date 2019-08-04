<template>
  <a-card :bordered="false" v-action:query>
    <s-table :columns="columns" :data="loadData" :rowKey="(item) => item.id" bordered>
      <span slot="actions" slot-scope="text, record">
        <a-tag v-for="(action, index) in record.actionList" :key="index">{{ action.describe }}</a-tag>
      </span>
    </s-table>
  </a-card>
</template>

<script>
import { STable } from "@/components";
import { getPermissions } from "@/api/manage";

export default {
  name: "PermissionList",
  components: {
    STable
  },
  data() {
    return {
      visible: false,
      labelCol: {
        xs: { span: 24 },
        sm: { span: 5 }
      },
      wrapperCol: {
        xs: { span: 24 },
        sm: { span: 16 }
      },
      form: null,
      mdl: {},

      // 高级搜索 展开/关闭
      advanced: false,
      // 查询参数
      queryParam: {},
      // 表头
      columns: [
        {
          title: "#",
          dataIndex: "id",
          width: "80px"
        },
        {
          title: "权限名称",
          dataIndex: "permissionName"
        },
        {
          title: "可操作权限",
          dataIndex: "actions",
          scopedSlots: { customRender: "actions" }
        }
      ],
      // 向后端拉取可以用的操作列表
      permissionList: null,
      // 加载数据方法 必须为 Promise 对象
      loadData: parameter => {
        return getPermissions(parameter).then(res => {
          const result = res.result;
          result.data.map(permission => {
            permission.actionList = permission.actionEntitySet;
            return permission;
          });
          return result;
        });
      }
    };
  }
};
</script>
