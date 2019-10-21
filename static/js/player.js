audioPlayer()
    function audioPlayer(){
        $(window).load(function() {
            var currentSong = 0;
            $("#audioPlayer")[0].src = $("#playlist li a")[0];
            $("#audioPlayer")[0].play();
            $("#playlist li a").click(function(e){
                e.preventDefault();
                $("#audioPlayer")[0].src = this;
                $("#playlist li a").removeClass("current-song");
                currentSong = $(this).parent().index();
                $(this).parent().addClass("current-song");
                $("#audioPlayer")[0].play();
            });

            $("#audioPlayer")[0].addEventListener("ended", function(){
                currentSong++;
                if(currentSong == $("#playlist li a").length)
                    currentSong = 0;
                $("#playlist li").removeClass("current-song");
                $("#playlist li:eq("+currentSong+")").addClass("current-song")
                $("#audioPlayer")[0].src = $("#playlist li a")[currentSong].href;
                $("#audioPlayer")[0].play();
            });
            var audio = new Audio('static/files/Rafo-Cricket(OriginMix).mp3');
            audio.type = 'audio/.mp3'
            var playPromise = audio.play();

            if (playPromise !== undefined) {
                playPromise.then(function () {
                console.log('Playing....');
            }).catch(function (error) {
                console.log('Failed to play....' + error);
            });
        }
    });
};