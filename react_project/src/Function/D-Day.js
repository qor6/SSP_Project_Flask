var dday = new Date("January 1, 2022, 0:00:00").getTime();

setInterval(function() {
  var today = new Date().getTime();
  var gap = dday - today;
  var day = Math.ceil(gap / (1000 * 60 * 60 * 24));
  //var hour = Math.ceil((gap % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  //var min = Math.ceil((gap % (1000 * 60 * 60)) / (1000 * 60));
  //var sec = Math.ceil((gap % (1000 * 60)) / 1000);

  document.getElementById("count").innerHTML = "D-DAY - " + day;
}, 1000);
