//also use to election
var prev;

//table hovering
$(function () {
    $(".card-body tr").click(function () {
        //change previous selection to original color
        $(prev).css('background-color', '')

        //update new selection
        $(this).css('background-color', 'cyan');
        prev = this;
    });
});


//scroll
$(".intro a").click(function(e){
        //anon ID, adds event listener to a tags inside of .intro
        //when event occurs, scrolls to desired href tag
       var sectionID = e.currentTarget.id + "-Section";
       //alert(sectionID);
       //animate
       $("html, body").animate({
            scrollTop: $("#" + sectionID).offset().top},'slow');
    });
});




$("button").click(function() {
    $('html,body').animate({
        scrollTop: $(".second").offset().top},
        'slow');
});


