<template>
  <a-card :bordered="false" :style="{ height: '100%' }">
    <a-row :gutter="24">
      <a-col :md="4">
        <a-list itemLayout="vertical" :dataSource="roles">
          <a-list-item slot="renderItem" slot-scope="item, index" :key="index">
            <a-list-item-meta :style="{ marginBottom: '0' }">
              <span slot="description" style="text-align: center; display: block">{{ item.describe }}</span>
              <a slot="title" style="text-align: center; display: block" @click="edit(item)">{{ item.name }}</a>
            </a-list-item-meta>
          </a-list-item>
        </a-list>
      </a-col>
      <a-col :md="20">
        <div style="max-width: 800px">
          <a-divider v-if="isMobile()" />
          <div v-if="mdl.id">
            <h3>Role：{{ mdl.name }}</h3>
          </div>
          <a-form :form="form" :layout="isMobile() ? 'vertical' : 'horizontal'">
            <a-form-item label="Key">
              <a-input v-decorator="[ 'id', {rules: [{ required: true, message: 'Please input unique key!' }]} ]" />
            </a-form-item>

            <a-form-item label="Name:">
              <a-input v-decorator="[ 'name', {rules: [{ required: true, message: 'This field is required.' }]} ]" />
            </a-form-item>

            <a-form-item label="Status">
              <a-select v-decorator="[ 'status', {rules: []} ]">
                <a-select-option :value="0">Enable</a-select-option>
                <a-select-option :value="1">Disable</a-select-option>
              </a-select>
            </a-form-item>

            <a-form-item label="Describe">
              <a-textarea :row="3" v-decorator="[ 'describe', {rules: [{ required: true, message: 'This field is required.' }]} ]" />
            </a-form-item>

            <a-form-item label="Permissions">
              <a-row :gutter="16" v-for="(permission, index) in permissions" :key="index">
                <a-col :xl="4" :lg="24">
                  {{ permission.permissionName }}：
                </a-col>
                <a-col :xl="20" :lg="24">
                  <a-checkbox
                    v-if="permission.actionsOptions.length > 0"
                    :indeterminate="permission.indeterminate"
                    :checked="permission.checkedAll"
                    @change="onChangeCheckAll($event, permission)">
                    all
                  </a-checkbox>
                  <a-checkbox-group :options="permission.actionsOptions" v-model="permission.selected" @change="onChangeCheck(permission)" />
                </a-col>
              </a-row>
            </a-form-item>
          </a-form>
        </div>
      </a-col>
    </a-row>
  </a-card>
</template>

<script>
import { getRoleList, getPermissions } from '@/api/manage'
import { mixinDevice } from '@/utils/mixin'
import { actionToObject } from '@/utils/permissions'
import pick from 'lodash.pick'

export default {
  name: 'RoleList',
  mixins: [mixinDevice],
  components: {},
  data () {
    return {
      form: this.$form.createForm(this),
      mdl: {},

      roles: [],
      permissions: []
    }
  },
  created () {
    getRoleList().then((res) => {
      this.roles = res.result
      this.roles.push({
        id: '-1',
        name: 'Add Role',
        describe: 'Add a role',
        permissions: [

        ]
      }) 
      this.loadPermissions()
    })
  },
  methods: {
    callback (val) {
    },

    add () {
      this.edit({ id: 0 })
    },

    edit (record) {
      this.mdl = Object.assign({}, record)
      if (this.mdl.permissions && this.permissions) {
        const permissionsAction = {}
        this.mdl.permissions.forEach(permission => {
          permissionsAction[permission.permissionId] = permission.actionEntitySet.map(entity => entity.action)
        })
        this.permissions.forEach(permission => {
          const selected = permissionsAction[permission.permissionId]
          permission.selected = selected || []
          this.onChangeCheck(permission)
        })
      }

      this.$nextTick(() => {
        this.form.setFieldsValue(pick(this.mdl, 'id', 'name', 'status', 'describe'))
      })
    },

    onChangeCheck (permission) {
      permission.indeterminate = !!permission.selected.length && (permission.selected.length < permission.actionsOptions.length)
      permission.checkedAll = permission.selected.length === permission.actionsOptions.length
    },
    onChangeCheckAll (e, permission) {
      Object.assign(permission, {
        selected: e.target.checked ? permission.actionsOptions.map(obj => obj.value) : [],
        indeterminate: false,
        checkedAll: e.target.checked
      })
    },
    loadPermissions () {
      getPermissions().then(res => {
        const result = res.result
        this.permissions = result.map(permission => {
          const options = permission.actionEntitySet.map((f) => {
            f.defaultCheck = false
            return f;
          })
          permission.checkedAll = false
          permission.selected = []
          permission.indeterminate = false
          permission.actionsOptions = options.map(option => {
            return {
              label: option.describe,
              value: option.action
            }
          })
          return permission
        })
        this.edit(this.roles[0])
      })
    }
  }
}
</script>

<style scoped>

</style>
