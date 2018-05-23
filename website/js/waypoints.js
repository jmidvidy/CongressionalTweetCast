
//also use to election
var prev;
var selected;

//smooth scroll implementation
$(document).ready(function(){

    $("#Third-Block").hide();

    $("#enter-button").click(function(e){

        //don't jump
        e.preventDefault();

        //enter button is this
        var scrollTo = $(this).attr('href');
      //  console.log($(scrollTo).offset().top);

       $("html, body").animate({
            scrollTop: $(scrollTo).offset().top
        },1000);
    });
});

//table hovering
$(function () {
    $("#Second-Block .card-body tr").click(function () {
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
    $("#go-button").click(function (e) {
        
        //gets the value of the twitter-handle
        var twitter_handle = $('#inputDefault').val();

        //use global selected
        election = selected;
        //alert("twitter_handle: " + twitter_handle + " | Election: " + election);

        //external call to python
        var result;

       $.ajax({
            crossDomain: true,
            data: {'twitter_handle': twitter_handle,
                    'election': election
            },  
            type: "POST",
            dataType : "json",
            jsonp: "false",
            withCredentials: "true",
            jsonpCallback: 'callback',
            success: function(data){
                console.log(data.result);
                console.log(data.hotwords);
                console.log(data.invalid);
                if (data.invalid == "True") {
                    alert("twitter user is protected or invalid.")
                }
                else {
                afterResult(selected, twitter_handle,data.result, data.hotwords);
                }
              },
            error: function(){ alert("FAILURE"); },
            url: "http://localhost:8000/ajax_caller"
        });

  
    });
});


function afterResult(sel, t_h, res, h_w){


        var toget = "#" + sel;
        var toget_state = toget + " .state";
        var state = $(toget_state).html();
        var rep_name = $(toget + " .rc").html();
        var dem_name = $(toget + " .dc").html();

       var p = "In the " + state + " election, " + t_h + " will vote for:";
       $("#predict-title").html(p);


       if (res == "rep") {
         $("#predict-result").html("republican, " + rep_name);
       }
       else if (res == "dem") {
         $("#predict-result").html("democrat, " + dem_name);
       }
       else {
         $("#predict-result").html("a candidate in this race had no twitter :(");
       }

      //update hotwords
      var i;
      for (i = 1; i < 11; i++) { 
        var loc = "#hw" + i + " .val";
        var word = h_w[i-1];
        $(loc).html(word);
        };

        $("#Third-Block").show();

       $("html, body").animate({
            scrollTop: $("#Third-Block").offset().top
        },1000);





};


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





