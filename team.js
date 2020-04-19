var resultView = new Vue({
  el: '#app',
  data () {
    return {
      art: [],
      audio: [],
      programming: [],
      design: [],
      all: []
    }
  }, //data

  beforeMount() {

    var reader = new FileReader();
    var data = $.get("file:///Users/striesenberg/WSOFT/wolverinesoftstudio.github.io/data/team.csv?origin=*");


    var record_num = 4;  // or however many elements there are in each row
    var allTextLines = allText.split(/\r\n|\n/);
    var entries = allTextLines[0].split(',');
    var lines = [];

    var headings = entries.splice(0,record_num);

    while (entries.length>0) {
      var tarr = [];
      for (var j=0; j<record_num; j++) {
        tarr.push(headings[j]+":"+entries.shift());
      }
      lines.push(tarr);
    }

    console.log(lines)



    console.log("hi")



  },


  mounted: function () {

  }
})
