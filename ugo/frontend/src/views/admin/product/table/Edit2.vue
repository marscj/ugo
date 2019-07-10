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
      :customRequest="customRequest"
      listType="picture-card"
    >
      <div v-if="fileList.length < 3">
        <a-icon type="plus" />
        <div class="ant-upload-text">Upload</div>
      </div> 
    </a-upload>
  </div>
</template>
<script>
import { upload } from '@/api/upload'

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
      const isIMG = (file.type === 'image/jpeg' || file.type === 'image/png')
      if (!isIMG) {
        this.$message.error('You can only upload JPG or PNG file!')
      }
      const isLt2M = file.size / 1024 / 1024 < 2
      if (!isLt2M) {
        this.$message.error('Image must smaller than 2MB!')
      }
      return isIMG && isLt2M
    },
    customRequest(request) {
      const formData = new FormData();
      formData.append('image', request.file);
      upload(formData).then((res) => {
        const { result } = res
        this.fileList.push({
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
}
</script>