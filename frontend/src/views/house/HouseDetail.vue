<template>
  <v-layout row wrap justify-space-between>
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

        <section class="content">
          <v-layout row justify-space-between>
            <v-flex md3>
              <h2 class="detailTitle">{{house.name}}</h2>
            </v-flex>
            <v-flex md3 class="text-xs-right">
              <HouseEditModal :detail="house" v-show="authenticated"></HouseEditModal>
            </v-flex>
          </v-layout>
          <v-divider></v-divider>
          <v-flex class="mt-2">
            <div style="margin-bottom: 10px">
              <div>
                <el-tag>Price: {{house.price}}</el-tag> <el-tag type="info"><span class="subtitle">Location: {{house.location}}</span></el-tag>
              </div>
            </div>
            <v-divider> </v-divider>
            <el-carousel autoplay=false trigger="click" height="700px" interval="6000">
              <el-carousel-item  v-for="img in house.imgs_url" :key="item">
                <v-img :src="house.cover_img + img" style="margin-top: 10px"></v-img>
              </el-carousel-item>
            </el-carousel>

          </v-flex>
          <v-flex class="mt-4">
            <div v-html="markdownContent(house.description)" id="mdeditor"></div>
          </v-flex>
        </section>

        <section class="markdown-editor">
          <v-layout style="max-height: 500px;" column>
            <v-flex>
              <mavon-editor language="en"/>
            </v-flex>
            <v-flex md4>
              <v-list>
                 <v-btn class="primary align-right">Submit</v-btn>
                 <v-btn class="danger align-right">Reset</v-btn>
              </v-list>
            </v-flex>
            <v-divider></v-divider>
          </v-layout>
        </section>
      </v-container>
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
  },
  created() {
    this.$store.dispatch('house/getHouseDetailObj',this.$route.params.id)
  },
  computed: mapState({
    house: state => state.house.detail,
    authenticated: state => state.user.detail.id !== -1,
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
    }
  },
  methods: {
    markdownContent: (content) => {
      return marked(content, { sanitize: true })
    }
  }
}
</script>

<style scoped lang="less">
.subtitle {
  font-size: 10px;
  color: grey;
}
.content {
  padding: 16px;
  .detailTitle {
    font-size: 20px;
  }
}

.markdown-editor {
  padding: 16px;
}
</style>
