<template>
  <a-spin :spinning="spinning">
    <a-card>
      <a-form :form="form">
        <a-form-item
          label="Title"
          :required="true"
          :validate-status="help.title == null || help.title === '' ?  null : 'error'"
          :help="help.title"
        >
          <a-input v-model="form.title"></a-input>
        </a-form-item>

        <a-form-item
          label="SubTitle"
          :required="true"
          :validate-status="help.subtitle == null || help.subtitle === '' ?  null : 'error'"
          :help="help.subtitle"
        >
          <a-textarea v-model="form.subtitle" :rows="5"></a-textarea>
        </a-form-item>

        <a-form-item
          label="Content"
          :required="true"
          :validate-status="help.content == null || help.content === '' ? null : 'error'"
          :help="help.content"
        >
          <div class="components-container">
            <div>
              <tinymce v-model="form.content" :height="500" />
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
import Tinymce from "@/components/Tinymce";
import { checkError } from "@/views/utils/error";
import { getNotice, updateNotice, createNotice } from "@/api/notice";

export default {
  name: "EditDetail",
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
      form: {
        title: '',
        subtitle: '',
        content: ''
      },
      help: {},
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
      getNotice(id)
        .then(res => {
          const { result } = res;
          this.form = result;
          this.initData(result);
        })
        .finally(() => {
          this.spinning = false;
        });
    },
    updateForm(data) {
      this.spinning = true;
      updateNotice(this.$route.params.id, data)
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
      createNotice(data)
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
    checkError(error) {
      var errors = checkError(error, 'title', 'subtitle', 'content');

      this.help = {
        title: errors["title"],
        subtitle: errors["subtitle"],
        content: errors["content"]
      };

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
        this.$emit("title", data);
      }
    },
    handleSubmit() {
      console.log(this.form, '=======')
      if (this.isEdit) {
        this.updateForm(this.form);
      } else {
        this.createForm(this.form);
      }
    }
  }
};
</script>
