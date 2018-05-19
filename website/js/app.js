$(document).ready(function(){

    //add click listener
    setBindings();

});

function setBindings(){
    $(".intro a").click(function(e){
        //anon ID, adds event listener to a tags inside of .intro
        //when event occurs, scrolls to desired href tag
       var sectionID = e.currentTarget.id + "-Section";
       alert(sectionID);
       //animate
       $("html body").animate({
            scrollTop: $("#" + sectionID).offset().top 
       },1000)
    });
