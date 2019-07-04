<template>
  <a-modal
    :title="title"
    :width="640"
    :visible="visible"
    :confirmLoading="confirmLoading"
    @ok="handleSubmit"
    @cancel="handleCancel"
  >
    <a-spin :spinning="confirmLoading">
      <a-form :form="form">
        <a-form-item
          label="ID:"
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
        >
        <a-input v-decorator="['id']" :disabled="true"/>
        </a-form-item>
      </a-form>
      <a-form :form="form">
        <a-form-item
          label="Name:"
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
        >
          <a-input v-decorator="['name', {rules: [{required: true, min: 2, message: 'Please enter at least 2 characters.'}]}]" />
        </a-form-item>
      </a-form>
    </a-spin>
  </a-modal>
</template>

<script>
import pick from 'lodash.pick'
import { updateCategory, createCategory } from '@/api/product'
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
      confirmLoading: false,
      title:'Add',

      form: this.$form.createForm(this)
    }
  },
  methods: {
    add () {
      this.title = 'Add'
      this.visible = true
      this.$nextTick(() => {
        this.form.setFieldsValue({'id': null, 'name': ''})
      })
    },
    edit(data) {
      this.title = 'Edit'
      this.visible = true
      this.$nextTick(() => {
        const formData = pick(data, ['id', 'name'])
        this.form.setFieldsValue(formData)
      })
    },
    createForm(data) {
      return createCategory(data).then((res) => {
        console.log(res)
        this.$emit('ok', res)
        this.visible = false
        this.confirmLoading = false
      }).catch((error) => {
        this.confirmLoading = false
      })
    },
    handleSubmit () {
      const { form: { validateFields } } = this
      this.confirmLoading = true
      console.log(this)
      validateFields((errors, values) => {
        if (!errors) {
          if (this.title === 'Add') {
            this.createForm(values)
          }
          
        } else {
          this.confirmLoading = false
        }
        // if (!errors) {
        //   setTimeout(() => {
        //     this.visible = false
        //     this.confirmLoading = false
        //     this.$emit('ok', values)
        //   }, 1500)
        // } else {
        //   this.confirmLoading = false
        // }
      })
    },
    handleCancel () {
      this.visible = false
    }
  }
}
</script>
