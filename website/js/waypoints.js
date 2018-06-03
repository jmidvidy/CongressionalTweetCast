
//also use to election
var prev;
var selected;
var doneLoading = "False";

//smooth scroll implementation
$(document).ready(function(){

    //change back
    $("#Predict-Block").hide();
    $("#Load-Block").hide();
    $("#invalid-feedback").hide();
    $("#load-text").hide();

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

    $("#predict-again").click(function(e){

        //don't jump
        e.preventDefault();

        //enter button is this
        var scrollTo = $(this).attr('href');
      //  console.log($(scrollTo).offset().top);




       $("html, body").animate({
            scrollTop: $(scrollTo).offset().top - 30
        },500);

        setTimeout(function () {
            hideCaller();
        }, 500);
    });
});

function hideCaller(){
    hidePredictBlocks();
}

//delay compiler
function hidePredictBlocks(){
        $("#Predict-Block").hide();
        $("#Load-Block").hide(); 
        $("#load-text").hide(); 
};

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
        $("#load-text").hide();


        //use global selected
        election = selected;
        //alert("twitter_handle: " + twitter_handle + " | Election: " + election);

        //DO SOME TWITTER HANDLE CHECKING HERE
        var v_th = validTwitterHandle(twitter_handle);
        if (v_th == 0){
            invalid(1);
            return;
        }

        $("#invalid-feedback").hide();
        
        beforeAjax();

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
                console.log(data.invalid);
                if (data.invalid == "invalid_handle") {
                    //alert("twitter user is protected or invalid.")
                    invalid(2);
                }
                else if (data.invalid == "protected"){
                    invalid(3);
                }
                else {
                afterResult(election, twitter_handle, data.result, data.hotwords);
                }
              },
            error: function(){ alert("FAILURE"); },
            url: "http://localhost:8000/ajax_caller"
        });
    });
});

//do basic checking on inputted twitter handle
function validTwitterHandle(t_h){
    if (t_h == "") {
        return 0;
    }
    else if (t_h.substring(0, 1) != '@'){
        return 0;
    }
    else if (t_h.indexOf(' ') > -1){ //contains a space
        return 0
    }
    var charset = ",./-;'[]\"`~!#$%^&*()+{}:<>?";
    var i;
    for (i=0; i < charset.length; i++) {
        var curr_char = charset.charAt(i);
        if (t_h.indexOf(curr_char) > -1) { //contains any of these chars
            return 0;
        }

    }
    return 1;
};



//before ajax call is made (loading)
function beforeAjax(){
        $("#load-text h1").css('color', '#1a1a1a');
        $("#Load-Block").show();
        $("#loading").show();
        $("html, body").animate({
            scrollTop: $("#Load-Block").offset().top
        },1000);         
};

//what to do with invalid input
function invalid(c){

    if (c != 1) { //if error comes from backend do "Oops!" instead of of "Done!"
        $("#loading").hide();
        $("#load-text h1").html("Oops!");
        $("#load-text h1").css('color', '#d9534f');
        $("#load-text").show();
    }
    if (c == 1) { //poorly formatted input
        $("#invalid-feedback").html("Invalid input.  Please enter a valid, public, twitter-handle of the form \"@handle\"");
    }
    else if (c == 2) { //invalid handle
        $("#invalid-feedback").html("Inputted twitter handle did not exist.");
    }
    else { //protected user
        $("#invalid-feedback").html("Inputted twitter handle is protected.  Please enter a public user.");
    }

    $("#invalid-feedback").show();
    $("#invalid-feedback").css('color', '#d9534f');
    //try and change outline

    setTimeout(function () {
        $("html, body").animate({
            scrollTop: $("#Second-Block").offset().top - 30
        },500);
    }, 1000);

}

//after ajax call is made and is successful
function afterResult(sel, t_h, res, h_w){

        //loading animations when done
        $("#load-text h1").html("Done!");
        $("#load-text h1").css('color', '#4BBF73');
        $("#loading").hide();
        $("#load-text").show();

        //scrape name of Democrat and Republican in selected election
        var toget = "#" + sel;
        var toget_state = toget + " .state";
        var state = $(toget_state).html();
        var rep_name = $(toget + " .rc").html();
        var dem_name = $(toget + " .dc").html();

        //fill in predict block title
        var p = "In the " + state + " election, " + t_h + " will vote for:";
        $("#predict-title").html(p);

        //if election contains a none, isolate candidate
        var cand;
        var none_cand;
        if (res == "cand" || res == "not-cand") { //if res of either of these vaues we know election contained a none
            var c = sel.split("-");
            if (c[0] == "none") { // "none-SenBurr" none candidate is democrat
                cand = rep_name;
                none_cand = dem_name;
            }
            else { // "KamalaHarris-none" none candidate is republican
                cand = dem_name;
                none_cand = rep_name;
            }
        }

       if (res == "rep") {
         $("#predict-result").html("republican, " + rep_name);
       }
       else if (res == "dem") {
         $("#predict-result").html("democrat, " + dem_name);
       }
       else if (res == "cand") {
         $("#predict-result").html("democrat, " + cand);
       }
       else {
         $("#predict-result").html("not, " + cand);
         
       }

      //update hotwords
      var i;
      for (i = 1; i < 11; i++) { 
        var loc = "#hw" + i + " .val";
        var word = h_w[i-1];
        $(loc).html(word);
        };

       $("#Predict-Block").show();
        $("#predict-again").hide();  

        setTimeout(function () {
            $("html, body").animate({
            scrollTop: $("#predict-title").offset().top
                },1000);
        }, 500);
   

        setTimeout(function () {
            $("#predict-again").fadeIn("slow");
            $("html, body").animate({
            scrollTop: $("#predict-title").offset().top + 100
            },1000);
        }, 5000);
         

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





