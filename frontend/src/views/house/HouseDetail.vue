<template>
  <v-layout justify-center>
    <v-flex md8 xs16>
      <v-container fluid grid-list-md>
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
        <section class="content">
          <v-layout row justify-space-between>
            <v-flex md8>
              <h2 class="detailTitle">{{houseDetail.name === invalidName ? "Anonymous house" : houseDetail.name}}</h2>
            </v-flex>
            <v-flex md3 class="text-xs-right">
              <HouseEditModal :detail="houseDetail" v-show="authenticated"></HouseEditModal>
              <v-btn icon flat color="yellow darken-2" @click="handleLike(houseDetail,userDetail)" v-show="authenticated">
                <v-icon v-if="houseDetail.has_liked">star</v-icon>
                <v-icon v-else>star_border</v-icon>
              </v-btn>

            </v-flex>
          </v-layout>


          <v-divider></v-divider>
          <v-flex class="mt-2" xs>
            <el-carousel :autoplay="false" trigger="click" height="700px" :interval="6000" v-if="$vuetify.breakpoint.mdAndUp">
              <el-carousel-item  v-for="(img,i) in houseDetail.imgs_url" :key="i">
                <v-img :src="houseDetail.cover_img + img" style="margin-top: 10px"></v-img>
              </el-carousel-item>
            </el-carousel>
            <el-carousel :autoplay="false" trigger="click" height="300px" :interval="6000" v-else>
              <el-carousel-item  v-for="(img,i) in houseDetail.imgs_url" :key="i">
                <v-img :src="houseDetail.cover_img + img" style="margin-top: 10px"></v-img>
              </el-carousel-item>
            </el-carousel>
          </v-flex>

          <v-divider></v-divider>
          <v-flex class="mt-2 mb-2">
            <v-flex>
              <el-tag style="font-size: 15px">Price: {{houseDetail.price === invalidPrice ? "Unavailable" : houseDetail.price}}</el-tag>
              <el-tag type="info" v-show="$vuetify.breakpoint.mdAndUp"><span class="subtitle">Location: {{houseDetail.location}}</span></el-tag>
              <span v-if="houseDetail.closest_department">
                <el-tag style="font-size: 15px" type="success"><span>Department: {{houseDetail.closest_department.name}}</span></el-tag>
                <el-tag style="font-size: 15px" type="danger"><span>Distance: {{houseDetail.closest_department.distance.toFixed(2)}} km</span></el-tag>
              </span>
            </v-flex>
          </v-flex>
          <v-divider> </v-divider>

          <v-flex class="mt-4">
            <div class="description-font" v-html="markdownContent(houseDetail.description)" id="mdeditor"></div>
            <v-divider></v-divider>
          </v-flex>
          <v-flex class="mt-4" v-if="houseDetail.provider">
            <p class="description-font">Actions: </p>
            <v-btn  class="white--text yellow darken-2" @click="jumpToUrl(houseDetail.provider.url)">
              <v-icon>insert_link</v-icon>
              View site
            </v-btn>
            <v-btn color="orange" class="white--text" :href="'mailto:' + houseDetail.provider.email">
              <v-icon>email</v-icon>
              Email them
            </v-btn>
            <v-btn disabled class="white--text pink">
              <v-icon>phone</v-icon>
              Phone: {{houseDetail.provider.phone}}
            </v-btn>
          </v-flex>
        </section>

      </v-container>
    </v-flex>


    <v-flex md3 v-show="$vuetify.breakpoint.mdAndUp">
      <div class="mr-4 mt-4">
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
          to: '/house/'
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
    },
    jumpToUrl(url) {
      window.location.href = url
    },
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
