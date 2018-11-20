<template>
  <v-dialog
   v-model="dialogView"
   width="500"
  >
    <v-btn icon flat color="orange" slot="activator"><v-icon>edit</v-icon></v-btn>
    <v-card>
      <v-card-title
        class="headline grey lighten-2"
        primary-title
      >
        Edit House!
      </v-card-title>

      <form>
        <v-card-text>
            <v-container grid-list-md>
              <v-layout wrap>
                <v-flex xs12>
                  <v-text-field
                    name="name"
                    label="* Name"
                    required
                    v-validate="'required'"
                    v-model="detail.name"
                    :error-messages="errors.collect('name')"
                    data-vv-name="name"
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md6>
                  <v-text-field
                    name="price"
                    label="* Price"
                    equired
                    v-validate="'required|numeric'"
                    v-model="detail.price"
                    :error-messages="errors.collect('price')"
                    data-vv-name="price"
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md6>
                  <v-text-field
                    name="location"
                    label="Location"
                    hint="the address of this house"
                    v-model="detail.location"
                  ></v-text-field>
                </v-flex>
                <v-flex xs12>
                  <v-text-field
                    name="imgs_url"
                    label="Image url"
                    v-model="detail.imgs_url"
                    v-validate="'url'"
                    :error-messages="errors.collect('imgs_url')"
                    data-vv-name="imgs_url"
                  ></v-text-field>
                </v-flex>
                <v-textarea
                  name="description"
                  label="* Description"
                  hint="Hint: the size/service/furniture..."
                  v-validate="'required'"
                  v-model="detail.description"
                  required
                  :error-messages="errors.collect('description')"
                  data-vv-name="description"
                ></v-textarea>

              </v-layout>
            </v-container>
        </v-card-text>
      </form>

      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          color="green"
          flat
          @click="submit(detail)"
        >
          Edit
        </v-btn>
        <v-btn
          color="primary"
          flat
          @click="dialogView = false"
        >
          Cancel
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>

export default {
  name: "HouseEditModal",
  props: ["detail"],
  data: () => {
    return {
      dialogView: false,
      house: {
        name: '',
        price: 0,
        cover_img: '',
        imgs_url: '',
        location: '',
        description: '',
      }
    }
  },
  watch: {
    detail: function(newVal,oldVal){
      this.house = newVal;
    }
  },
  methods: {
    submit (house) {
      let splitedURL = house.imgs_url.split('/')
      let originalURL = house.imgs_url
      house.imgs_url = splitedURL[splitedURL.length - 1]
      house.cover_img = originalURL.slice(0, (originalURL.length - house.imgs_url.length))
      house.imgs_url = [splitedURL[splitedURL.length - 1]]

      this.$validator.validateAll().then((isvalid) => {
        if(!isvalid) {
          this.$notify({
            title: "Edit failed",
            type: "error",
            message: "The input fields are invalid!"
          })
          return
        }
        this.editHouse(house)
        this.dialogView = false
      })
    },
    editHouse: function (house) { // No arrow function here...
      this.$store.dispatch('house/editHouseObj', { data: house, id: this.$route.params.id }).then(() => {
        this.$notify({
          title: "Edit successfully",
          type: "success",
          message: "You have edited the house."
        })
      })
    }
  }
}
</script>

<style scoped>

</style>
