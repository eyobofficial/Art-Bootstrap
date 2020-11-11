$(function() {
  // Add to wishlisht
  $('.btn-favorite').click(function() {
    const slug = $(this).data('slug');
    const wishlistUrl = `/wishlist/add/themes/${slug}/`;
    const wishlistToastUrl = `/wishlist/themes/${slug}/wishlist-toast/`;
    const $btn = $(this);

    $.get(wishlistUrl, function(data) {
      $btn.attr('disabled', true);
      $.get(wishlistToastUrl, function(data) {
        $('.toast').html(data);
        $('.toast').toast('show');
      });
    });
  });

  // Global Search query
  $('.global-search-input').on('keypress', function(event) {
    if (event.which == 13) {
      const searchTerm = $(this).val();
      const url = `/themes/?search=${searchTerm}`;

      window.location.href = url;
    }
  });
});
