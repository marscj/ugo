<template>
  <a-spin :spinning="spinning">
    <a-card>
      <a-form :form="form">
        <a-form-item
          label="Status"
          :required="true"
        >
          <a-switch checkedChildren="上架" unCheckedChildren="下架" :checked="status" @change="handleStatusChange"/>
        </a-form-item>
        <a-form-item
          label="Category"
          :required="true"
          :validate-status="category.help == null || category.help === '' ?  null : 'error'"
          :help="category.help"
        >
          <a-select :value="category.value" @change="category.handleChange" :filterOption="false">
            <a-select-option v-for="d in categoryData" :key="d.value">{{d.label}}</a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item
          label="Product ID"
          :required="true"
          :validate-status="productID.help == null || productID.help === '' ?  null : 'error'"
          :help="productID.help"
        >
          <a-input v-model="productID.data"></a-input>
        </a-form-item>
        <a-form-item
          label="Title"
          :required="true"
          :validate-status="title.help == null || title.help === '' ?  null : 'error'"
          :help="title.help"
        >
          <a-input v-model="title.data"></a-input>
        </a-form-item>
        <a-form-item
          label="SubTitle"
          :validate-status="subtitle.help == null || subtitle.help === '' ?  null : 'error'"
          :help="subtitle.help"
        >
          <a-textarea v-model="subtitle.data" :rows="5"></a-textarea>
        </a-form-item>
        <a-form-item
          label="Location"
          :validate-status="location.help == null || location.help === '' ?  null : 'error'"
          :help="location.help"
        >
          <a-input v-model="location.data"></a-input>
        </a-form-item>
        <a-form-item
          label="Sort ID"
          :validate-status="sort_by.help == null || sort_by.help === '' ?  null : 'error'"
          :help="sort_by.help"
        >
          <a-input v-model="sort_by.data"></a-input>
        </a-form-item>
        <a-form-item
          label="Photo"
          :validate-status="photo.help == null || photo.help === '' ?  null : 'error'"
          :help="photo.help"
          v-if="title.data"
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
          label="Gallery"
          :validate-status="gallery.help == null || gallery.help === '' ?  null : 'error'"
          :help="gallery.help"
          v-if="title.data"
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
          label="Special"
          :validate-status="special.help == null || special.help === '' ? null : 'error'"
          :help="special.help"
        >
          <div class="components-container">
            <div>
              <tinymce v-model="special.data" :height="150" />
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
  </a-spin>
</template>

<script>
import pick from "lodash.pick";
import Tinymce from "@/components/Tinymce";

import { checkError } from "@/views/utils/error";
import { upload } from "@/api/source";
import { getProduct, updateProduct, createProduct } from "@/api/backend";

const categoryData = [
  { value: 1, label: "美食" },
  { value: 2, label: "门票" },
  { value: 3, label: "日游" },
  { value: 4, label: "用车" },
  { value: 5, label: "酒店" },
  { value: 6, label: "伴手礼" }
];

