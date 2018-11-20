<template>
  <v-dialog
   v-model="dialogView"
   width="500"
  >
    <div slot="activator"><v-icon>flag</v-icon>Sign Up</div>
    <v-card>
      <v-card-title
        class="headline orange lighten-2 white--text"
        primary-title
      >
        SignUp here!
      </v-card-title>
      <form>
        <v-card-text>
            <v-container grid-list-md>
              <v-layout wrap>
                <v-flex xs12>
                  <v-text-field
                    name="email"
                    label="* Email"
                    required
                    type="email"
                    v-validate="'required'"
                    v-model="input.email"
                    :error-messages="errors.collect('email')"
                    data-vv-name="email"
                  ></v-text-field>
                </v-flex>
                <v-flex xs12>
                  <v-text-field
                    name="username"
                    label="* Username"
                    required
                    v-validate="'required'"
                    v-model="input.username"
                    :error-messages="errors.collect('username')"
                    data-vv-name="username"
                  ></v-text-field>
                </v-flex>
                <v-flex xs12>
                  <v-text-field
                    name="password"
                    ref="password"
                    label="* Password"
                    v-model="input.password"
                    type="password"
                    v-validate="'required'"
                    required
                    :error-messages="errors.collect('password')"
                    data-vv-name="password"
                  ></v-text-field>
                </v-flex>
                <v-flex xs12>
                  <v-text-field
                    name="repeatPassword"
                    ref="repeatPassword"

                    label="* Repeat Password"
                    v-model="input.repeatPassword"
                    type="password"
                    v-validate="'required|confirmed:password'"
                    required
                    :error-messages="errors.collect('repeatPassword')"
                    data-vv-name="repeatPassword"
                  ></v-text-field>
                </v-flex>
                <v-flex>
                  <el-select v-model="input.department" class="mt-2"
                   filterable placeholder="Your department" no-data-text="No data" no-match-text="No matching">
                    <el-option
                      v-for="item in departments"
                      :key="item.id"
                      :label="item.name"
                      :value="item.id">
                    </el-option>
                </el-select>
                </v-flex>
                <v-flex>
                  <v-list-tile-action>
                     <v-checkbox
                       name="remember"
                       :label="'Remember me?'"
                       v-model="input.remember"
                       :error-messages="errors.collect('remember')"
                       color="orange"
                       data-vv-name="remember"
                      ></v-checkbox>
                  </v-list-tile-action>
                </v-flex>

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
          @click="submit(input)"
        >
          Sign Up
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
import { mapState } from 'vuex'
export default {
  name: "SignUpModal",
  data: () => {
    return {
      dialogView: false,
      input: {
        email: '',
        username: '',
        password: '',
        repeatPassword: '',
        remember: false,
        department: '',
      }
    }
  },
  computed: mapState({
    departments: state => state.department.list,
  }),
  methods: {
    submit (input) {
      this.$validator.validateAll().then((isvalid) => {
        if(!isvalid) {
          this.$notify({
            title: "Create failed",
            type: "error",
            message: "The input fields are invalid!"
          })
          return
        }
        this.signup(input)
        this.dialogView = false
      })
    },
    signup: function (input) { // No arrow function here...
      console.log(input)
      this.$store.dispatch('user/signup',input).then(() => {
      })
      let store = this.$store
      let notify = this.$notify
      setTimeout(() => {
        if(!store.state.user.status) {
        this.$notify.error({
          title: "Signup Failed",
          message: "Check your username/password again."
        })
        return
      }
      notify({
        title: "Signup successfully",
        type: "success",
        message: "Your account is available now!"
      })
      },1400)

    }
  }
}
</script>

<style scoped>

</style>
