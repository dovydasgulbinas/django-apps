Vue.component('meta-line', {
  delimiters: ['[[', ']]'],
  props: ['field', 'value'],
  template: `
    <tr>
        <th>[[ field ]]:</th>
        <td>[[ value ]]</td>
    </tr>
    `
})

var bmb_album_meta = new Vue({
delimiters: ['[[', ']]'],
  el: '#album-meta',
  data: {
    title: 'Welcome to My Journal'
  }
})


new Vue({
  delimiters: ['[[', ']]'],
  el: '#app',
  data:{
    message: 'xD',
  },
  methods: {
    onCopy: function (e) {
       console.log(e.text);
    },
    onError: function (e) {
       console.log('Failed to copy texts')
    }
  }
})
