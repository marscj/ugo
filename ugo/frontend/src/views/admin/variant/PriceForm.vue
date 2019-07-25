<template>
  <a-modal
    key="formkey"
    :title="title"
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
        <a-form-item label="ID" :labelCol="labelCol" :wrapperCol="wrapperCol">
          <a-input v-decorator="['id']" :disabled="true" />
        </a-form-item>
        <a-form-item label="Variant ID:" :labelCol="labelCol" :wrapperCol="wrapperCol">
          <a-input v-decorator="['variant_id']" :disabled="true" />
        </a-form-item>
        <a-form-item
          label="User"
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
        >
          <a-select
            v-decorator="[
                'user_id',
                {rules: [{ required: true, message: 'Please select user.' }]}
            ]"
            placeholder="Please select a user"
          >
            <a-select-option v-for="data in userOption" :key="data.id">{{data.username}}</a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item
          label="Current Lev"
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
          :validate-status="validate['curLev'] != null ? 'error' : null"
          :help="validate['curLev']"
        >
          <a-input-number
            :min="1"
            :max="5"
            v-decorator="['curLev', {rules: [{required: true}], initialValue: 1}]"
          />
        </a-form-item>
        <a-form-item
          label="Lev1"
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
          :validate-status="validate['lev1'] != null ? 'error' : null"
          :help="validate['lev1']"
        >
          <a-input-number
            :min="0.0"
            :max="99999.99"
            :precision="2"
            :step="0.5"
            v-decorator="['lev1', {rules: [{required: true}], initialValue: 0.0}]"
          />
        </a-form-item>
        <a-form-item
          label="Lev2"
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
          :validate-status="validate['lev2'] != null ? 'error' : null"
          :help="validate['lev2']"
        >
          <a-input-number
            :min="0.0"
            :max="99999.99"
            :precision="2"
            :step="0.5"
            v-decorator="['lev2', {rules: [{required: true}], initialValue: 0.0}]"
          />
        </a-form-item>
        <a-form-item
          label="Lev3"
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
          :validate-status="validate['lev3'] != null ? 'error' : null"
          :help="validate['lev3']"
        >
          <a-input-number
            :min="0.0"
            :max="99999.99"
            :precision="2"
            :step="0.5"
            v-decorator="['lev3', {rules: [{required: true}], initialValue: 0.0}]"
          />
        </a-form-item>
        <a-form-item
          label="Lev4"
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
          :validate-status="validate['lev4'] != null ? 'error' : null"
          :help="validate['lev4']"
        >
          <a-input-number
            :min="0.0"
            :max="99999.99"
            :precision="2"
            :step="0.5"
            v-decorator="['lev4', {rules: [{required: true}], initialValue: 0.0}]"
          />
        </a-form-item>
        <a-form-item
          label="Lev5"
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
          :validate-status="validate['lev5'] != null ? 'error' : null"
          :help="validate['lev5']"
        >
          <a-input-number
            :min="0.0"
            :max="99999.99"
            :precision="2"
            :step="0.5"
            v-decorator="['lev5', {rules: [{required: true}], initialValue: 0.0}]"
          />
        </a-form-item>
      </a-form>
    </a-spin>
  </a-modal>
</template>

<script>
import pick from "lodash.pick";
import { checkError } from "@/views/utils/error";

import { createPrice, updatePrice, deletePrice } from "@/api/price";
import { getCompanyUserList } from "@/api/manage";

export default {
  name: "CreateForm",
  data() {
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
        type: "primary",
        name: "Submit"
      },
      title: "New",
      validate: {},
      userOption: [],
      form: this.$form.createForm(this)
    };
  },
  methods: {
    add(data) {
      this.title = "New";
      this.visible = true;
      (this.submitButton = {
        type: "primary",
        name: "Submit"
      }),
        (this.validate = {}),
        this.$nextTick(() => {
          this.form.setFieldsValue(pick(data, ["variant_id"]));
        });

      if (this.userOption.length == 0) {
        this.getUserOption();
      }
    },
    edit(data) {
      this.title = "Edit";
      this.visible = true;
      (this.submitButton = {
        type: "primary",
        name: "Submit"
      }),
        (this.validate = {}),
        this.$nextTick(() => {
          const formData = pick(data, [
            "id",
            "user",
            "variant",
            "curLev",
            "lev1",
            "lev2",
            "lev3",
            "lev4",
            "lev5"
          ]);
          this.form.setFieldsValue(formData);
        });
    },
    delete(data) {
      this.title = "Are you sure delete this user price form?";
      this.visible = true;
      (this.submitButton = {
        type: "danger",
        name: "Yes"
      }),
        (this.validate = {}),
        this.$nextTick(() => {
          const formData = pick(data, [
            "id",
            "user",
            "variant",
            "curLev",
            "lev1",
            "lev2",
            "lev3",
            "lev4",
            "lev5"
          ]);
          this.form.setFieldsValue(formData);
        });
    },
    createForm(data) {
      return createPrice(data)
        .then(res => {
          this.$emit("create", res.result);
          this.visible = false;
        })
        .catch(error => {
          this.validate.name = checkError(error, "name")["name"];
          this.$notification["error"]({
            message: "error",
            description: "create failure",
            duration: 4
          });
        })
        .finally(() => {
          this.confirmLoading = false;
        });
    },
    updateForm(data) {
      return updatePrice(data["id"], data)
        .then(res => {
          this.$emit("update", res.result);
          this.visible = false;
        })
        .catch(error => {
          this.validate.name = checkError(error, "name")["name"];
          this.$notification["error"]({
            message: "error",
            description: "change failure",
            duration: 4
          });
        })
        .finally(() => {
          this.confirmLoading = false;
        });
    },
    deleteForm(data) {
      this.loading = true;
      return deletePrice(data.id)
        .then(res => {
          this.$emit("delete", data);
          this.visible = false;
        })
        .catch(error => {
          this.$notification["error"]({
            message: "error",
            description: "delete failure",
            duration: 4
          });
        })
        .finally(() => {
          this.confirmLoading = false;
        });
    },
    handleSubmit() {
      const {
        form: { validateFields }
      } = this;
      this.confirmLoading = true;
      validateFields((errors, values) => {
        if (!errors) {
          if (this.title === "New") {
            console.log(values)
            this.createForm(values);
          } else if (this.title === "Edit") {
            this.updateForm(values);
          } else {
            this.deleteForm(values);
          }
        } else {
          this.confirmLoading = false;
        }
      });
    },
    getUserOption() {
      getCompanyUserList().then(res => {
        const { result } = res;
        this.userOption = result;
      });
    }
  }
};
</script>