export default {
  name: "ProductDetail",
  components: {
    Tinymce
  },
  props: {
    isEdit: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      categoryData,
      form: this.$form.createForm(this),
      status: true,
      category: {
        value: 1,
        help: null,
        handleChange: (value) => {
          this.category.value = value;
        }
      },
      photo: {
        data: null,
        file: null,
        help: null,
        loading: false,
        remove: file => {
          photo.data = null;
          photo.file = null;
        },
        request: request => {
          const formData = new FormData();
          formData.append("image", request.file);
          formData.append("flag", "icon");
          formData.append("title", this.title.data);
          upload(formData)
            .then(res => {
              const { result } = res;
              this.photo.data = result;
              this.photo.file = {
                uid: result.uid,
                name: result.title,
                status: "done",
                url: result.image.thumbnail
              };
              this.$message.success("Upload successfully.");
            })
            .catch(error => {
              this.$message.error("Upload failed.");
            });
        }
      },
      gallery: {
        data: [],
        file: [],
        help: null,
        remove: file => {
          const index = this.gallery.data.indexOf(file);
          const newFileList = this.gallery.data.slice();
          newFileList.splice(index, 1);
          this.gallery.data = newFileList;

          const _index = this.gallery.file.indexOf(file);
          const _newFileList = this.gallery.file.slice();
          _newFileList.splice(_index, 1);
          this.gallery.file = _newFileList;
        },
        request: request => {
          const formData = new FormData();
          formData.append("image", request.file);
          formData.append("flag", "gallery");
          formData.append("title", this.title.data);
          upload(formData)
            .then(res => {
              const { result } = res;
              this.gallery.data.push(result);
              this.gallery.file.push({
                uid: result.uid,
                name: result.title,
                status: "done",
                url: result.image.full_size
              });
              this.$message.success("Upload successfully.");
            })
            .catch(error => {
              this.$message.error("Upload failed.");
            });
        }
      },
      content: {
        data: null,
        help: null
      },
      subtitle: {
        data: null,
        help: null
      },
      productID: {
        data: null,
        help: null
      },
      sort_by: {
        data: null,
        help: null
      },
      title: {
        data: null,
        help: null
      },
      special: {
        data: null,
        help: null
      },
      location: {
        data: null,
        help: null
      },
      spinning: false
    };
  },
  created() {
    if (this.isEdit) {
      const id = this.$route.params && this.$route.params.id;
      this.fetch(id);
    }
  },
  methods: {
    handleGoBack() {
      this.$router.go(-1);
    },
    fetch(id) {
      this.spinning = true;
      getProduct(id)
        .then(res => {
          const { result } = res;
          this.initData(result);
        })
        .finally(() => {
          this.spinning = false;
        });
    },
    updateForm(data) {
      this.spinning = true;
      updateProduct(this.$route.params.id, data)
        .then(res => {
          const { result } = res;
          this.handleGoBack();
        })
        .catch(error => {
          this.checkError(error);
        })
        .finally(() => {
          this.spinning = false;
        });
    },
    createForm(data) {
      this.spinning = true;
      createProduct(data)
        .then(res => {
          const { result } = res;
          this.handleGoBack()
        }).catch(error => {
          this.checkError(error);
        })
        .finally(() => {
          this.spinning = false;
        });
    },
    checkError(error) {
      var errors = checkError(
        error,
        "category",
        "productID",
        "sort_by",
        "title",
        "subtitle",
        "location",
        "photo",
        "gallery",
        "special",
        "content"
      );
      this.category.help = errors["category"];
      this.productID.help = errors["productID"];
      this.sort_by.help = errors["sort_by"];
      this.title.help = errors["title"];
      this.subtitle.help = errors["subtitle"];
      this.location.help = errors["location"];
      this.photo.help = errors["photo"];
      this.gallery.help = errors["gallery"];
      this.special.help = errors["special"];
      this.content.help = errors["content"];

      for (var key in errors) {
        if (errors[key]) {
          this.$notification["error"]({
            message: key,
            description: errors[key],
            duration: 4
          });
        }
      }
    },
    initData(data) {
      if (this.isEdit) {
        this.$route.meta.title = data.title;
        this.$emit("title");
      }

      this.status = data.status;

      this.category.value = data.category;

      this.productID = {
        data: data.productID,
        help: null
      };

      this.sort_by = {
        data: data.sort_by,
        help: null
      };

      this.title = {
        data: data.title,
        help: null
      };

      this.subtitle = {
        data: data.subtitle,
        help: null
      };

      this.location = {
        data: data.location,
        help: null
      };

      this.content = {
        data: data.content,
        help: null
      };

      this.special = {
        data: data.special,
        help: null
      };

      if (data.photo != null) {
        this.photo.file = {
          uid: data.photo.uid,
          name: data.photo.title,
          url: data.photo.image.thumbnail
        };
        this.photo.data = data.photo;
      }

      if (data.gallery != null) {
        for (var g of data.gallery) {
          this.gallery.file.push({
            uid: g.uid,
            name: g.title,
            url: g.image.full_size
          });
        }
        this.gallery.data = data.gallery;
      }
    },
    handleSubmit() {

      if (this.category.value == null) {
        this.category.help = "This field is required.";
      } else {
        this.category.help = null;
      }

      if (this.productID.data == null || this.productID.data === "") {
        this.productID.help = "This field is required.";
      } else {
        this.productID.help = null;
      }

      this.sort_by.help = null;

      if (this.title.data == null || this.title.data === "") {
        this.title.help = "This field is required.";
      } else {
        this.title.help = null;
      }

      this.subtitle.help = null;
      this.location.help = null;
      this.photo.help = null;
      this.gallery.help = null;
      this.special.help = null;
      this.content.help = null;

      if (
        this.category.help ||
        this.productID.help ||
        this.sort_by.help ||
        this.title.help ||
        this.subtitle.help ||
        this.location.help ||
        this.photo.help ||
        this.gallery.help ||
        this.special.help ||
        this.content.help
      ) {
        return;
      }

      var values = {
        status: this.status,
        category: this.category.value,
        productID: this.productID.data,
        sort_by: this.sort_by.data,
        title: this.title.data,
        subtitle: this.subtitle.data,
        location: this.location.data,
        photo_id: this.photo.data != null ? this.photo.data.id : null,
        gallery_id: this.gallery.data.map(f => {
          if (f) {
            return f.id;
          }
        }),
        special: this.special.data,
        content: this.content.data
      };
      if (this.isEdit) {
        this.updateForm(values);
      } else {
        this.createForm(values);
      }
    },
    beforeUpload(file) {
      const isIMG = file.type === "image/jpeg" || file.type === "image/png";
      if (!isIMG) {
        this.$message.error("You can only upload JPG or PNG file!");
      }
      const isLt2M = file.size / 1024 / 1024 < 2;
      if (!isLt2M) {
        this.$message.error("Image must smaller than 2MB!");
      }
      return isIMG && isLt2M;
    },
    handleStatusChange(value) {
      this.status = value
    }
  }
};
</script>
