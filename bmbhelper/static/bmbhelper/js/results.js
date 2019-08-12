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

new Vue({
  delimiters: ['[[', ']]'],
  el: '#app',
  data:{
    message: 'please-implement',
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
