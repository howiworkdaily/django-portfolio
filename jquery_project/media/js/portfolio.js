$(document).ready(function() {
    var index = -1;
    var images = $("#images");
    var len = images.children().length;

    var show_next = function() {
      index = (index+1) % len;
      $(images.children()).hide();
      $(images.children()[index]).show();
    }
    show_next();
    $("#images").click(show_next);
  });
