(function() {
  var questions = [{
    question: "겨울엔 피부가 잘 트는 편이다.",
    choices: ["Yes", "No"],
    correctAnswer: 0 //0
  }
  , {
    question: "각질 때문에 항상 얼굴에 크림이나 보습제를 챙겨 바른다.",
    choices: ["Yes", "No"],
    correctAnswer: 0 //1
  }, {
    question: "피부가 얇고 건조하다",
    choices: ["Yes", "No"],
    correctAnswer: 0 //2
  }, {
    question: "세안 후 땅기고 각질이 일어난다.",
    choices: ["Yes", "No"],
    correctAnswer: 0 //3
  }, {
    question: "건조한 느낌이 들면 얼굴이 빨개진다.",
    choices: ["Yes", "No"],
    correctAnswer: 0 //4
  }, {
    question: "화장품 트러블이 잘 생긴다.",
    choices: ["Yes", "No"],
    correctAnswer: 0 //5
  }, {
    question: "얼굴과 몸에 뾰루지가 잘 생긴다.",
    choices: ["Yes", "No"],
    correctAnswer: 0 //6
  }, {
    question: "T존 부위가 항상 번들거린다.",
    choices: ["Yes", "No"],
    correctAnswer: 0 //7
  }, {
    question: "끈적임이 싫어 가능하면 화장품을 많이 바르지 않는다.",
    choices: ["Yes", "No"],
    correctAnswer: 0 //8
  }, {
    question: "얼굴과 몸에 털이 많은 편이다.",
    choices: ["Yes", "No"],
    correctAnswer: 0 //9
  }, {
    question: "코에 검은 피지가 많이 있다.",
    choices: ["Yes", "No"],
    correctAnswer: 0 //10
  }, {
    question: "모공이 넓은 편이다.",
    choices: ["Yes", "No"],
    correctAnswer: 0 //11
  }
  ];

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

    var question = $('<p style="font-size:0.9rem;">').append(questions[index].question);
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
    var type_result = $('<p style="text-align: center;">',{id: 'type'});
    var type = "앙기모띠당"
    var dryness = 0;
    var type = "";
    // for (var i = 0; i < selections.length; i++) {
    //   if (selections[i] === questions[i].correctAnswer) {
    //     dryness += 5;
    //   }
    // }
    // 점수 계산 영역

    if (selections[0] === questions[0].correctAnswer) {
      dryness += 5;
    }
    else {
      dryness += 1;
    }
    if (selections[1] === questions[1].correctAnswer) {
      dryness += 4;
    }
    else {
      dryness += 1;
    }if (selections[2] === questions[2].correctAnswer) {
      dryness += 4;
    }
    else {
      dryness += 2;
    }if (selections[3] === questions[3].correctAnswer) {
      dryness += 4;
    }
    else {
      dryness += 2;
    }if (selections[4] === questions[4].correctAnswer) {
      dryness += 3;
    }
    else {
      dryness += 0;
    }if (selections[5] === questions[5].correctAnswer) {
      dryness += 0;
    }
    else {
      dryness += 3;
    }if (selections[6] === questions[6].correctAnswer) {
      dryness += 0;
    }
    else {
      dryness += 3;
    }if (selections[7] === questions[7].correctAnswer) {
      dryness += 0;
    }
    else {
      dryness += 3;
    }if (selections[8] === questions[8].correctAnswer) {
      dryness += 0;
    }
    else {
      dryness += 2;
    }if (selections[9] === questions[9].correctAnswer) {
      dryness += 0;
    }
    else {
      dryness += 2;
    }if (selections[10] === questions[10].correctAnswer) {
      dryness -= 1;
    }
    else {
      dryness += 3;
    }if (selections[11] === questions[11].correctAnswer) {
      dryness -= 5;
    }
    else {
      dryness += 4;
    }

    if (dryness >= 37){
      type = "건성피부(민감성피부)"
      send_type = "Dry"
    }
    else if (dryness >= 28 && dryness < 37){
      type = "중성(약한 민감성 피부)"
      send_type = "Dry1"
    }
    else if (dryness >= 7 && dryness < 28){
      type = "복합성 피부"
      send_type = "Wet"
    }
    else{
      type = "지성피부"
      send_type = "Oily"
    }
    // type_result.append('당신의 피부타입은 ' + type + ' 입니당 <br>');
    // $('<a class="btn" style="text-align:center; cursor:pointer;"><h1>결과보기</h1></a>')
    //     .appendTo(type_result)
    //     .click(function (e) {
    //       window.open("08_2_popup.html", "a", "width=400, height=300, left=100, top=50");
    //     });
    type_result.append('<i class="large material-icons" style="font-size:3rem;">face</i>');
    type_result.append('<br><h4>아래 버튼을 눌러 결과를 확인하세요!</h4>');
    window.parent.document.getElementById('skin_type_result').value = type;
    window.parent.document.getElementById('skin_type_result_mobile').value = type;
    window.parent.document.getElementById('web_modal').innerHTML =
        '<div class="skin_type_test_box hide-on-med-and-down">\n' +
        '<a class="waves-effect waves-light btn modal-trigger" href="#modal1">결과 확인</a>\n' +
        '</div>';
    window.parent.document.getElementById('mobile_modal').innerHTML =
        '<div class="skin_type_test_result_box_mobile hide-on-large-only" style="margin-left:7px; margin-top:5px;">\n' +
        '<a class="waves-effect waves-light btn modal-trigger" href="#modal1">결과 확인</a>\n' +
        '</div>';
    return type_result;
  }



})();