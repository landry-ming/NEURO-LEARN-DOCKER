<template>
  <div style="text-align: center">
    <div class="ml-task-form">
      <div style="text-align: left; width: 700px; margin: 0 auto; font-family: 'Arial', Times, serif; font-size: 18px; color: #505050">
        <h2><i class="el-icon-edit-outline"></i> New Machine Learning Task</h2>
      </div>
      <el-form ref="form" :model="form" label-width="100px" label-position="middle">
        <el-form-item label="Task Name">
          <el-input v-model="newform.task_name" placeholder="Specify Task Name, Date_Transformer_Estimator by Default."></el-input>
        </el-form-item>
        <el-form-item label="Task Type">
          <el-radio-group v-model="newform.task_type" @change="onRadioChange">
            <el-radio label="ml_clf">Classification</el-radio>
            <el-radio label="ml_rgs">Regression</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="Proj. Name">
          <el-select class="select-label" v-model="selected_proj_label" placeholder="Select Project" @change="handelSelectionChange">
            <el-option v-for="(proj_option, key) in form.proj_options" :label="proj_option.fields.label" :value="proj_option.fields.label" :key="key"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="Train Data">
          <el-select class="select-data" v-model="newform.train_data" placeholder="Select Train Data" filterable multiple>
            <el-option v-for="(data_option, key) in data_table" :label="data_option.fields.data_name" :value="data_option.fields.data_name" :key="key"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="Label">
          <el-select class="select-label" v-model="newform.label" placeholder="Select Label">
          <el-option v-for="(label_option, key) in form.label_options" :label="label_option.name" :value="label_option.value" :key="key"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="Feat. Sel.">
          <el-select class="select-model" v-model="newform.feat_sel" placeholder="Select Model" filterable multiple>
            <el-option v-for="(feat_sel_option, key) in form.feat_sel_options" :label="feat_sel_option.name" :value="feat_sel_option.value" :key="key"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="Estimator">
          <el-select class="select-model" v-model="newform.estimator" placeholder="Select Model" filterable multiple>
            <el-option v-for="(estimator_option, key) in form.estimator_options" :label="estimator_option.name" :value="estimator_option.value" :key="key"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="CV Type">
          <el-select class="select-cv-type" v-model="newform.cv_type" placeholder="Select CV Type">
          <el-option v-for="(cv_type_option, key) in form.cv_type_options" :label="cv_type_option.name" :value="cv_type_option.value" :key="key"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="Enable Test">
          <el-switch
            v-model="newform.enable_test">
          </el-switch>
        </el-form-item>
        <el-form-item label="Test Data">
          <el-select class="select-data" v-model="newform.test_data" placeholder="Select Test Data" :disabled="!newform.enable_test" filterable multiple>
            <el-option v-for="(data_option, key) in data_table" :label="data_option.fields.data_name" :value="data_option.fields.data_name" :key="key"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">Submit</el-button>
          <el-button @click="onCancel">Cancel</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      selected_proj_label: '',
      selected_proj_id: '',
      data_table: [],
      newform: {
        proj_id: '',
        proj_name: '',
        task_name: '',
        task_type: '',
        train_data: [],
        enable_test: false,
        test_data: [],
        label: '',
        feat_sel: [],
        estimator: [],
        cv_type: ''
      },
      form: {
        proj_options: [],
        label_options: [],
        feat_sel_options: [],
        estimator_options: [],
        cv_type_options: [
          {name: '10-fold', value: '10-fold'},
          {name: '5-fold', value: '5-fold'},
          {name: '3-fold', value: '3-fold'},
          {name: 'Leave-One-Out', value: 'Leave-One-Out'}
        ]
      }
    }
  },
  mounted () {
    this.updateProjects()
    // this.updateData()
  },
  methods: {
    onRadioChange () {
      if (this.newform.task_type === 'ml_clf') {
        this.form.estimator_options = [
          {name: 'Support Vector Machine', value: 'Support Vector Machine'},
          {name: 'Random Forest', value: 'Random Forest'},
          {name: 'Linear Discriminative Analysis', value: 'Linear Discriminative Analysis'},
          {name: 'Logistic Regression', value: 'Logistic Regression'},
          {name: 'K Nearest Neighbor', value: 'K Nearest Neighbor'}
        ]
        this.form.label_options = [
          {name: 'GROUP', value: 'GROUP'}
        ]
        this.form.feat_sel_options = [
          {name: 'Analysis of Variance', value: 'Analysis of Variance'},
          {name: 'Principal Component Analysis', value: 'Principal Component Analysis'},
          {name: 'Recursive Feature Elimination', value: 'Recursive Feature Elimination'},
          {name: 'None', value: 'None'}
        ]
      } else if (this.newform.task_type === 'ml_rgs') {
        this.form.estimator_options = [
          {name: 'Support Vector Regression', value: 'Support Vector Regression'},
          {name: 'Elastic Net', value: 'Elastic Net'},
          {name: 'Ordinary Least Square', value: 'Ordinary Least Square'},
          {name: 'Lasso Regression', value: 'Lasso Regression'},
          {name: 'Ridge Regression', value: 'Ridge Regression'}
        ]
        this.form.label_options = [
          // {name: 'PANSS_P', value: 'PANSS_P'},
          // {name: 'PANSS_N', value: 'PANSS_N'},
          // {name: 'PANSS_G', value: 'PANSS_G'},
          // {name: 'PANSS_T', value: 'PANSS_T'}
          {name: 'SCORE', value: 'SCORE'}
        ]
        this.form.feat_sel_options = [
          {name: 'Analysis of Variance', value: 'Analysis of Variance'},
          {name: 'None', value: 'None'}
        ]
      }
    },
    onSubmit () {
      this.$confirm('Submit this task now?', 'Attention!', {
        confirmButtonText: 'Confirm',
        cancelButtonText: 'Cancel'
      }).then(() => {
        this.newTask()
      }).catch(() => {})
    },
    onCancel () {
      this.$router.replace({
        path: '/analysis/overview',
        component: resolve => require(['@/pages/analysis/overview'], resolve)
      })
    },
    updateProjects () {
      axios.get('/rest/api/v0/show_project_overview?user_id=' + sessionStorage.getItem('UserID'))
        .then(response => {
          var res = response.data
          if (res.error_num === 0) {
            console.log(res)
            this.form.proj_options = res['list']
            console.log(this.form.proj_options)
          } else {
            this.$message.error('Failed!')
            console.log(res['msg'])
          }
        })
    },
    handelSelectionChange () {
      console.log(this.selected_proj_label)
      var i
      for (i in this.form.proj_options) {
        if (this.form.proj_options[i].fields.label === this.selected_proj_label) {
          this.selected_proj_id = this.form.proj_options[i].fields.proj_id
        }
      }
      console.log(this.selected_proj_id)
      this.updateData()
    },
    updateData () {
      axios.get('/rest/api/v0/show_data?proj_id=' + this.selected_proj_id)
        .then(response => {
          var res = response.data
          if (res.error_num === 0) {
            console.log(res)
            this.data_table = res['list']
            console.log(this.data_table[0].fields.data_name)
          } else {
            this.$message.error('Failed!')
            console.log(res['msg'])
          }
        })
    },
    newTask () {
      this.newform.proj_name = this.selected_proj_label
      this.newform.proj_id = this.selected_proj_id
      console.log(JSON.stringify(this.newform))
      axios.post('/rest/api/v0/new_task', JSON.stringify(this.newform))
        .then(response => {
          var res = response.data
          if (res.code === 200) {
            this.$router.replace({
              path: '/analysis/overview',
              component: resolve => require(['@/pages/analysis/overview'], resolve)
            })
            console.log(res)
          } else {
            this.$message.error('Failed submission! Please retry!')
            console.log(res['msg'])
          }
        })
    }
  }
}
</script>

<style lang="scss">
.ml-task-form {
  background-color: #FFFFFF;
  width: 760px;
  margin: 14px auto;
  padding: 14px 20px;
  text-align: left;
  .select-data {
    width: 400px;
  }
  .select-label {
    width: 200px;
  }
  .select-model {
    width: 300px;
  }
  .select-cv-type {
    width: 200px;
  }
}
</style>
