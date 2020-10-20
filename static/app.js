if (location.pathname === '/show_profile') {
  $(() => {
    $logoutButton = $('button')
    $logoutButton.on('click', () => {
      location = '/'
    });
  });
}
else {
  $form = $('form')
  $(() => {
    $form.on('submit', (event) => {
      $username = $('#username').val()
      $password = $('#password').val()
      if ($username.includes(':') || $password.includes(':')) {
        event.preventDefault()
        $form.trigger('reset')
        alert('Username and password cannot contain ":"!')
      }
    });
  });
}