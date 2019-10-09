


// Write VUE code here :)
var radioapp = new Vue({

    el: '#radioapp',
    data: {
    message: 'Hello Vue!',
    searchTerm: 'Techno',
    info: null,

    stations: [
        {id: 0, name: 'Cancer', genres: 'dubstep, canker', currentTrack: 'hew - brew', streamurl:'http://185.33.21.112:80/dance_128'},
        {id: 2, name: 'c2', genres: 'dubstep', currentTrack: 'jimmy - billy', streamurl:'http://strm112.1.fm/dubstep_mobile_mp3'},
    ],
    searchMode: 'station',
  },

  // data ends
  methods: {
        onSearchEnter: function() {
            var msg = `${this.searchTerm}, ${this.searchMode}`;
            NAME_SEARCH_URL = `http://rad.io/info/index/searchembeddedbroadcast?q=${this.searchTerm}&start=0&rows=10&streamcontentformats=aac,mp3`

var data = null;
var xhr = new XMLHttpRequest();
xhr.withCredentials = true;

xhr.addEventListener("readystatechange", function () {
  if (this.readyState === 4) {
    console.log(this.responseText);
  }
});

xhr.open("GET", "http://rad.io/info/index/searchembeddedbroadcast?q=1.%20fm&start=0&rows=200&streamcontentformats=aac,mp3");
xhr.setRequestHeader("User-Agent", "XBMC Addon Radio");
xhr.setRequestHeader("Cache-Control", "no-cache");
xhr.setRequestHeader("Postman-Token", "812466e6-7519-05e4-7737-86c5f1adfd50");

xhr.send(data);




          //  alert(msg);
        }
    }
})
