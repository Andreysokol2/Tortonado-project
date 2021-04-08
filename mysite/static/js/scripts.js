$(function(){
  $('.attrib .option').click(function(){
    $(this).siblings().removeClass('activ');
    $(this).addClass('activ');
  })
  $('.zoomControl').click(function(){
    $(this).parents('.productCard').addClass('morph');
    $('body').addClass('noScroll');
  })
  $('.closePreview').click(function(){
    $(this).parents('.productCard').removeClass('morph');
    $('body').removeClass('noScroll');
  })
  $('.movControl').click(function(){
    let imgActiv = $(this).parents('.preview').find('.imgs img.activ');
    if ($(this).hasClass('left')) {
      imgActiv.index() == 0 ? $('.imgs img').last().addClass('activ') : $('.imgs img.activ').prev().addClass('activ');
    } else {
      imgActiv.index() == ($('.imgs img').length - 1) ? $('.imgs img').first().addClass('activ') : $('.imgs img.activ').next().addClass('activ');
    }
    imgActiv.removeClass('activ');
  })
})
$(document).ready(function(){
        var form = $('#form_buying_product');
        var submit_btn = $('#submit_btn');
        var dop1 = '';
        var dop2 = '';
        var dop3 = '';
        form.on('submit', function(e){
            e.preventDefault()
            if ($('#dop1').is(':checked')){
	            dop1 = 'Дополнение1';
//	            window.alert('Дайте свое согласие на обработку данных!');
	           };
	           if ($('#dop2').is(':checked')){
	            dop2 = 'Дополнение2';
	           };
	           if ($('#dop3').is(':checked')){
	            dop3 = 'Дополнение3';
	           };
	        var weight = $('.form-select').val();
	        console.log(weight)
            var submit_btn = $('#submit_btn');
            var product_id = submit_btn.data('product_id');
            var apps = dop1 +'\n'+  dop2 +'\n' + dop3
            console.log(apps)
            var product_name = submit_btn.data('product_name');
            var product_price = submit_btn.data('price');
            var curret_weight = parseFloat($('.form-select').val());
            var price_per_kilogram = parseFloat(submit_btn.data('price_per_kilogram'));
            var total_price1 = curret_weight * price_per_kilogram;
            var decorations = ' '
            if ($('#dop1').is(':checked')){
                        total_price1 += 300;
            };
            if ($('#dop2').is(':checked')){
                        total_price1 += 100;
            };
            if ($('#dop3').is(':checked')){
                        total_price1 += 350;
            };
            if ($('.dop1').is(':checked')){
                decorations = 'Без оформления'
            };
            if ($('.dop2').is(':checked')){
                        total_price1 += 350;
                        decorations = 'Оформление 1'
            };
            if($('.dop3').is(':checked')){
	            total_price1 += 450;
	            decorations = 'Оформление 2'
	        };
            basketUpdating(product_id, apps, is_delete=false, total_price1, decorations, weight)
            dop1 = '';
            dop2 = '';
            dop3 = '';
            kilograms = 0;
            total_price1 = 0;
            decorations = ''

    });
        function basketUpdating(product_id, apps,is_delete, total_price, decorations,  weight ){
            var form = $('#form_buying_product');
            var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
            if (!csrf_token){
                var csrf_token = $('#basket_total_nub [name="csrfmiddlewaretoken"]').val();
                console.log('меняем токен')
            }
            var nub = $('#number').val();
            console.log(nub);
            var submit_btn = $('#submit_btn');
            var data ={};
            if (is_delete){
                 var csrf_token = $('.delete_item [name="csrfmiddlewaretoken"]').val();
                    if (!csrf_token){
                        var csrf_token = $('.delete_item [name="csrfmiddlewaretoken"]').val();
                    }
                var form = $('.delete_item');
                data["is_delete"] = true;
            }
            else{
                var product_id = submit_btn.data('product_id');
                data.apps = apps
                data.weight = weight
                data.total_price = total_price
                data.decorations = decorations
            }
            data.product_id = product_id;
            data["csrfmiddlewaretoken"] = csrf_token;
            var url = form.attr("action");
            console.log(data)
            $.ajax({
                  url: url,
                  type: 'POST',
                  data: data,
                  cache: true,
                  success: function (data) {
                     dops = ''
                     $('#basket_total_nub').text(data.products_total_nub);
                     console.log("OK");
                     if (is_delete){
                        $('[data-product_id='+product_id+']').remove();
                        if (data.products_total_nub = '0'){
                            $('.not-products-in-basket').text('У вас пока нет тортов в корзине');
                        }
                        swal("Готово!", "Торт удалён из корзины", "error");
                     }
                     else{
                        swal("Отлично!", "Торт добавлен в корзину", "success");
                     }


                 },
                 error:function(){
                    console.log('error');
                 }
            });
    }
        function shovingCarrousel(){
        $("#product-image").addClass("active");
    };
    shovingCarrousel();
    $(document).on('change', ".form-select" , function(){
    var curret_weight = parseFloat($('.form-select').val());
    console.log(curret_weight)
    var price_per_kilogram = parseFloat(submit_btn.data('price_per_kilogram'));
    console.log(price_per_kilogram)
    var new_price = curret_weight * price_per_kilogram;
    if ($('#dop1').is(':checked')){
	            new_price += 300;
	};
	if ($('#dop2').is(':checked')){
	            new_price += 100;
	};
	if ($('#dop3').is(':checked')){
	            new_price += 350;
	};
	if ($('.dop1').is(':checked')){
	            console.log(123);
	};
	if ($('.dop2').is(':checked')){
	            new_price += 350;
	            console.log(456);
	};
	if ($('.dop3').is(':checked')){
	            new_price += 450;
	            console.log(456);
	};
    $('.product_price').text(new_price+ '.руб')
    new_price = 0;
    });
    $(document).on('change', ".form-check" , function(){
    var curret_weight = parseFloat($('.form-select').val());
    console.log(curret_weight)
    var price_per_kilogram = parseFloat(submit_btn.data('price_per_kilogram'));
    console.log(price_per_kilogram)
    var new_price = curret_weight * price_per_kilogram;
    if ($('#dop1').is(':checked')){
	            new_price += 300;
	};
	if ($('#dop2').is(':checked')){
	            new_price += 100;
	};
	if ($('#dop3').is(':checked')){
	            new_price += 350;
	};
	if ($('.dop1').is(':checked')){
	            console.log(123);
	};
	if ($('.dop2').is(':checked')){
	            new_price += 350;
	            console.log(456);
	};
	if ($('.dop3').is(':checked')){
	            new_price += 450;
	            console.log(456);
	};
    $('.product_price').text(new_price+ '.руб')
    new_price = 0;
    });
    $(document).on('click', '.delete_item', function(e){
            e.preventDefault();
            product_id = $(this).data("product_id")
            nub = 0;
            basketUpdating(product_id = product_id, nub = nub, is_delete=true)
    })
})
window.onload = function () {
    document.body.classList.add('loaded_hiding');
    window.setTimeout(function () {
      document.body.classList.add('loaded');
      document.body.classList.remove('loaded_hiding');
    }, 500);
  }


