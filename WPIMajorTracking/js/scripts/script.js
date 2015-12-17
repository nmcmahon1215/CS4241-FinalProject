  $(document).ready(function () {
    $('#registration-form').validate({ // initialize the plugin
      rules: {
      email: {
        required: true,
        email: true
      },
      password: {
        required: true,
        minlength: 5
      },
      passwordRepeat: {
        required: true,
        minlength: 5,
        equalTo: "#password"
      },
      firstName: {
        required: true
      },
      lastName: {
        required: true
      }
    },
    messages: {
      password: {
        required: "Please provide a password",
        minlength: "Your password must be at least 5 characters long"
      },
      passwordRepeat: {
        required: "Please provide a password",
        minlength: "Your password must be at least 5 characters long",
        equalTo: "Please enter the same password as above"
      }
    },
    submitHandler: function (form) {
      form.submit();
    }
  });
});

/*
 * Submits a form with the given ID after 3 seconds
 *
 * @param {string} id The ID of the form to submit
 */
function delayFormSubmission(id) {
  setTimeout( function() {
    $(id).submit();
  }, 3000);
}

function emailAdvisor() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("POST", "/api/email", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

  xhttp.onload = function () {
    
  }
  var query = "advisor_name=" + $("#advisor_name").val() + 
              "&advisor_email=" + $("#advisor_email").val() +
              "&sheet_id=" + $("#sheet_id").val() +
              "&user_name=" + $("#user_name").val();
  $("#advisor_name").val("");
  $("#advisor_email").val("");
  xhttp.send(query);
}