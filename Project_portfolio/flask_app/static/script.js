var img = document.getElementById('crop');

img.setAttribute('data-image', img.src);
img.onmouseover = function () {
    this.src = this.getAttribute('data-hover');
};
img.onmouseout = function () {
    this.src = this.getAttribute('data-image');
}

var img = document.getElementById('cropped-2');

img.setAttribute('data-image', img.src);
img.onmouseover = function () {
    this.src = this.getAttribute('data-hover');
};
img.onmouseout = function () {
    this.src = this.getAttribute('data-image');
}

var img = document.getElementById('cropped-3');

img.setAttribute('data-image', img.src);
img.onmouseover = function () {
    this.src = this.getAttribute('data-hover');
};
img.onmouseout = function () {
    this.src = this.getAttribute('data-image');
}
$(document).ready(function(){
    $(".like, .unlike").click(function(){
        var id = this.id;   
        var split_id = id.split("_");
        var text = split_id[0];
        var post_id = split_id[1]; 
        var type = 0;
        if(text == "like"){
            type = 1;
        }else{
            type = 0;
        }
        $.ajax({
            url: '/likeunlike',
            type: 'post',
            data: {post_id:post_id,type:type},
            dataType: 'json',
            success: function(data){
                var likes = data['likes'];
                var unlikes = data['unlikes'];
                $("#likes_"+post_id).text(likes);       
                $("#unlikes_"+post_id).text(unlikes);   
                if(type == 1){
                    $("#like_"+post_id).css("color","#ffa449");
                    $("#unlike_"+post_id).css("color","lightseagreen");
                }
                if(type == 0){
                    $("#unlike_"+post_id).css("color","#ffa449");
                    $("#like_"+post_id).css("color","lightseagreen");
                }
            }
        });
    });
});