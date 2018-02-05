(function() {
  var questions = [{
    question: "피부가 얇고 건조하다",
    choices: ["Yes", "No"],
    correctAnswer: 0
  }, {
    question: "모공이 넓은 편이다",
    choices: ["Yes", "No"],
    correctAnswer: 0
  }, {
    question: "계절이 바뀔 때마다 피부 트러블이 생긴다",
    choices: ["Yes", "No"],
    correctAnswer: 0
  }, {
    question: "겨울에 피부가 잘 트는 편이다",
    choices: ["Yes", "No"],
    correctAnswer: 0
  }, {
    question: "머리가 가렵고 비듬이 생긴다",
    choices: ["Yes", "No"],
    correctAnswer: 0
  }];
  
  var questionCounter = 0; //Tracks question number
  var selections = []; //Array containing user choices
  var quiz = $('#quiz'); //Quiz div object
  
  // Display initial question
  displayNext();
  
  // Click handler for the 'next' button
  $('#next').on('click', function (e) {
    e.preventDefault(); // 기본적인 서브밋 행동을 취소하고 이어서 그 후 실행되어야 할 것을 적는다.
    
    // Suspend click listener during fade animation
    if(quiz.is(':animated')) {        
      return false;
    }
    choose();
    
    // If no user selection, progress is stopped
    if (isNaN(selections[questionCounter])) {
      alert('선택하셔야 합니다!!');
    } else {
      questionCounter++;
      displayNext();
    }
  });
  
  // Click handler for the 'prev' button
  $('#prev').on('click', function (e) {
    e.preventDefault();
    
    if(quiz.is(':animated')) {
      return false;
    }
    choose();
    questionCounter--;
    displayNext();
  });
  
  // Click handler for the 'Start Over' button
  $('#start').on('click', function (e) {
    e.preventDefault();
    
    if(quiz.is(':animated')) {
      return false;
    }
    questionCounter = 0;
    selections = [];
    displayNext();
    $('#start').hide();
  });
  
  // Animates buttons on hover
  $('.button').on('mouseenter', function () {
    $(this).addClass('active');
  });
  $('.button').on('mouseleave', function () {
    $(this).removeClass('active');
  });
  
  // Creates and returns the div that contains the questions and 
  // the answer selections
  function createQuestionElement(index) {
    var qElement = $('<div>', {
      id: 'question'
    });
    
    var header = $('<h2 style="display:inline; background-color:#ffcdd2;">Question ' + (index + 1) + ':</h2>');
    qElement.append(header);
    
    var question = $('<p>').append(questions[index].question);
    qElement.append(question);
    
    var radioButtons = createRadios(index);
    qElement.append(radioButtons);
    
    return qElement;
  }
  
  // Creates a list of the answer choices as radio inputs
  function createRadios(index) {
    var radioList = $('<ul>');
    var item;
    var input = '';
    for (var i = 0; i < questions[index].choices.length; i++) {
      item = $('<li>');
      input = '<input type="radio" name="answer" value=' + i + ' />';
      input += questions[index].choices[i];
      item.append(input);
      radioList.append(item);
    }
    return radioList;
  }
  
  // Reads the user selection and pushes the value to an array
  function choose() {
    selections[questionCounter] = +$('input[name="answer"]:checked').val();
  }
  
  // Displays next requested element
  function displayNext() {
    quiz.fadeOut(function() {
      $('#question').remove();
      
      if(questionCounter < questions.length){
        var nextQuestion = createQuestionElement(questionCounter);
        quiz.append(nextQuestion).fadeIn();
        if (!(isNaN(selections[questionCounter]))) {
          $('input[value='+selections[questionCounter]+']').prop('checked', true);
        }
        
        // Controls display of 'prev' button
        if(questionCounter === 1){
          $('#prev').show();
        } else if(questionCounter === 0){
          
          $('#prev').hide();
          $('#next').show();
        }
      }else {
        var scoreElem = displayScore();
        quiz.append(scoreElem).fadeIn();
        $('#next').hide();
        $('#prev').hide();
        $('#start').hide();
      }
    });
  }
  
  // Computes score and returns a paragraph element to be displayed
  function displayScore() {
    var type_result = $('<p>',{id: 'type'});
    var dryness = 0;
    var type = "";
    for (var i = 0; i < selections.length; i++) {
      if (selections[i] === questions[i].correctAnswer) {
        dryness += 5;
      }
    }
    if (dryness > 19){
      type = "건성피부(민감성피부)";
      type1 = "Dry1"
    }
    else if (dryness == 15){
      type = "중성(약한 민감성 피부)";
      type1 = "Dry2";
    }
    else if (dryness == 10){
      type = "복합성 피부";
      type1 = "Wet1";
    }
    else{
      type = "지성피부";
      type1 = "Oily1";
    }
    type_result.append('당신의 피부타입은 ' + type + ' 입니당 <br>');
    //type_result.append('<form action="'+ window.parent +'" method="GET"><input type="hidden" name="skin_type" value=' + type1 + '>' + '<input type="submit" value="전송"></form>');
    window.parent.document.getElementById('skin_type_result').value = type;
    return type_result;
  }


})();