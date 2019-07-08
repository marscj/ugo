<!-- <template>
  <div class="clearfix" >
    <a-upload
      action="api/source/"
      listType="picture-card"
      :fileList="fileList"
      name='image'
      @preview="handlePreview"
      @change="handleChange"
      :remove="handleRemove"
    >
      <div v-if="fileList.length < 3">
        <a-icon type="plus" />
        <div class="ant-upload-text">Upload</div>
      </div> 
    </a-upload>
    <a-modal :visible="previewVisible" :footer="null" @cancel="handleCancel">
      <img alt="example" style="width: 100%" :src="previewImage" />
    </a-modal>
  </div>
</template>

<script>
import { upload } from '@/api/upload'
export default {
  data () {
    return {
      previewVisible: false,
      previewImage: '',
      fileList: [{
        uid: '-1',
        name: 'xxx.png',
        status: 'done',
        url: 'https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png',
      }],
    }
  },
  methods: {
    handleCancel () {
      this.previewVisible = false
    },
    handlePreview (file) {
      this.previewImage = file.url || file.thumbUrl
      this.previewVisible = true
    },
    handleRemove (file) {
      console.log(file)
    },
    handleChange ({ file, fileList, event }) {
      this.fileList = fileList
    },
  },
}
</script>
<style>
  /* you can make up upload button and sample style by using stylesheets */
  .ant-upload-select-picture-card i {
    font-size: 32px;
    color: #999;
  }

  .ant-upload-select-picture-card .ant-upload-text {
    margin-top: 8px;
    color: #666;
  }
</style>
-->

<template>
  <div class="clearfix">
    <a-upload
      :fileList="fileList"
      :remove="handleRemove"
      :beforeUpload="beforeUpload"
      listType="picture-card"
    >
      <!-- <a-button>
        <a-icon type="upload" /> Select File
      </a-button> -->
      <div v-if="fileList.length < 3">
        <a-icon type="plus" />
        <div class="ant-upload-text">Upload</div>
      </div> 
    </a-upload>
    <!-- <a-button
      type="primary"
      @click="handleUpload"
      :disabled="fileList.length === 0"
      :loading="uploading"
      style="margin-top: 16px"
    >
      {{uploading ? 'Uploading' : 'Start Upload' }}
    </a-button> -->
  </div>
</template>
<script>
import { upload } from '@/api/upload'
import Vue from 'vue'
import { ACCESS_TOKEN } from '@/store/mutation-types'

export default {
  data () {
    return {
      fileList: [
        {
          uid: '-1',
          name: 'xxx.png',
          status: 'done',
          url: 'https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png',
        }
      ],
      uploading: false,
      headers: {
        'Authorization': 'JWT ' + Vue.ls.get(ACCESS_TOKEN)
      }
    }
  },
  methods: {
    handleRemove(file) {
      const index = this.fileList.indexOf(file);
      const newFileList = this.fileList.slice();
      newFileList.splice(index, 1);
      this.fileList = newFileList
    },
    beforeUpload(file) {
      this.handleUpload(file)
      return false;
    },
    handleChange ({ file, fileList, event }) {
      this.fileList = fileList
    },
    handleUpload(file) {
      console.log('11111111')
      const formData = new FormData();
      formData.append('image', file);
      this.uploading = true
      console.log('22222222')
      upload(formData).then((res) => {
        // this.fileList = []
        console.log('33333333')
        this.fileList.push({
          uid: 'kjwlkejf',
          name: 'sdfef.png',
          status: 'done',
          url: res.result.image.thumbnail,
        })
        console.log(this.fileList)
        console.log('44444')
        this.uploading = false
        this.$message.success('upload successfully.')
      }).catch((error) => {
        this.uploading = false
        this.$message.error('upload failed.')
        console.log(error)
      })
    }
  },
}
</script>