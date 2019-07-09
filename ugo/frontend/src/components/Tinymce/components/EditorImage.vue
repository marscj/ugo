<template>
  <div class="upload-container">
    <a-button type="primary" style="{background:color,borderColor:color}" @click="dialogVisible=true">
      Upload
    </a-button>

    <a-modal :visible="dialogVisible" title="Select a picture" @cancel="dialogVisible=false" @ok="dialogVisible=false">
      <a-upload-dragger
        :multiple="false"
        :fileList="fileList"
        :showUploadList="false"
        :beforeUpload="beforeUpload"
        :remove="handleRemove"
        :customRequest="customRequest"
        listType="picture-card"
      >
        <div>
          <a-icon :type="loading ? 'loading' : 'plus'" />
          <div class="ant-upload-text">Upload</div>
        </div> 
      </a-upload-dragger>
    </a-modal>
  </div>
</template>

<script>
import { upload } from '@/api/source'
export default {
  name: 'EditorSlideUpload',
  props: {
    color: {
      type: String,
      default: '#1890ff'
    }
  },
  data() {
    return {
      dialogVisible: false,
      listObj: {},
      fileList: [],
      loading: false
    }
  },
  methods: {
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
    handleRemove(file) {
      const index = this.fileList.indexOf(file);
      const newFileList = this.fileList.slice();
      newFileList.splice(index, 1);
      this.fileList = newFileList
    },
    customRequest(request) {
      const formData = new FormData();
      formData.append('image', request.file);
      this.loading = true
      upload(formData).then((res) => {
        const { result } = res
        this.fileList.push({
          uid: result.uid,
          name: result.name,
          status: 'done',
          url: result.image.full_size,
        })
        this.$message.success('Upload successfully.')
        this.$emit('successCBK', this.fileList[0])
        this.fileList = []
        this.dialogVisible = false

      }).catch((error) => {
        this.$message.error('Upload failed.')
        console.log(error)
      }).finally(() => {
        this.loading = false
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.editor-slide-upload {
  margin-bottom: 20px;
  /deep/ .el-upload--picture-card {
    width: 100%;
  }
}

.upload-container {
  .a-upload {
    width: 100%;

    .el-upload-dragger {
      width: 100%;
      height: 200px;
    }
  }
}
</style>
