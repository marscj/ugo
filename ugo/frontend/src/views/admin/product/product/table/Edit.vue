<template>
  <div>
    <a-form :form="form" @submit="handleSubmit">
      
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
        label="Product ID:"
      >
        <a-input v-decorator="['productID', {rules: [{ required: true, message: 'This field is required.' }]}]"></a-input>
      </a-form-item>

      <a-form-item
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        label="Title:"
      >
        <a-input v-decorator="['title', {rules: [{ required: true, message: 'This field is required.'}]}]" />
      </a-form-item>

      <a-form-item
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        label="SubTitle:"
      >
        <a-input v-decorator="['subtitle', {rules: [{ required: true, message: 'This field is required.' }]}]"></a-input>
      </a-form-item>

      <a-form-item
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        label="Description"
      >
        <a-textarea :rows="5" placeholder="..." v-decorator="['description', {rules: [{ required: true }]}]" />
      </a-form-item>

      <a-form-item
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        label="Photo"
      >
        <a-upload
          :showUploadList="false"
          :beforeUpload="beforeUpload"
          :remove="photo.remove"
          :customRequest="photo.request"
          listType="picture-card"
        >
          <img v-if="photo.file" :src="photo.file.url" alt="photo" />
          <div v-else>
              <a-icon :type="photo.loading ? 'loading' : 'plus'" />
              <div class="ant-upload-text">Upload</div>
          </div>
        </a-upload>
      </a-form-item>

      <a-form-item
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        label="Gallery"
      >
        <a-upload
          :fileList="gallery.file"
          :beforeUpload="beforeUpload"
          :remove="gallery.remove"
          :customRequest="gallery.request"
          listType="picture-card"
        >
          <div v-if="gallery.file.length < 8">
            <a-icon type="plus" />
            <div class="ant-upload-text">Upload</div>
          </div> 
        </a-upload>
      </a-form-item>
      
      <a-form-item
        :labelCol="labelCol"
        :wrapperCol="{
          xs: { span: 24 },
          sm: { span: 24 }
        }"
      >
        <div class="components-container">
          <div>
            <tinymce v-model="content" :height="500" />
          </div>
          <div class="editor-content" v-html="content" />
        </div>
      </a-form-item>

      <a-form-item
        v-bind="buttonCol"
      >
        <a-row>
          <a-col span="6">
            <a-button type="primary" html-type="submit">Submit</a-button>
          </a-col>
          <a-col span="10">
            <a-button @click="handleGoBack">Return</a-button>
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
import { upload } from '@/api/upload'

import Tinymce from '@/components/Tinymce'

export default {
  name: 'TableEdit',
  components: {
    Tinymce,
  },
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
        sm: { span: 3 }
      },
      wrapperCol: {
        xs: { span: 24 },
        sm: { span: 15 }
      },
      buttonCol: {
        wrapperCol: {
          xs: { span: 24 },
          sm: { span: 12}
        }
      },
      form: this.$form.createForm(this),
      photo: {
        data: null,
        file: null,
        loading: false,
        remove: (file) => {
          photo.data = null
          photo.file = null
        },
        request: (request) => {
          const formData = new FormData();
          formData.append('image', request.file);
          upload(formData).then((res) => {
            const { result } = res
            this.photo.data = result
            this.photo.file = {
              uid: result.uid,
              name: result.name,
              status: 'done',
              url: result.image.thumbnail,
            }
            this.$message.success('Upload successfully.')
          }).catch((error) => {
            this.$message.error('Upload failed.')
          })
        }
      },
      gallery: {
        data: [],
        file: [],
        remove: (file) => {
          const index = this.gallery.data.indexOf(file);
          const newFileList = this.gallery.data.slice();
          newFileList.splice(index, 1);
          this.gallery.data = newFileList

          const _index = this.gallery.file.indexOf(file);
          const _newFileList = this.gallery.file.slice();
          _newFileList.splice(_index, 1);
          this.gallery.file = _newFileList
        },
        request: (request) => {
          const formData = new FormData();
          formData.append('image', request.file);
          upload(formData).then((res) => {
            const { result } = res
            this.gallery.data.push(result) 
            this.gallery.file.push({
              uid: result.uid,
              name: result.name,
              status: 'done',
              url: result.image.thumbnail,
            })
            this.$message.success('Upload successfully.')
          }).catch((error) => {
            this.$message.error('Upload failed.')
            console.log(error)
          })
        }
      },
      content: null
    }
  },
  mounted () {
    this.$nextTick(() => {
      const { form } = this
      this.$nextTick(() => {
        const formData = pick(data, ['productID', 'name', 'category', 'description', 'photo'])
        form.setFieldsValue(formData)
      })
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
    beforeUpload(file) {
      const isIMG = (file.type === 'image/jpeg' || file.type === 'image/png')
      if (!isIMG) {
        this.$message.error('You can only upload JPG or PNG file!')
      }
      const isLt2M = file.size / 1024 / 1024 < 2
      if (!isLt2M) {
        this.$message.error('Image must smaller than 2MB!')
      }
      return isIMG && isLt2M
    }
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

  .editor-content{
    margin-top: 20px;
  }
</style>