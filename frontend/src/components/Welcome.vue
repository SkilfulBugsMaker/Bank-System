<template>
  <v-container>
    <v-row>
      <v-col cols="8" offset="2" align="space-around">
        <h1 justify="center" class="py-6 display-1">Welcome to YuxuanGuo's Bank System</h1>
        <li class="body-1">Author: YuxuanGuo</li>
        <li class="body-1">ID: PB17111568</li>
        <li class="body-1">Code Repo: <a href="https://github.com/SkilfulBugsMaker/Bank-System">Bank-System</a></li>
        <h2 justify="center" class="my-4 title">How to lunch</h2>
        <li class="body-1">Need to add.</li>
        <h2 justify="center" class="my-4 title">Builtin data</h2>

        <v-card outlined class="my-4 px-4" v-for="(dType, idxType) in dataType" :key="idxType">
          <v-card-title>{{ dataType[idxType] }}</v-card-title>
          <v-simple-table>
            <template v-slot:default>
              <thead>
                <tr>
                  <th
                    class="text-left"
                    v-for="(dLabel, idxLabel) in label[idxType]"
                    :key="idxLabel"
                  >{{ dLabel }}</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(dOut, idxOut) in data[idxType]" :key="idxOut">
                  <td v-for="(dIn, idxIn) in dOut" :key="idxIn">{{ dIn }}</td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Welcome",

  data: () => ({
    dataType: ["Bank", "Staff", "Department", "Manager"],
    label: [
      ["Bank Name", "Bank City", "Bank assets"],
      [
        "Staff ID",
        "Staff Name",
        "Staff Phone",
        "Staff Address",
        "Staff Start Work Date",
        "Staff Department"
      ],
      [
        "Department ID",
        "Department Name",
        "Department Type",
        "Department Manager",
        "Bank of Department"
      ],
      ["Staff ID", "Manager ID"]
    ],
    data: [
      [
        ["Beijing Bank", "Beijing", 0.0],
        ["Shanghai Bank", "Shanghai", 0.0],
        ["Hefei Bank", "Hefei", 0.0],
        ["Nanjing Bank", "Nanjing", 0.0]
      ],
      [
        ["staff_1",
        "大司马",
        "13312312345",
        "芜湖市起飞区",
        "2012-08-17",
        "depart_1"],
        ["staff_2",
        "李姐",
        "13323323333",
        "理解市李姐万岁",
        "2019-08-31",
        "depart_3"],
        ["staff_3",
        "韩金龙",
        "13323311451",
        "这波市肉弹冲击",
        "2020-01-31",
        "depart_5"],
        ["staff_4",
        "神魔恋",
        "17344455555",
        "李在赣神魔市",
        "2020-01-01",
        "depart_2"],
        ["staff_5",
        "小王",
        "18912345678",
        "北京市海淀区",
        "2018-01-31",
        "depart_4"],
        ["staff_6",
        "小李",
        "13012345678",
        "合肥市包河区",
        "2018-02-28",
        "depart_2"],
        ["staff_7",
        "小郭",
        "18900011100",
        "合肥市蜀山区",
        "2018-10-31",
        "depart_3"],
        ["staff_8",
        "小史",
        "18912321232",
        "广东省深圳市",
        "2000-01-31",
        "depart_3"]
      ],
      [
        ["depart_1", "市场部", "普通", "staff_1", "Beijing Bank"],
        ["depart_2", "市场部", "普通", "staff_2", "Beijing Bank"],
        ["depart_3", "市场部", "特殊", "staff_3", "Shanghai Bank"],
        ["depart_4", "人事部", "普通", "staff_4", "Nanjing Bank"],
        ["depart_5", "人事部", "普通", "staff_5", "Hefei Bank"]
      ],
      [
        ["staff_1", "depart_1"],
        ["staff_2", "depart_2"],
        ["staff_3", "depart_3"],
        ["staff_4", "depart_4"],
        ["staff_5", "depart_5"]
      ]
    ]
  })
};
</script>
