<template>
<v-dialog v-model="dialog" max-width="800px">
  <v-card-title
        class="headline orange lighten-2 white--text"
        primary-title
      >
        Advanced Filter
      </v-card-title>
  <v-list three-line subheader>
    <v-subheader>Properties</v-subheader>

    <v-list-tile avatar>
      <v-list-tile-content>
        <v-list-tile-title>Department</v-list-tile-title>
        <v-list-tile-sub-title>Set the department to get the houses nearest to this department</v-list-tile-sub-title>
        <v-list-tile-sub-title class="mt-1">
          <el-select  v-show="departments" v-model="filter.department"
                   filterable clearable placeholder="Choose a department" no-data-text="No data" no-match-text="No matching">
            <el-option
              v-for="item in departments"
              :key="item.id"
              :label="item.name"
              :value="item.id">
            </el-option>
        </el-select>
        </v-list-tile-sub-title>

      </v-list-tile-content>
    </v-list-tile>

    <v-list-tile avatar  class="mb-2">
      <v-list-tile-content>
        <v-list-tile-title>Provider</v-list-tile-title>
        <v-list-tile-sub-title>Set the provider here</v-list-tile-sub-title>
        <v-list-tile-sub-title class="mt-1">
           <el-select v-show="providers" v-model="filter.provider"
                   filterable clearable placeholder="Choose a provider" no-data-text="No data" no-match-text="No matching">
            <el-option
              v-for="item in providers"
              :key="item.id"
              :label="item.name"
              :value="item.id">
            </el-option>
          </el-select>
        </v-list-tile-sub-title>

      </v-list-tile-content>
    </v-list-tile>

    <v-divider></v-divider>

    <v-list three-line subheader>
      <v-subheader>Price</v-subheader>
      <v-layout row wrap>
        <v-flex xs1>
          <v-text-field v-model="filter.price[0]"  class="price-textfield mr-0 slider" type="number" color="yellow darken-1"></v-text-field>
        </v-flex>

        <v-flex xs10>
          <v-range-slider v-model="filter.price" class="slider" :max="6000" :min="0" :step="10" color="yellow darken-1"></v-range-slider>
        </v-flex>

        <v-flex xs1>
          <v-text-field class="price-textfield ml-0 slider" v-model="filter.price[1]" type="number" color="yellow darken-1"></v-text-field>
        </v-flex>
      </v-layout>
    </v-list>

    <v-divider></v-divider>

    <v-list three-line subheader>
      <v-subheader>General</v-subheader>
      <v-list-tile avatar>
        <v-list-tile-action>
          <v-checkbox v-model="filter.like" color="yellow darken-1"></v-checkbox>
        </v-list-tile-action>
        <v-list-tile-content>
          <v-list-tile-title>Houses I Like</v-list-tile-title>
          <v-list-tile-sub-title>The houses marked as liked.</v-list-tile-sub-title>
        </v-list-tile-content>
      </v-list-tile>
      <v-list-tile avatar>
        <v-list-tile-action>
          <v-checkbox v-model="filter.suggestion" color="yellow darken-1"></v-checkbox>
        </v-list-tile-action>
        <v-list-tile-content>
          <v-list-tile-title>Suggestion</v-list-tile-title>
          <v-list-tile-sub-title>The suggested houses based on our suggestion algorithm.</v-list-tile-sub-title>
        </v-list-tile-content>
      </v-list-tile>
    </v-list>
  </v-list>

  <v-divider></v-divider>
  <v-list three-line subheader>
    <v-card-actions>
       <v-spacer></v-spacer>
        <v-btn color="blue" flat @click="resetFilter">Reset</v-btn>
        <v-btn color="green" @click="submit(filter)"flat>Submit</v-btn>
    </v-card-actions>

  </v-list>

  <v-btn flat slot="activator"><v-icon>filter</v-icon>Filter</v-btn>
</v-dialog>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name: "HouseFilter",
  created() {
    this.filter = this.getFilterFromURL(this.$router.history.current.query)
    this.$store.dispatch('provider/getList')
    this.$store.dispatch('department/getList')
  },
  data: () => {
    return {
      filter: {
        price: [0,6000],
        department: "",
        provider: "",
        like: false,
        suggestion: false,
      },
      dialog: false,
    }
  },
  computed: mapState({
    providers: state => state.provider.list.results,
    departments: state => state.department.list.results,
  }),
  methods: {
    resetFilter() {
      this.filter  = {
        price: [0,6000],
        department: "",
        provider: "",
        like: false,
        suggestion: false,
      }
    },
    getFilterFromURL(query) {
      let filter = {
        price: [0,6000],
        department: "",
        provider: "",
        like: false,
        suggestion: false,
      }
      filter.price[0] = query.minprice ? query.minprice : 0
      filter.price[1] = query.maxprice ? query.maxprice : 6000
      filter.department = query.department ? parseInt(query.department) : ""
      filter.provider = query.provider ? parseInt(query.provider) : ""
      filter.like = query.like && true
      filter.suggestion = query.suggestion && true
      return filter
    },
    submit(filter) {
      let query = {}
      if (filter.price[0] !== 0 || filter.price[1] !== 6000) {
        query.minprice = filter.price[0]
        query.maxprice = filter.price[1]
      }
      if (filter.department !== "") query.department = filter.department
      if (filter.provider !== "")query.provider = filter.provider
      if (filter.suggestion) query.suggestion = true
      if (filter.like) query.like = true

      this.toRoute('', {}, query)

      this.dialog = false // todo: route the url
    },
    toRoute (rname, rparams = {}, query = {}) {
      this.$router.push({path: rname, params: rparams, query: query})
    },
  },
}
</script>

<style scoped>
.price-textfield {
  padding-top: 0px;
  font-size: 15px;
}
.slider {
  margin: 0 20px;
}

</style>
