<template>
  <v-layout justify-center>
    <v-flex md8>
      <v-container>
        <v-flex>

          <v-breadcrumbs>
            <el-breadcrumb separator-class="el-icon-arrow-right">
              <el-breadcrumb-item
                v-for="crumb in crumbs"
                :disabled="crumb.disabled"
                :key="crumb.text"
                :to="crumb.to"
              > {{ crumb.text }}
              </el-breadcrumb-item>
            </el-breadcrumb>
          </v-breadcrumbs>
        </v-flex>
        {{houseDetail.has_liked}}
        <section class="content">
          <v-layout row justify-space-between>
            <v-flex md8>
              <h2 class="detailTitle">{{houseDetail.name === invalidName ? "Anonymous house" : houseDetail.name}}</h2>
            </v-flex>
            <v-flex md3 class="text-xs-right">
              <HouseEditModal :detail="houseDetail" v-show="authenticated"></HouseEditModal>
              <v-btn icon flat color="yellow darken-2" @click="handleLike(houseDetail,userDetail)">
                <v-icon v-if="houseDetail.has_liked">star</v-icon>
                <v-icon v-else>star_border</v-icon>
              </v-btn>

            </v-flex>
          </v-layout>


          <v-divider></v-divider>
          <v-flex class="mt-2" xs>
            <el-carousel :autoplay="false" trigger="click" height="700px" :interval="6000">
              <el-carousel-item  v-for="(img,i) in houseDetail.imgs_url" :key="i">
                <v-img :src="houseDetail.cover_img + img" style="margin-top: 10px"></v-img>
              </el-carousel-item>
            </el-carousel>
          </v-flex>

          <v-divider></v-divider>
          <div class="mt-2 mb-2">
            <div>
              <el-tag style="font-size: 15px">Price: {{houseDetail.price === invalidPrice ? "Unavailable" : houseDetail.price}}</el-tag>
              <el-tag type="info"><span class="subtitle">Location: {{houseDetail.location}}</span></el-tag>
              <span v-show="houseDetail.closest_department">
                <el-tag style="font-size: 15px" type="success"><span>Department: {{houseDetail.closest_department.name}}</span></el-tag>
                <el-tag style="font-size: 15px" type="danger"><span>Distance: {{houseDetail.closest_department.distance.toFixed(2)}} km</span></el-tag>
              </span>
            </div>
          </div>
          <v-divider> </v-divider>

          <v-flex class="mt-4">
            <div class="description-font" v-html="markdownContent(houseDetail.description)" id="mdeditor"></div>
          </v-flex>
        </section>

      </v-container>
    </v-flex>


    <v-flex md3 v-show="$vuetify.breakpoint.mdAndUp">
      <div class="mr-3 mt-4" style="position:fixed;">
        <HouseSuggestionCard></HouseSuggestionCard>
        <RoommateCard></RoommateCard>
      </div>
    </v-flex>

  </v-layout>
</template>

<script>
import { marked } from '../../library/markedplus'
import { mapState } from 'vuex'
export default {
  name: 'HouseDetail',
  components: {
    'vmenu': () => import('./HouseMenu.vue'),
    "HouseEditModal": () => import('./HouseEditModal.vue'),
    "HouseSuggestionCard": () => import('./HouseSuggestionCard.vue'),
    "RoommateCard": () => import('./RoommateCard.vue'),
  },
  created() {
    this.$store.dispatch('house/getHouseDetailObj',this.$route.params.id)
  },
  computed: mapState({
    houseDetail: state => state.house.detail,
    authenticated: state => state.user.detail.id !== -1,
    userDetail: state => state.user.detail,
  }),
  data: () => {
    return {
      id: null,
      crumbs: [
        {
          text: 'Home',
          disabled: false,
          to: '/'
        },
        {
          text: 'House list',
          disabled: false,
          to: '/house'
        },
        {
          text: 'Detail',
          disabled: true
        }
      ],
      invalidName: 'Please Select Your Suite',
      invalidPrice: 9999,
    }
  },
  methods: {
    markdownContent: (content) => {
      return marked(content, { sanitize: true })
    },
    handleLike(house,user) {
      let data = {house_id: house.id, user_id: user.id}
      this.$store.dispatch('house/likeHouseObj',data).then(() => {
        house.has_liked = !house.has_liked
      })
    }
  }
}
</script>

<style scoped lang="less">
.subtitle {
  font-size: 15px;
  color: grey;
}
.content {
  padding: 16px;
  .detailTitle {
    font-size: 20px;
  }
}

.description-font {
  font-size: 18px;
}

.markdown-editor {
  padding: 16px;
}
</style>
