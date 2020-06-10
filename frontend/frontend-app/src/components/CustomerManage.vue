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
                  <v-row>
                    <v-col cols="2" offset="4">
                      <v-btn :disabled="formEmpty" color="success" @click="commitForm">Commit</v-btn>
                    </v-col>
                    <v-col cols="2">
                      <v-btn :disabled="formEmpty" color="warning" @click="resetForm">Reset</v-btn>
                    </v-col>
                  </v-row>
                </v-form>
              </v-card>
              <v-divider class="py-2"></v-divider>
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
    operations: ["Add", "Delete", "Modify", "Search"],
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
    }
  }),
  computed: {
    formEmpty: function () {
      let result = (this.inputData['id'].length == 0)
      for (let item in this.inputData) {
        result = result && (this.inputData[item].length == 0)
      }
      return result
    }
  },
  methods: {
    resetForm: function () {
      for (let item in this.inputData) {
        this.inputData[item] = ''
      }
    },
    commitForm: function () {
      alert(this.operations[this.tab])
    }
  }
};
</script>
