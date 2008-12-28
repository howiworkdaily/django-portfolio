$(document).ready(function() {
    var index = -1;
    var images = $("#images");
    var len = images.children('li').length;
    var make_counter = function() {
      return $("<span id=\"counter\">" + (index+1) + "/" + len + "</span>");
    }

    

    var show_next = function() {
      index = (index+1) % len;
      $(images.children('li')).hide();
      $(images.children('li')[index]).show();
      $("#counter").replaceWith(make_counter());
    }
    
    $("#images").prepend(make_counter());
    
    show_next();
    $("#images").click(show_next);
  });
