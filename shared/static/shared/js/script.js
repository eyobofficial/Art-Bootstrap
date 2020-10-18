$(function() {
  // Add to cart
  $('.btn-cart').click(function() {
    const slug = $(this).data('slug');
    const cartUrl = `/cart/add/themes/${slug}/`;
    const cartToastUrl = `/cart/themes/${slug}/cart-toast/`;
    const $btn = $(this);

    $.get(cartUrl, function(data) {
      $btn.attr('disabled', true);
      $.get(cartToastUrl, function(data) {
        $('.toast').html(data);
        $('.toast').toast('show');
      });
      $('.cart-count').removeClass('d-none').html(data['cart_count']);
    });
  });

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
