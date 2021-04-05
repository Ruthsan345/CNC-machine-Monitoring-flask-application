//Go Back
function OpenProduct(i){
    var i = $('.product-image[item-data="'+i+'"] img');
    var lbi = $('.lightbox-blanket .product-image img');
    console.log($(i).attr("src"));
    $(lbi).attr("src", $(i).attr("src"));  
    $(".lightbox-blanket").toggle();
      
    $("#product-quantity-input").val("0");
    CalcPrice (0);
    
  }
  function GoBack(){
    $(".lightbox-blanket").toggle();
  }
  
  //Calculate new total when the quantity changes.
  function CalcPrice (qty){
    var price = $(".product-price").attr("price-data");
    var total = parseFloat((price * qty)).toFixed(2);
    $(".product-checkout-total-amount").text(total);
  }
  
  //Reduce quantity by 1 if clicked
  $(document).on("click", ".product-quantity-subtract", function(e){
    var value = $("#product-quantity-input").val();
    //console.log(value);
    var newValue = parseInt(value) - 1;
    if(newValue < 0) newValue=0;
    $("#product-quantity-input").val(newValue);
    CalcPrice(newValue);
  });
  
  //Increase quantity by 1 if clicked
  $(document).on("click", ".product-quantity-add", function(e){
    var value = $("#product-quantity-input").val();
    //console.log(value);
    var newValue = parseInt(value) + 1;
    $("#product-quantity-input").val(newValue);
    CalcPrice(newValue);
  });
  
  $(document).on("blur", "#product-quantity-input", function(e){
    var value = $("#product-quantity-input").val();
    //console.log(value);
    CalcPrice(value);
  });
  
  
