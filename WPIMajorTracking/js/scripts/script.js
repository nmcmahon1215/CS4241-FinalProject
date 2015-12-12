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
    submitHandler: function (form) { // for demo
       //need to use a post request to handle this
       alert("Registration form submitted!");
       form.submit();
     }
   });
});