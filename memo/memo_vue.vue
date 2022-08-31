{
    "#p": "post() {
        this.$axios
          .post(`/admin/misc/event`, formPost)
          .then((response) => {
            if (response.data.success == 'success') {
              //this.resetForm();
              alert('สร้างlllll สำเร็จ');
            } else {
              console.log(response.data);
            }
          })
          .catch((error) => {
            console.log(error);
          });
      },",
    "#g": "font_get",
    "#d": "font_delete",
    "#r": "<row >\n<v-col cols='12' lg='6' md='5'>lllll</v-col>\n</v-row>",
    "#ima": "<v-card class='rounded-lg-plus' e='0'><v-img :src'`image`' :as/></v-card>",

    "$g": "g",

    "@ac": "a",
    "@ct": "a"
}