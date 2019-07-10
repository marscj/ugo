<template>
  <a-card>
    <a-form :form="form">
      <a-form-item label="Category">
        <!-- <a-select v-decorator="['category', {rules: [{ required: true, message: 'This field is required.' }], initialValue: '1'}]">
          <a-select-option :value="1">Option 1</a-select-option>
          <a-select-option :value="2">Option 2</a-select-option>
          <a-select-option :value="3">Option 3</a-select-option>
        </a-select> -->
        <!-- <a-select
          placeholder="Select category"
          @search="getCategory"
        > 

        </a-select>-->
      </a-form-item>
      <a-form-item label="Product ID:">
        <a-input v-decorator="['productID', {rules: [{ required: true, message: 'This field is required.' }]}]"></a-input>
      </a-form-item>
      <a-form-item label="Title:">
        <a-input v-decorator="['title', {rules: [{ required: true, message: 'This field is required.'}]}]" />
      </a-form-item>
      <a-form-item label="Location:">
        <a-input v-decorator="['location', {rules: [{ required: true, message: 'This field is required.' }]}]"></a-input>
      </a-form-item>
      <a-form-item
        label="Photo"
        :validate-status="photo.file == null ?  'error': null"
        :help="photo.file == null ?  'This field is required.': null"
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
      <a-form-item label="Gallery">
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
        label="SubTitle"
        :validate-status="subtitle.help == null || subtitle.help === '' ? null : 'error'"
        :help="subtitle.help"
      >
        <div class="components-container">
          <div>
            <tinymce v-model="subtitle.data" :height="150" />
          </div>
        </div>
      </a-form-item>
      <a-form-item
        label="Content"
        :validate-status="content.help == null || content.help === '' ? null : 'error'"
        :help="content.help"
      >
        <div class="components-container">
          <div>
            <tinymce v-model="content.data" :height="500" />
          </div>
        </div>
      </a-form-item>
    </a-form>
    <a-row>
      <a-col span="2">
      <a-button type="primary" html-type="submit" @click="handleSubmit">Submit</a-button>
      </a-col>
      <a-col span="2">
      <a-button @click="handleGoBack">Return</a-button>
      </a-col>
    </a-row>
  </a-card>
</template>

<script>
import moment from 'moment'
import pick from 'lodash.pick'
import Tinymce from '@/components/Tinymce'

import { upload } from '@/api/source'
import { getCategoryList, getProduct } from '@/api/product'

export default {
  name:'ProductDetail',
  components: {
    Tinymce,
  },
  props: {
    isEdit: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      labelCol: {
        xs: { span: 24 },
        sm: { span: 2 }
      },
      wrapperCol: {
        xs: { span: 24 },
        sm: { span: 15 }
      },
      buttonCol: {
        wrapperCol: {
          xs: { span: 24 },
          sm: { span: 6}
        }
      },
      form: this.$form.createForm(this),
      photo: {
        data: null,
        file: null,
        help: null,
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
        help: null,
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
          })
        }
      },
      content: {
        data: null,
        help: null
      },
      subtitle: {
        data: null,
        help: null
      }
    }
  },
  mounted() {
    if (this.isEdit) {
      this.fetch()
    }
  },
  methods: {
    handleGoBack () {
      this.$router.go(-1)
    },
    fetch() {
      getProduct(this.$route.params.id).then((res) => {
        const { result } = res
        this.initData(result)
      })
    },
    getCategory() {
      getCategoryList().then((res) => {

      })
    },
    initData (data) {
      if(this.isEdit) {
        this.$route.meta.title = data.title
      }

      this.content = {
        data: data.content,
        help: null
      }

      this.subtitle = {
        data: data.subtitle,
        help: null
      }

      if (data.photo != null) {
        this.photo.file = {
            uid: data.photo.uid,
            name: data.photo.name,
            url: data.photo.image.thumbnail
        }
      }

      if (data.gallery != null) {
        for(var g of data.gallery) {
            this.gallery.file.push({
                uid: g.uid,
                name: g.name,
                url: g.image.thumbnail
            })
        }
      }
      this.$nextTick(() => {
        var formData = pick(data, ['productID', 'title', 'location'])
        this.form.setFieldsValue(formData)
      })
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
