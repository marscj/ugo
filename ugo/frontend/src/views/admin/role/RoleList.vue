<template>
  <a-spin :spinning="spinning">
    <a-card :bordered="false" :style="{ height: '100%' }" v-action:query>
      <a-row :gutter="24">
        <a-col :md="4">
          <a-list itemLayout="vertical" :dataSource="roles">
            <a-list-item slot="renderItem" slot-scope="item, index" :key="index">
              <a-list-item-meta :style="{ marginBottom: '0' }">
                <span
                  slot="description"
                  style="text-align: center; display: block"
                >{{ item.describe }}</span>
                <a
                  slot="title"
                  style="text-align: center; display: block"
                  @click="edit(item)"
                >{{ item.name }}</a>
              </a-list-item-meta>
            </a-list-item>
          </a-list>
        </a-col>
        <a-col :md="20">
          <div style="max-width: 800px">
            <div>
              <h3>Role：{{ form.name }}</h3>
            </div>
            <a-form :form="form">
              <a-form-item
                label="Name:"
                required
                :validate-status="help.name == null || help.name === '' ?  null : 'error'"
                :help="help.name"
              >
                <a-input v-model="form.name" />
              </a-form-item>

              <a-form-item
                label="Status"
                required
                :validate-status="help.status == null || help.status === '' ?  null : 'error'"
                :help="help.status"
              >
                <a-select v-model="form.status">
                  <a-select-option :value="0">Enable</a-select-option>
                  <a-select-option :value="1">Disable</a-select-option>
                </a-select>
              </a-form-item>

              <a-form-item
                label="Describe"
                :validate-status="help.describe == null || help.describe === '' ?  null : 'error'"
                :help="help.describe"
              >
                <a-textarea v-model="form.describe" />
              </a-form-item>

              <a-form-item label="Permissions" v-if="isEdit">
                <a-row :gutter="16" v-for="(permission, index) in form.permissions" :key="index">
                  <a-col :xl="4" :lg="24">{{ permission.permissionName }}：</a-col>
                  <a-col :xl="20" :lg="24">
                    <a-checkbox-group
                      :options="permission.actionEntitySet.map((f) => {
                        return f.label
                      })"
                      :value="permission.actionEntitySet.map((f) => {
                        if (f.enable) {
                          return f.label
                        }
                      })"
                      @change="(value) => {
                        permission.actionEntitySet.forEach((f)=>{
                          if(value.includes(f.label)) {
                            f.enable = true
                          } else {
                            f.enable = false
                          }
                        })
                      }"
                    />
                  </a-col>
                </a-row>
              </a-form-item>
              <div style="position:relative; margin-top:20px">
                <a-button
                  type="primary"
                  html-type="submit"
                  @click="handleSubmit"
                  style="margin-right:20px"
                >Submit</a-button>
              </div>
            </a-form>
          </div>
        </a-col>
      </a-row>
    </a-card>
  </a-spin>
</template>

<script>
import { checkError } from "@/views/utils/error";
import { getRoleList, createRole, updateRole } from "@/api/manage";
import { mixinDevice } from "@/utils/mixin";

export default {
  name: "RoleList",
  mixins: [mixinDevice],
  components: {},
  data() {
    return {
      isEdit: false,
      spinning: false,
      form: {},
      roles: [],
      help: {}
    };
  },
  created() {
    this.fetch();
  },
  methods: {
    edit(record) {
      this.form = Object.assign({}, record);
      if(this.form.id != undefined) {
        this.isEdit = true;
      } else {
        this.isEdit = false;
      }
    },
    fetch() {
      this.spinning = true;
      getRoleList()
        .then(res => {
          const { result } = res;
          this.roles = result;
          this.roles.push({
            id: undefined,
            name: "Add Role",
            describe: "Add a role",
            status: 0,
            permissions: []
          });
          this.edit(this.roles[0]);
        })
        .finally(() => {
          this.spinning = false;
        });
    },
    checkError(error) {
      var errors = checkError(error, "name", "status", "describe");

      this.help = {
        name: errors["name"],
        status: errors["status"],
        describe: errors["describe"]
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
    },
    handleSubmit() {
      this.spinning = true;

      if (this.isEdit) {
        updateRole(this.form.id, this.form)
          .then(res => {
            this.$notification.success({
              message: "修改成功"
            });
          })
          .catch(error => {
            this.checkError(error);
          })
          .finally(() => {
            this.spinning = false;
          });
      } else {
        createRole(this.form)
          .then(res => {
            this.$notification.success({
              message: "创建成功"
            });
            this.form = res.result;
            this.isEdit = true;
          })
          .catch(error => {
            this.checkError(error);
          })
          .finally(() => {
            this.spinning = false;
          });
      }
    }
  }
};
</script>

<style scoped>
</style>
