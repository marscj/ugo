<template>
  <div>
    <a-form :form="form" @submit="handleSubmit">

      <a-form-item
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        label="Product ID:"
      >
        <a-input v-decorator="['productID', {rules: [{ required: true, message: 'This field is required.' }]}]"></a-input>
      </a-form-item>

      <a-form-item
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        label="Product Name:"
      >
        <a-input v-decorator="['name', {rules: [{ required: true, message: 'This field is required.'}]}]" />
      </a-form-item>

      <a-form-item
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        label="Category"
      >
        <a-select v-decorator="['category', {rules: [{ required: true, message: 'This field is required.' }], initialValue: '1'}]">
          <a-select-option :value="1">Option 1</a-select-option>
          <a-select-option :value="2">Option 2</a-select-option>
          <a-select-option :value="3">Option 3</a-select-option>
        </a-select>
      </a-form-item>

      <a-form-item
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        label="Description"
      >
        <a-textarea :rows="5" placeholder="..." v-decorator="['description', {rules: [{ required: true }]}]" />
      </a-form-item>

      <!-- <a-form-item
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        label="Photo"
      >
        <a-upload
          name="avatar"
          listType="picture-card"
          :showUploadList="false"
          class="avatar-uploader"
          action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
          v-decorator="['productID']"
          @change="handleChange"
        >
          <img v-if="imageUrl" :src="imageUrl" alt="avatar" />
          <div v-else>
              <a-icon :type="loading ? 'loading' : 'plus'" />
              <div class="ant-upload-text">Upload</div>
          </div>
        </a-upload>
      </a-form-item> -->

      <a-form-item
        v-bind="buttonCol"
      >
        <a-row>
          <a-col span="6">
            <a-button type="primary" html-type="submit">提交</a-button>
          </a-col>
          <a-col span="10">
            <a-button @click="handleGoBack">返回</a-button>
          </a-col>
          <a-col span="8"></a-col>
        </a-row>
      </a-form-item>
    </a-form>
  </div>
</template>

<script>
import moment from 'moment'
import pick from 'lodash.pick'

export default {
  name: 'TableEdit',
  props: {
    record: {
      type: [Object, String],
      default: ''
    }
  },
  data () {
    return {
      labelCol: {
        xs: { span: 24 },
        sm: { span: 5 }
      },
      wrapperCol: {
        xs: { span: 24 },
        sm: { span: 12 }
      },
      buttonCol: {
        wrapperCol: {
          xs: { span: 24 },
          sm: { span: 12, offset: 5 }
        }
      },
      form: this.$form.createForm(this),
      id: 0,
      loading: false,
      imageUrl: '',
    }
  },
  // beforeCreate () {
  //   this.form = this.$form.createForm(this)
  // },
  mounted () {
    this.$nextTick(() => {
      this.loadEditInfo(this.record)
    })
  },
  methods: {
    handleGoBack () {
      this.$emit('onGoBack')
    },
    handleSubmit () {
      const { form: { validateFields } } = this
      validateFields((err, values) => {
        if (!err) {
          console.log('Received values of form: ', values)
        }
      })
    },
    handleGetInfo () {

    },
    loadEditInfo (data) {
      const { form } = this
      this.$nextTick(() => {
        const formData = pick(data, ['productID', 'name', 'category', 'description', 'image'])
        form.setFieldsValue(formData)
      })
    },
    handleChange (info) {
      if (info.file.status === 'uploading') {
        this.loading = true
        return
      }
      if (info.file.status === 'done') {
        // Get this url from response in real world.
        getBase64(info.file.originFileObj, (imageUrl) => {
          this.imageUrl = imageUrl
          this.loading = false
        })
      }
    },
  }
}
</script>

<style>
  .avatar-uploader > .ant-upload {
    width: 128px;
    height: 128px;
  }
  .ant-upload-select-picture-card i {
    font-size: 32px;
    color: #999;
  }

  .ant-upload-select-picture-card .ant-upload-text {
    margin-top: 8px;
    color: #666;
  }
</style>