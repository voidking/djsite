$(function(){
    $('table').on('click','.del',function(){
        $that = $(this);
        layer.confirm('确认删除？', {
            btn: ['确认','取消'] //按钮
        }, function(){
            var $tr = $that.parents('tr');
            var id = $tr.attr('data-id');
            $.ajax({
                url: '/blog/delete',
                type: 'POST',
                dataType: 'json',
                data: {id: id},
                success: function(data){
                    console.log(data);
                    if(data.code == '0'){
                        $tr.remove();
                        layer.msg('删除成功');
                    }
                },
                error: function(xhr){
                    console.log(xhr);
                }
            });
        }, function(){
            // nothing
        });
        
    });

    $('.search').on('click',function(){
        var key = $('.search-input').val();
        $.ajax({
            url: '/blog/search',
            type: 'POST',
            dataType: 'json',
            data: {key: key},
            success: function(data){
                console.log(data);
                if(data.code == '0'){
                    var html = template('tr_template',{articles: data.articles});
                    $('tbody').html(html);
                }
            },
            error: function(xhr){
                console.log(xhr);
            }
        });
    });

    $('.search-input').keypress(function(event) {
        var key = event.which;
        // console.log(key);
        if(key == 13){
            //do something
            $('.search').trigger('click');
        }
    });
});