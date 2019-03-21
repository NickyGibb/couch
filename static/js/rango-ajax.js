$('#likes').click(function() {
  var gameid;
  gameid = $(this).attr("data-gameid");
  $.get('/dice/like/', {
    category_id: gameid
  }, function(data) {
    $('#like_count').html(data);
    $('#likes').hide();
  });
});
$('#dislikes').click(function() {
  var gameid;
  gameid = $(this).attr("data-gameid");
  $.get('/dice/dislike/', {
    category_id: gameid
  }, function(data) {
    $('#dislike_count').html(data);
    $('#dislike').hide();
  });
});
