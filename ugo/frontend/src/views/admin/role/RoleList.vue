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
              <a-form-item label="Name:" required>
                <a-input v-model="form.name" />
              </a-form-item>

              <a-form-item label="Status" required>
                <a-select v-model="form.status">
                  <a-select-option :value="0">Enable</a-select-option>
                  <a-select-option :value="1">Disable</a-select-option>
                </a-select>
              </a-form-item>

              <a-form-item label="Describe" required>
                <a-textarea v-model="form.describe" />
              </a-form-item>

              <a-form-item label="Permissions">
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
import { getRoleList, createRole, updateRole } from "@/api/manage";
import { mixinDevice } from "@/utils/mixin";
import { actionToObject } from "@/utils/permissions";

export default {
  name: "RoleList",
  mixins: [mixinDevice],
  components: {},
  data() {
    return {
      spinning: false,
      form: {},

      roles: [],
      permissions: []
    };
  },
  created() {
    this.fetch();
  },
  methods: {
    add() {
      this.edit({});
    },
    edit(record) {
      this.form = Object.assign({}, record);
    },
    fetch() {
      this.spinning = true;
      getRoleList()
        .then(res => {
          const { result } = res;
          this.roles = result;
          this.roles.push({
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
    handleSubmit() {
      this.spinning = true
      console.log(this.form)
      updateRole(this.form.id, this.form).then((res) => {

      }).finally(() => {
        this.spinning = false
      })
    }
  }
};
</script>

<style scoped>
</style>
