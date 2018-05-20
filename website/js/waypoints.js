//also use to election
var prev;
var selected;

//table hovering
$(function () {
    $(".card-body tr").click(function () {
        //change previous selection to original color
        $(prev).css('background-color', '')
        //add deselector later

        //update new selection
        $(this).css('background-color', '#f0ad4e');
        prev = this;
        selected = prev.id;
    });
});

//run button submission
$(function () {
    $("#go-button").click(function () {
        
        //gets the value of the twitter-handle
        var twitter_handle = $('#inputDefault').val();

        //use global selected
        election = selected;
        //alert("twitter_handle: " + twitter_handle + " | Election: " + election);

        //external call to python
        $.ajax({
              data: {
                'twitter_handle' : twitter_handle,
                'election'  : election
              },
              type: 'POST',
              success: function(da){
                alert(da);
              },
              url: "/C:/Users/jmidv/Documents/Spring 2018/EECS 338/backend/ajax_caller.py",

            }).done(function(data) {
              // alert( data   );
            });


    });
});


//scroll
$(function (){
    $(".intro a").click(function(e){
        //anon ID, adds event listener to a tags inside of .intro
        //when event occurs, scrolls to desired href tag
       var sectionID = e.currentTarget.id + "-Section";
       //alert(sectionID);
       //animate
       $("html #First_Block").animate({
            scrollTop: $("#" + sectionID).offset().top 
       },1000);
    });
});





