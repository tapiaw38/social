$(document).ready(function(){
    $("#text1").hide();
    $("#text2").hide();
});

$(document).ready(function() {
    $('#image1').hover(function(){
        $('#text1').toggle();
    })
    $('#image2').hover(function(){
        $('#text2').toggle();
    })
});