<template>
  <v-layout justify-center>

    <v-flex>
      <v-container fluid grid-list-md>

        <v-layout row wrap justify-space-between>
          <v-flex md8 xs12>
          <el-carousel type="card">
              <el-carousel-item v-for="(item,i) in houses" :key="i" :src="item.cover_img">
                <v-layout justify-center>
                  <img :src="item.cover_img + item.imgs_url[0]"/>
                  <h4 class="white--text ml-1 carousel-title">{{item.name}}</h4>
                </v-layout>
              </el-carousel-item>
            </el-carousel>
          </v-flex>

          <v-flex md3 v-show="$vuetify.breakpoint.mdAndUp">
            <div class="mr-3" style="position:fixed;">
              <HouseSuggestionCard :houses="houses.slice(0,3)"></HouseSuggestionCard>
              <RoommateCard></RoommateCard>
            </div>
          </v-flex>

          <v-flex md8>
            <v-layout row justify-space-between>
              <v-flex md3>
                <h1>House list</h1>
              </v-flex>
              <v-flex md5 class="text-xs-right list-header-bar">
                <HouseCreateModal v-show="authenticated"></HouseCreateModal>
                <HouseFilter></HouseFilter>

                <el-dropdown trigger="click">
                  <v-btn flat><v-icon>sort</v-icon>Sort</v-btn>
                  <el-dropdown-menu slot="dropdown">
                    <div v-for="(key,i) in sortMethods" :key="i">
                      <div @click="() => toRoute('',{},key.param)">
                        <el-dropdown-item >{{key.name}}</el-dropdown-item>
                      </div>
                    </div>
                  </el-dropdown-menu>
                </el-dropdown>

              </v-flex>
              </v-layout>
            <v-divider></v-divider>
          </v-flex>

          <v-flex md8>
            <v-layout row wrap>


              <v-flex v-if="houses.length > 0" v-for="item in houses" v-bind="{ [`xs${item.flex}`]: true }" :key="item.id" xs12 md12>
                <v-hover>
                  <v-card class="mt-3" slot-scope="{ hover }" :class="`elevation-${hover ? 6 : 2}`">
                    <v-layout row>
                      <v-flex md3 v-show="$vuetify.breakpoint.mdAndUp" >
                        <v-card :to="'/house/'+item.id">
                          <v-img :src="item.cover_img + item.imgs_url[0]" @click.stop="$router.push(item.id)"></v-img>
                        </v-card>
                      </v-flex>
                      <v-flex md9 xs12>
                        <v-card-title class="pb-2">
                          <div class="headline">{{item.name === invalidName ? "Anonymous house" : item.name}}</div>
                          <br>
                        </v-card-title>
                          <v-card-text class="pt-2" >
                            <h4>Price:
                              <span v-if="item.price !== invalidPrice" style="color: orange">${{item.price}}</span>
                              <span v-else style="color: grey">Unavailable</span>
                            </h4>
                            <div v-show="item.closest_department">
                              <span>Closest Department:
                                <span style="color: orangered">{{item.closest_department.name}}</span>
                              </span>
                              <br>
                              <span>Distance:
                                <span style="color: dodgerblue">{{item.closest_department.distance.toFixed(2)}} km</span>
                              </span>
                            </div>
                            <br>
                            <span class="grey--text">Location: {{item.location}}</span><br>
                            <span class="grey--text">{{item.description.slice(0,200)}}...</span>
                          </v-card-text>
                        <v-card-actions>
                          <v-btn  flat color="green" :to="'/house/'+item.id"><v-icon>details</v-icon>Detail</v-btn>
                          <div v-show="authenticated">
                            <v-btn flat color="orange" @click="handleLike(item,userDetail)"><v-icon>{{item.has_liked ? "star" : "star_border"}}
                            </v-icon>Likes: {{item.like_count ? item.like_count : 0}}</v-btn>
                          </div>
                          <div v-show="authenticated">
                            <el-popover trigger="click" placement="top" v-model="item.popover">
                              <p>Do you want to delete the house? (This operation is irrevocable)</p>
                              <div style="text-align: right; margin: 0">
                                <v-btn flat color="green" @click="item.popover = false">Cancel</v-btn>
                                <v-btn flat color="red" @click="deleteHouse(item.id)">Delete</v-btn>
                              </div>
                              <v-btn flat color="red" slot="reference"><v-icon>close</v-icon>Delete</v-btn>
                            </el-popover>
                          </div>
                        </v-card-actions>
                      </v-flex>
                    </v-layout>
                  </v-card>
                </v-hover>
              </v-flex>
              <v-flex v-else xs12 md12>
                <v-layout justify-align-center justify-center>
                    <h1 class="display-2 mt-5">No house found <v-icon style="font-size:60px">sentiment_very_dissatisfied</v-icon></h1>
                </v-layout>
              </v-flex>

            </v-layout>
          </v-flex>

        </v-layout>
        <v-flex md12 class="mt-3">
          <div class="text-xs-center">
              <el-pagination
                layout="prev, pager, next"
                :total="totalNums"
                :currentPage="this.$route.query.page ? parseInt(this.$route.query.page) : 1"
                @current-change="(page) => toRoute('',{}, {page: page})"
                @next-click="(page) => toRoute('',{}, {page: page})"
                @prev-click="(page) => toRoute('',{}, {page: page})"
              >
              </el-pagination>
            </div>
        </v-flex>

      </v-container>
    </v-flex>
  </v-layout>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'HouseList',
  components: {
    "HouseCreateModal": () => import('./HouseCreateModal.vue'),
    "HouseFilter": () => import('./HouseFilter.vue'),
    "HouseSuggestionCard": () => import('./HouseSuggestionCard.vue'),
    "RoommateCard": () => import('./RoommateCard.vue'),
  },
  created() {
    const query = this.$route.query
    this.$store.dispatch('house/getList', query)
  },
  data: () => {
    return {
      sortMethods: [
        {name: "Price Low to High", param: {srule: "price-low-to-high"}},
        {name: "Price High to Low", param: {srule: "price-high-to-low"}},
        {name: "Likes High to Low", param: {srule:"like-high-to-low"}},
        {name: "Likes Low to High", param: {srule:"like-low-to-high"}},
        {name: "House name A - Z", param: {srule:"name-ascending"}},
        {name: "House name Z - A", param: {srule:"name-descending"}},
      ],
      invalidName: 'Please Select Your Suite',
      invalidPrice: 9999,
    }
  },
  computed: mapState({
    totalNums: state => state.house.list.count,
    houses: state => state.house.list.results,
    providers: state => state.provider.list.results,
    departments: state => state.department.list,
    currentPage: () => {
      const query = this.$route.query
      return query.page ? parseInt(query.page) : 1
    },
    authenticated: state => state.user.detail.id !== -1,
    userDetail: state => state.user.detail,
  }),
  methods: {
    deleteHouse: function (id) { // No arrow function here...
      this.$store.dispatch('house/deleteHouseObj',id).then(() => {
        this.$notify({
          title: "Delete successfully",
          type: "success",
          message: "Your chosen house has been deleted."
        })
      })
    },
    toRoute (rname, rparams = {}, query = {}) {
      this.$router.push({path: rname, params: rparams, query: query})
    },
    handleLike(house,user) {
      let data = {house_id: house.id, user_id: user.id}
      this.$store.dispatch('house/likeHouseList',data).then(() => {
        house.has_liked = !house.has_liked
        if(house.like_count) {
          if(house.has_liked) house.like_count -= 1
          else house.like_count += 1
        }

      })
    }
  }
}
</script>

<style scoped>
.carousel-title {
  position: absolute;
  bottom: 20%;
  font-size: 20px;
}
</style>
