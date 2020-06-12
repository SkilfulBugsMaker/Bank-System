<template>
  <v-container>
    <!-- <v-row align="center" justify="center" class="display-1 py-4">Customer Management</v-row> -->
    <v-row>
      <v-col>
        <v-card flat>
          <v-tabs fixed-tabs v-model="tab">
            <v-tab v-for="(op, idx) in operations" :key="idx">{{ op }}</v-tab>
          </v-tabs>
          <v-tabs-items v-model="tab">
            <v-tab-item v-for="(op, idx) in operations" :key="idx">
              <v-card outlined class="my-4 px-4">
                <v-card-title>{{ cardOneTitle[idx] }}</v-card-title>
                <v-form>
                  <v-row>
                    <v-col cols="2">
                      <v-text-field
                        v-model="inputData.id"
                        counter="256"
                        label="Customer ID"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="2">
                      <v-text-field
                        v-model="inputData.name"
                        counter="256"
                        label="Customer Name"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="2">
                      <v-text-field
                        v-model="inputData.phone"
                        counter="256"
                        label="Customer Phone"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="6">
                      <v-text-field
                        v-model="inputData.address"
                        counter="256"
                        label="Customer Address"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col cols="2">
                      <v-text-field
                        v-model="inputData.contactName"
                        counter="256"
                        label="Contact Name"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="2">
                      <v-text-field
                        v-model="inputData.contactPhone"
                        counter="256"
                        label="Contact Phone"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="2">
                      <v-text-field
                        v-model="inputData.contactEmail"
                        counter="256"
                        label="Contact Email"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="2">
                      <v-text-field
                        v-model="inputData.contactRelationship"
                        counter="256"
                        label="Contact Relationship"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="2">
                      <v-text-field
                        v-model="inputData.loanStaffID"
                        counter="256"
                        label="Loan Staff ID"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="2">
                      <v-text-field
                        v-model="inputData.accountStaffID"
                        counter="256"
                        label="Account Staff ID"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-form>
              </v-card>
              <v-card outlined class="my-4 px-4" v-if="idx==2">
                <v-card-title>更新后的用户信息</v-card-title>
                <v-form>
                  <v-row>
                    <v-col cols="2">
                      <v-text-field
                        v-model="modifyData.id"
                        counter="256"
                        label="Customer ID"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="2">
                      <v-text-field
                        v-model="modifyData.name"
                        counter="256"
                        label="Customer Name"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="2">
                      <v-text-field
                        v-model="modifyData.phone"
                        counter="256"
                        label="Customer Phone"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="6">
                      <v-text-field
                        v-model="modifyData.address"
                        counter="256"
                        label="Customer Address"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col cols="2">
                      <v-text-field
                        v-model="modifyData.contactName"
                        counter="256"
                        label="Contact Name"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="2">
                      <v-text-field
                        v-model="modifyData.contactPhone"
                        counter="256"
                        label="Contact Phone"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="2">
                      <v-text-field
                        v-model="modifyData.contactEmail"
                        counter="256"
                        label="Contact Email"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="2">
                      <v-text-field
                        v-model="modifyData.contactRelationship"
                        counter="256"
                        label="Contact Relationship"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="2">
                      <v-text-field
                        v-model="modifyData.loanStaffID"
                        counter="256"
                        label="Loan Staff ID"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="2">
                      <v-text-field
                        v-model="modifyData.accountStaffID"
                        counter="256"
                        label="Account Staff ID"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-form>
              </v-card>
              <v-card flat class="my-4 px-4">
                <v-row>
                    <v-col cols="2" offset="4">
                      <v-btn :disabled="!commitBtnValid" color="success" @click="commitForm">Commit</v-btn>
                    </v-col>
                    <v-col cols="2">
                      <v-btn :disabled="!resetBtnValid" color="warning" @click="resetForm">Reset</v-btn>
                    </v-col>
                  </v-row>
              </v-card>
              <v-divider class="py-2"></v-divider>
              
              <v-card outlined>
                <v-card-title> {{ cardStatusTitle[idx] }}</v-card-title>
              </v-card>
            </v-tab-item>
          </v-tabs-items>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "CustomerManage",

  data: () => ({
    tab: 0,
    operations: ["Create", "Delete", "Modify", "Search"],
    cardOneTitle: [
      "需要创建的用户的信息",
      "需要删除的用户的信息",
      "更新前的用户信息",
      "需要搜索的用户信息"
    ],
    cardStatusTitle: [
      "创建用户状态",
      "删除用户状态",
      "更新用户状态",
      "搜索用户状态"
    ],
    inputData: {
      id: "",
      name: "",
      phone: "",
      address: "",
      loanStaffID: "",
      accountStaffID: "",
      contactName: "",
      contactPhone: "",
      contactEmail: "",
      contactRelationship: ""
    },
    modifyData: {
      id: "",
      name: "",
      phone: "",
      address: "",
      loanStaffID: "",
      accountStaffID: "",
      contactName: "",
      contactPhone: "",
      contactEmail: "",
      contactRelationship: ""
    }
  }),
  computed: {
    formOneEmpty: function () {
      let result = (this.inputData['id'].length == 0)
      for (let item in this.inputData) {
        result = result && (this.inputData[item].length == 0)
      }
      return result
    },
    formTwoEmpty: function () {
      let result = (this.modifyData['id'].length == 0)
      for (let item in this.modifyData) {
        result = result && (this.modifyData[item].length == 0)
      }
      return result
    },
    checkFormOneCreate: function () {
      let result = true
      for (let item in this.inputData) {
        if (item == 'loanStaffID' || item == 'accountStaffID') {
          continue
        }
        result = result && (this.inputData[item] != '')
      }
      return result
    },
    resetBtnValid: function () {
      let result = false
      if (this.tab == 2) {
        // if modify
        result = (!this.formOneEmpty) || (!this.formTwoEmpty)
      } else {
        result = !this.formOneEmpty
      }
      return result
    },
    commitBtnValid: function () {
      let result = false
      if (this.tab == 0) {
        // if modify
        result = this.checkFormOneCreate
      } else if (this.tab == 1) {
        result = !this.formOneEmpty
      } else if (this.tab == 2) {
        result = (!this.formOneEmpty) && (!this.formTwoEmpty)
      } else {
        result = !this.formOneEmpty
      }
      return result
    },
  },
  methods: {
    resetForm: function () {
      for (let item in this.inputData) {
        this.inputData[item] = ''
      }
    },
    commitForm: function () {
      alert(this.checkFormOneCreate)
    }
  }
};
</script>
