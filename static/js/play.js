      var NOTE_FREQS;
      var FIBONACCI;
      var CANVAS_WIDTH;
      var CANVAS_HEIGHT;
      var RADIUS;
      var playing;
      var circleColor;
      var BGCOLOR;
      var transitionColor;
      var textColor;
      var d;
      var isOverCircle;
      var previous;
      var current;
      var PAUSE;
      var errorMessage;
      var errorText;
      var canvas;
      var level;
      var notesSample;
      var points;
      var font; 
      var tries;
      var notes;
      var immunity;  // 

      function setup() {
	FIBONACCI = [8, 13, 21, 34, 55, 89];
        ERROR_WORDS = ["BAD!", "NOPE!", "OOF!", "NEIN!", "YIKES!", "DOH!", "WHOOPS!"];
	NOTE_FREQS = [16.35, 17.32, 18.35, 19.45, 20.60, 21.83, 23.12, 24.50, 25.96, 27.50, 29.14, 30.87];
	CANVAS_WIDTH = 1024;
        CANVAS_HEIGHT = 768;
        RADIUS = 150;
        notes = [];	  
        playing = false;
	immunity = false;  
        circleColor = 200;
	transitionColor = 0;  
	textColor = 0;  
        BGCOLOR = 77;
        PAUSE = 300;
	points = 0;
	level = 1;
        notesSample = getRandomSubarray(NOTE_FREQS, level+4);	  	  
	tries = 3;
        canvas = createCanvas(CANVAS_WIDTH, CANVAS_HEIGHT);
	canvas.parent('play-content'); 
        background(BGCOLOR);
        osc = new p5.Oscillator();
        osc.setType('sine');
        
      }


      function draw() {
        d = dist(mouseX, mouseY, CANVAS_WIDTH/2, CANVAS_HEIGHT/2);
	  
        if (d < RADIUS) {
          isOverCircle = true;
	  cursor(HAND);	
        } else {
          isOverCircle = false;
          cursor(ARROW);		
        }


	background(BGCOLOR);  
	stroke('#660066');
	strokeWeight(1);  
	fill(235);
	textFont("Delius Swash Caps");
	textSize(32);
	text("level: " + level, 120, 100);
        text("points: " + points, 120, 150);
	text("tries: ", 120, 200);  
	if (tries==2){
	    fill("#99ff66");    
	} else if (tries == 1) {
	    fill("#ff0000");
	}
	  else if (tries == 0) {
	    stroke("#ffffff");
	    fill("#000000");
	}
	if (tries>=0){
          text(tries, 200, 200);  
	}  	
	stroke("#ff99ff");
	strokeWeight(4);  
        fill(circleColor);
        ellipse(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, RADIUS*2, RADIUS*2);
	fill("#000000");
	if (errorMessage == true){
	      
	  noStroke;    
	  fill(textColor);
	  background(transitionColor);  
	  text(errorText, CANVAS_WIDTH/2 - 45, CANVAS_HEIGHT/2);
	    if (textColor < circleColor){
		textColor++;
	    }
	    if (transitionColor < BGCOLOR){
		transitionColor += 2;
	    }
	}
	  
      }
      
      function mouseClicked() {

        if (isOverCircle) {    
	  if (!playing){
	    playTune();
	  } 
          else {
            if ((notes.length-1) > 2){
              check();
            }
          }
        } 

      }


      function getRandomSubarray(arr, size) {
        var shuffled = arr.slice(0), i = arr.length, temp, index;
        while (i--) {
          index = Math.floor((i + 1) * Math.random());
          temp = shuffled[index];
          shuffled[index] = shuffled[i];
          shuffled[i] = temp;
        }
        return shuffled.slice(0, size);
      }

      function playTune() {
	 (function next() {
            if (tries < 1) return;	  
             setTimeout(function() {
	       // weight likelihood of same note to > 33%
	       if (Math.random() > 0.66 && notes.length>2){
		   console.log("weighted note added.");
		   freq = notes[notes.length-2];		   
		 }
	       else {

		   console.log("note sample is " + notesSample);
		   freq = notesSample[Math.floor(Math.random()*notesSample.length)] * 10;
		 }
	      notes.push(freq);
              playing = true;
	      osc.freq(freq);	 
	      osc.amp(0.5, 0.05);
       	      osc.start();
	      osc.stop(1);
	      console.log(str(notes));	 
	      // does user fail to click when notes are same?
	      setTimeout(function(){
      	          if (notes[notes.length-1] == notes[notes.length-3] && notes.length > 2 && !immunity) {
		        tries -= 1;
			errorText = str(ERROR_WORDS[Math.floor(Math.random()*(ERROR_WORDS.length-1))])
			errorMessage = true;
			console.log(notes[notes.length-1] + " is equal to " + notes[notes.length-3] + " but there was no click.");
	          }
	      }, 1500);
              immunity = false;
              errorMessage = false;	 
              next();
              }, 1500);
           })();
          }
	  
      function check() {
	if (notes[notes.length-1] == notes[notes.length-3]) {
	  console.log(str(notes));
	  console.log(notes[notes.length-1] + " is equal to " + notes[notes.length-3]);
	  if (points > FIBONACCI[level]){	
            level += 1;
            notesSample = getRandomSubarray(NOTE_FREQS, level+4);	  	      
	  }   
	  points += level;
	  immunity = true;  
	}
        else {
          tries -= 1;
	  console.log("tries equal to " + tries);  
	    console.log(notes[notes.length-1] + " isn't equal to " + notes[notes.length-3]);
	    errorText = str(ERROR_WORDS[Math.floor(Math.random()*(ERROR_WORDS.length-1))]);
	    errorMessage = true;  
	}
      }


