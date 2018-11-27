webpackJsonp([14],{VeAd:function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var r={name:"LoginModal",data:function(){return{dialogView:!1,input:{username_or_email:"",password:"",remember:!1}}},methods:{submit:function(e){var t=this;this.$validator.validateAll().then(function(a){a?(t.login(e),t.dialogView=!1):t.$notify({title:"Create failed",type:"error",message:"The input fields are invalid!"})})},login:function(e){var t=this;this.$store.dispatch("user/login",e).then(function(){});var a=this.$store,r=this.$notify;setTimeout(function(){a.state.user.status?(r({title:"Login successfully",type:"success",message:"You have login successfully."}),t.$router.push("/"),window.location.reload()):t.$notify.error({title:"Signin Failed",message:"Check your username/password again."})},2e3)}}},i={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-dialog",{attrs:{width:"500"},model:{value:e.dialogView,callback:function(t){e.dialogView=t},expression:"dialogView"}},[a("div",{attrs:{slot:"activator"},slot:"activator"},[a("v-icon",[e._v("exit_to_app")]),e._v("Sign in")],1),e._v(" "),a("v-card",[a("v-card-title",{staticClass:"headline orange lighten-2 white--text",attrs:{"primary-title":""}},[e._v("\n      Login here!\n    ")]),e._v(" "),a("form",[a("v-card-text",[a("v-container",{attrs:{"grid-list-md":""}},[a("v-layout",{attrs:{wrap:""}},[a("v-flex",{attrs:{xs12:""}},[a("v-text-field",{directives:[{name:"validate",rawName:"v-validate",value:"required",expression:"'required'"}],attrs:{name:"username_or_email",label:"* Username or Email",required:"","error-messages":e.errors.collect("username_or_email"),"data-vv-name":"username_or_email"},model:{value:e.input.username_or_email,callback:function(t){e.$set(e.input,"username_or_email",t)},expression:"input.username_or_email"}})],1),e._v(" "),a("v-flex",{attrs:{xs12:""}},[a("v-text-field",{directives:[{name:"validate",rawName:"v-validate",value:"required",expression:"'required'"}],attrs:{name:"password",label:"* Password",required:"",type:"password","error-messages":e.errors.collect("password"),"data-vv-name":"password"},model:{value:e.input.password,callback:function(t){e.$set(e.input,"password",t)},expression:"input.password"}})],1),e._v(" "),a("v-flex",[a("v-list-tile-action",[a("v-checkbox",{attrs:{name:"remember",label:"Remember me?","error-messages":e.errors.collect("remember"),color:"orange","data-vv-name":"remember"},model:{value:e.input.remember,callback:function(t){e.$set(e.input,"remember",t)},expression:"input.remember"}})],1)],1)],1)],1)],1)],1),e._v(" "),a("v-divider"),e._v(" "),a("v-card-actions",[a("v-spacer"),e._v(" "),a("v-btn",{attrs:{color:"green",flat:""},on:{click:function(t){e.submit(e.input)}}},[e._v("\n        Sign in\n      ")]),e._v(" "),a("v-btn",{attrs:{color:"primary",flat:""},on:{click:function(t){e.dialogView=!1}}},[e._v("\n        Cancel\n      ")])],1)],1)],1)},staticRenderFns:[]};var s=a("VU/8")(r,i,!1,function(e){a("k3Gw")},"data-v-75292482",null);t.default=s.exports},k3Gw:function(e,t){}});
//# sourceMappingURL=14.c396e6b89eace3994c96.js.map