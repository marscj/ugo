<template>
  <a-modal
    key="formkey"
    :title="title"
    :width="640"
    :visible="visible"
    :confirmLoading="confirmLoading"
    @ok="handleSubmit"
    @cancel="visible=false"
  >
    <template slot="footer">
      <a-button key="back" @click="visible=false">Return</a-button>
      <a-button key="submit" :type="submitButton.type" @click="handleSubmit">{{submitButton.name}}</a-button>
    </template>
    <a-spin :spinning="confirmLoading">
      <a-form :form="form">
        <a-form-item
          label="ID:"
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
        >
        <a-input v-decorator="['id']" :disabled="true"/>
        </a-form-item>
        <a-form-item
          label="Name:"
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
          :validate-status="validate['name'] != null ? 'error' : null"
          :help="validate['name']"
        >
          <a-input v-decorator="['name', {rules: [{required: true, min: 2, message: 'Please enter at least 2 characters.'}]}]" />
        </a-form-item>
      </a-form>
    </a-spin>
  </a-modal>
</template>

<script>
import pick from 'lodash.pick'
import { checkError } from '@/views/utils/error'
import { createCategory, updateCategory, deleteCategory } from '@/api/backend'
export default {
  name: 'CreateForm',
  data () {
    return {
      labelCol: {
        xs: { span: 24 },
        sm: { span: 7 }
      },
      wrapperCol: {
        xs: { span: 24 },
        sm: { span: 13 }
      },
      visible: false,
      showDelete: false,
      confirmLoading: false,
      submitButton: {
        type: 'primary',
        name: 'Submit'
      },
      title:'Add',
      validate: {
        name: {}
      },

      form: this.$form.createForm(this)
    }
  },
  methods: {
    add () {
      this.title = 'Add'
      this.visible = true
      this.submitButton = {
        type: 'primary',
        name: 'Submit'
      },
      this.validate = {},
      this.$nextTick(() => {
        this.form.setFieldsValue({'id': null, 'name': ''})
      })
    },
    edit(data) {
      this.title = 'Edit'
      this.visible = true
      this.submitButton = {
        type: 'primary',
        name: 'Submit'
      },
      this.validate = {},
      this.$nextTick(() => {
        const formData = pick(data, ['id', 'name'])
        this.form.setFieldsValue(formData)
      })
    },
    delete(data) {
      this.title = 'Are you sure delete this category?'
      this.visible = true
      this.submitButton = {
        type: 'danger',
        name: 'Yes'
      },
      this.validate = {},
      this.$nextTick(() => {
        const formData = pick(data, ['id', 'name'])
        this.form.setFieldsValue(formData)
      })
    },
    createForm(data) {
      return createCategory(data).then((res) => {
        this.$emit('create', res.result)
        this.visible = false
      }).catch((error) => {
        this.validate.name = checkError(error, 'name')['name']
        this.$notification['error']({
          message: 'error',
          description: 'create failure',
          duration: 4
        })
      }).finally(() => {
        this.confirmLoading = false
      })
    },
    updateForm(data) {
      return updateCategory(data['id'], data).then((res) => {
        this.$emit('update', res.result)
        this.visible = false
      }).catch((error) => {
        this.validate.name = checkError(error, 'name')['name']
        this.$notification['error']({
          message: 'error',
          description: 'change failure',
          duration: 4
        })
      }).finally(() => {
        this.confirmLoading = false
      })
    },
    deleteForm(data) {
      this.loading = true
      return deleteCategory(data.id).then((res) => {
        this.$emit('delete', data)
        this.visible = false
      }).catch((error) => {
        this.$notification['error']({
          message: 'error',
          description: 'delete failure',
          duration: 4
        })
      }).finally(() => {
        this.confirmLoading = false
      })
    },
    handleSubmit () {
      const { form: { validateFields } } = this
      this.confirmLoading = true
      validateFields((errors, values) => {
        if (!errors) {
          if (this.title === 'Add') {
            this.createForm(values)
          } else if (this.title === 'Edit') {
            this.updateForm(values)
          } else {
            this.deleteForm(values)
          }
        } else {
          this.confirmLoading = false
        }
      })
    }
  }
}
</script>
