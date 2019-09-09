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
            <span class="table-page-search-submitButtons">
              <a-button type="primary">查询</a-button>
              <a-button style="margin-left: 8px">重置</a-button>
            </span>
          </a-col>
        </a-row>
      </a-form>
    </div>

    <div class="table-operator">
      <a-button v-action:add type="primary" icon="plus" @click="handleCreate">Add</a-button>
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
        <a v-action:edit @click="handleChangePassword(record)">修改密码</a>
      </span>
    </s-table>

    <a-modal :title="isEdit ? 'Edit' : 'Create'" style="top: 20px;" width="90%" v-model="visible">
      <template slot="footer">
        <a-button key="back" @click="visible=false">Return</a-button>
        <a-button
          key="submit"
          type="primary"
          :loading="loading"
          @click="isEdit ? updateForm() : createForm()"
        >Submit</a-button>
      </template>
      <a-form :form="mdl">
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
          :required="true"
          :validate-status="help.username == null || help.username === '' ?  null : 'error'"
          :help="help.username"
        >
          <a-input v-model="mdl.username" :disabled="isEdit" />
        </a-form-item>

        <a-form-item
          v-if="!isEdit"
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
          label="Password"
          :required="true"
          :validate-status="help.password == null || help.password === '' ?  null : 'error'"
          :help="help.password"
        >
          <a-input size="large" type="password" autocomplete="false" v-model="mdl.password">
            <a-icon slot="prefix" type="lock" :style="{ color: 'rgba(0,0,0,.25)' }" />
          </a-input>
        </a-form-item>

        <a-form-item
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
          label="Price Level"
          :required="true"
          :validate-status="help.price_level == null || help.price_level === '' ?  null : 'error'"
          :help="help.price_level"
        > 
        <a-select v-model="mdl.price_level">
          <a-select-option key="0" :value="1">Level 1</a-select-option>
          <a-select-option key="1" :value="2">Level 2</a-select-option>
          <a-select-option key="2" :value="3">Level 3</a-select-option>
          <a-select-option key="3" :value="4">Level 4</a-select-option>
          <a-select-option key="4" :value="5">Level 5</a-select-option>
        </a-select>
        </a-form-item>

        <a-form-item
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
          label="Balance"
          :required="true"
          :validate-status="help.balance == null || help.balance === '' ?  null : 'error'"
          :help="help.balance"
        >
          <a-input-number
            v-model="mdl.balance"
            :min="0.0"
            :defaultValue="0.0"
            :precision="2"
            :step="0.5"
            style="width:200px;"
          />
        </a-form-item>

        <a-form-item
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
          label="Role"
          :validate-status="help.role_id == null || help.role_id === '' ?  null : 'error'"
          :help="help.role_id"
        >
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

        <a-form-item
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
          label="Status"
          :required="true"
          :validate-status="help.is_active == null || help.is_active === '' ?  null : 'error'"
          :help="help.is_active"
        >
          <a-switch
            v-model="mdl.is_active"
            checkedChildren="Enable"
            unCheckedChildren="Disable(禁用登陆)"
          ></a-switch>
        </a-form-item>

        <a-form-item
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
          label="Staff"
          :required="true"
          :validate-status="help.is_staff == null || help.is_staff === '' ?  null : 'error'"
          :help="help.is_staff"
        >
          <a-switch
            v-model="mdl.is_staff"
            checkedChildren="Enable"
            unCheckedChildren="Disable"
          ></a-switch>
        </a-form-item>

      </a-form>
    </a-modal>

    <a-modal title="修改密码" width="600px" v-model="visible_password">
      <template slot="footer">
        <a-button key="back" @click="visible_password=false">Return</a-button>
        <a-button key="submit" type="primary" :loading="loading" @click="changePassword">Submit</a-button>
      </template>
      <a-form :form="mdl">
        <a-form-item
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
          label="New Password"
          :required="true"
          :validate-status="help.new_password == null || help.new_password === '' ?  null : 'error'"
          :help="help.new_password"
        >
          <a-input size="large" type="password" autocomplete="false" v-model="mdl.new_password">
            <a-icon slot="prefix" type="lock" :style="{ color: 'rgba(0,0,0,.25)' }" />
          </a-input>
        </a-form-item>
      </a-form>
    </a-modal>
  </a-card>
</template>

<script>
import { STable } from "@/components";
import {
  getUserList,
  updateUser,
  createUser,
  changePassword
} from "@/api/manage";
import { getRoleList } from "@/api/manage";
import { checkError } from "@/views/utils/error";

export default {
  name: "UserList",
  components: {
    STable
  },
  data() {
    return {
      labelCol: {
        xs: { span: 24 },
        sm: { span: 5 }
      },
      wrapperCol: {
        xs: { span: 24 },
        sm: { span: 16 }
      },
      mdl: {
        role: {},
        role_id: 0
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
          title: "Staff",
          dataIndex: "is_staff",
          scopedSlots: { customRender: "staff" }
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
          title: "Action",
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

      visible: false,
      visible_password: false,
      isEdit: false,
      help: {},
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
      this.isEdit = true;
    },
    handleCreate() {
      this.mdl = {
        id: undefined,
        username: "",
        password: "",
        balance: 0.0,
        price_level: 5,
        role_id: null,
        is_active: true
      };
      this.visible = true;
      this.isEdit = false;
    },
    handleChangePassword(record) {
      this.mdl = {
        id: record.id,
        new_password: ''
      }
      this.visible_password = true;
    },
    handleChangeStatus(e) {
      this.mdl.is_active = e.target.checked;
    },
    updateForm() {
      this.loading = true;
      updateUser(this.mdl.id, this.mdl)
        .then(res => {
          this.visible = false;
        })
        .catch(error => {
          this.checkError(error);
        })
        .finally(() => {
          this.loading = false;
        });
    },
    createForm() {
      this.loading = true;
      createUser(this.mdl)
        .then(res => {
          this.visible = false;
        })
        .catch(error => {
          this.checkError(error);
        })
        .finally(() => {
          this.loading = false;
        });
    },
    changePassword() {
      this.loading = true;
      changePassword(this.mdl.id, {
        new_password: this.mdl.new_password
      })
        .then(res => {
          this.visible_password = false;
        })
        .catch(error => {
          this.checkError(error);
        })
        .finally(() => {
          this.loading = false;
        });
    },
    checkError(error) {
      var errors = checkError(
        error,
        "username",
        "password",
        "new_password",
        "price_level",
        "balance",
        "role_id",
        "is_active",
        "non_field_errors"
      );

      this.help = {
        username: errors["username"],
        password: errors["password"],
        new_password: errors["new_password"],
        price_level: errors["price_level"],
        balance: errors["balance"],
        role_id: errors["role_id"],
        is_active: errors["is_active"],
        non_field_errors: errors["non_field_errors"]
      };

      for (var key in errors) {
        if (errors[key]) {
          this.$notification["error"]({
            message: key,
            description: errors[key],
            duration: 4
          });
        }
      }
    }
  }
};
</script>
