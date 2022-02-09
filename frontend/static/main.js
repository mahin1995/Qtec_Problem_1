function searchItem(){
        let user=$('#id_userName').val()
        let title=$('#id_titles').val()
        let time=$('#id_time').val()
        console.log(user);
        console.log(title);
        console.log(time);

        let text=$('#id_search_text').val()
        let url =`/search_apiView?search=${text}&title=${title}&user=${user}&time=${time}`            

        $.ajax({url: url,beforeSend:function(){
            $(".result-show").html('');
        }, success: function(result){
            console.log(result);
            var div;
            if(result.length >0){
                div=result.map(data=>`<div class="card">
                <div class="card-header">${data.title}</div>
                <div class="card-body">${data.describe}</div>
                <div class="card-footer">create on:${data.app_date_tiem} || create by :${data.user_name}</div>
                </div><br> <br>`)
            }else{
                div='<h1>No result found</h1>'
            }

            $(".result-show").html(div);
          }});
}