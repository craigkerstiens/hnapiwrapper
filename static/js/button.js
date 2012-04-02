(function() {
var write_string="<iframe src=\"http://hnapiwrapper.herokuapp.com/button.html?width=120&url=";
    write_string += encodeURIComponent(window.location);
    write_string += "&title="; 
    write_string += encodeURIComponent(document.title);
  write_string += "\" height=\"22\" width=\"90\" scrolling='no' frameborder='0'></iframe>";
  document.write(write_string);
})()