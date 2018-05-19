//intro animation
$(function(){
    function onScrollInit( items, trigger ) {
        items.each( function() {
        var osElement = $(this),
            osAnimationClass = osElement.attr('data-os-animation'),
            osAnimationDelay = osElement.attr('data-os-animation-delay');
          
            osElement.css({
                '-webkit-animation-delay':  osAnimationDelay,
                '-moz-animation-delay':     osAnimationDelay,
                'animation-delay':          osAnimationDelay
            });

            var osTrigger = ( trigger ) ? trigger : osElement;
            
            osTrigger.waypoint(function() {
                osElement.addClass('animated').addClass(osAnimationClass);
                },{
                    triggerOnce: true,
                    offset: '80%'
            });
        });
    }

    onScrollInit( $('.os-animation') );
    onScrollInit( $('.staggered-animation'), $('.staggered-animation-container') );
});//]]>  


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


