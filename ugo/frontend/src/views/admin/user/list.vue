<template>
  <a-card :bordered="false" v-action:query>
    <div class="table-page-search-wrapper">
      <a-form layout="inline">
        <a-row :gutter="48">
          <a-col :md="8" :sm="24">
            <a-form-item label="角色ID">
              <a-input placeholder="请输入" />
            </a-form-item>
          </a-col>
          <a-col :md="8" :sm="24">
            <a-form-item label="状态">
              <a-select placeholder="请选择" default-value="0">
                <a-select-option value="0">全部</a-select-option>
                <a-select-option value="1">关闭</a-select-option>
                <a-select-option value="2">运行中</a-select-option>
              </a-select>
            </a-form-item>
          </a-col>
          <a-col :md="8" :sm="24">
            <span class="table-page-search-submitButtons">
              <a-button type="primary">查询</a-button>
              <a-button style="margin-left: 8px">重置</a-button>
            </span>
          </a-col>
        </a-row>
      </a-form>
    </div>

    <s-table row-key="id" size="default" :columns="columns" :data="loadData" bordered>
      <span slot="active" slot-scope="text">
        <a-checkbox :checked="text" disabled />
      </span>
      <span slot="staff" slot-scope="text">
        <a-checkbox :checked="text" disabled />
      </span>
      <span slot="action" slot-scope="text, record">
        <a v-action:edit @click="handleEdit(record)">编辑</a>
        <a-divider type="vertical" />
        <a v-action:edit @click="handleEdit(record)">修改密码</a>
      </span>
    </s-table>

    <a-modal title="操作" style="top: 20px;" width="90%" v-model="visible">
      <template slot="footer">
        <a-button key="back" @click="visible=false">Return</a-button>
        <a-button key="submit" type="primary" :loading="loading" @click="handleOk">Submit</a-button>
      </template>
      <a-form :form="form">
        <a-form-item
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
          label="UserID"
          validateStatus="success"
        >
          <a-input v-model="mdl.id" disabled />
        </a-form-item>

        <a-form-item
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
          label="Username"
          validateStatus="success"
        >
          <a-input v-model="mdl.username" disabled />
        </a-form-item>

        <a-form-item :labelCol="labelCol" :wrapperCol="wrapperCol" label="Price Level">
          <a-input-number
            v-model="mdl.price_level"
            :min="1"
            :max="5"
            :precision="0"
            style="width:200px;"
          />
        </a-form-item>

        <a-form-item :labelCol="labelCol" :wrapperCol="wrapperCol" label="Balance">
          <a-input-number
            v-model="mdl.balance"
            :min="0.0"
            :defaultValue="0.0"
            :precision="2"
            :step="0.5"
            style="width:200px;"
          />
        </a-form-item>

        <a-form-item :labelCol="labelCol" :wrapperCol="wrapperCol" label="Role">
          <a-select
            :value="mdl.role_id"
            :defaultActiveFirstOption="false"
            :showArrow="false"
            :filterOption="false"
            allowClear
            @change="handleRoleChange"
            notFoundContent="Not Found."
            style="width:200px;"
          >
            <a-select-option v-for="d in roleOption" :key="d.id" :value="d.id">{{d.name}}</a-select-option>
          </a-select>
        </a-form-item>

        <a-form-item :labelCol="labelCol" :wrapperCol="wrapperCol" label="Status">
          <a-switch v-model="mdl.is_active" checkedChildren="Enable" unCheckedChildren="Disable(禁用登陆)"></a-switch>
        </a-form-item>
      </a-form>
    </a-modal>
  </a-card>
</template>

<script>
import { STable } from "@/components";
import { getUserList, updateUser } from "@/api/manage";
import { getRoleList } from "@/api/manage";

export default {
  name: "UserList",
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
      form: {
        role_id: 0
      },
      mdl: {
        role: {}
      },
      // 查询参数
      queryParam: {},
      // 表头
      columns: [
        {
          title: "ID",
          dataIndex: "id",
          width: "100px"
        },
        {
          title: "Username",
          dataIndex: "username"
        },
        {
          title: "Role",
          dataIndex: "role.name"
        },
        {
          title: "Status",
          dataIndex: "is_active",
          scopedSlots: { customRender: "active" }
        },
        {
          title: "Balance",
          dataIndex: "balance"
        },
        {
          title: "Price Levle",
          dataIndex: "price_level",
          width: "120px",
          customRender: (text, row, index) => {
            return <span>Level {text}</span>;
          }
        },
        {
          title: "操作",
          width: "150px",
          dataIndex: "action",
          scopedSlots: { customRender: "action" }
        }
      ],
      // 加载数据方法 必须为 Promise 对象
      loadData: parameter => {
        return getUserList(parameter).then(res => {
          return res.result;
        });
      },

      pagination: {},
      roleOption: [],
      loading: false
    };
  },
  created() {
    this.handleRoleSearch();
  },
  methods: {
    handleRoleSearch() {
      getRoleList().then(res => {
        const { result } = res;
        this.roleOption = result;
      });
    },
    handleRoleChange(value) {
      if (value) {
        this.mdl.role_id = value;
      } else {
        this.mdl.role_id = null;
      }
    },
    handleEdit(record) {
      this.mdl = Object.assign({}, record);
      this.visible = true;
    },
    handleChangeStatus(e) {
      this.mdl.is_active = e.target.checked;
    },
    handleChangeStaff(e) {
      this.mdl.is_staff = e.target.checked;
    },
    handleOk() {
      this.loading = true;
      updateUser(this.mdl.id, this.mdl)
        .then(res => {
          this.visible = false;
        })
        .finally(() => {
          this.loading = false;
        });
    }
  }
};
</script>
