

$(function(){

    // $('#woven').click(function(){
    //     var parameters = $('')
    //     $.ajax({
    //         url : 'type//'
    //     })
    // })
    var arr = ['faltu','woven','all','print'];
    $('.tm-paging-link').click(function(e){
        var element_id = e.target.id;
        if(arr.indexOf(element_id) >  -1){
            e.preventDefault();				
            var page = $(this).text().toLowerCase();
            $('.tm-gallery-page').addClass('hidden');
            $('#tm-gallery-page-' + page).removeClass('hidden');
            $('.tm-paging-link').removeClass('active');
            $(this).addClass("active");
        }        
    });
    $(".appDetails").click(function (event) {
        var element_id = event.target.id;
        var url;var parameters;        
        // console.log(arr.indexOf(element_id), element_id);
        if(arr.indexOf(element_id) >  -1){
            url = 'type/'+ element_id +'/';
            // console.log(url);
            $(".tm-gallery").html('').load(url);
        }
     });

    //  $.ajax({
    //     url : url,
    //     dataType : 'json',
    //     success : function(data){
    //         console.log(data)
    //         $('#tm-gallery-page-pizza').html(data)
    //     },
    //     error : function(e){
    //         console.log('Error', e);
    //     }
    // })
})