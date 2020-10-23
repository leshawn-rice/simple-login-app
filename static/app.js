if (location.pathname === '/show-profile') {
  $(() => {
    $logoutButton = $('button')
    $logoutButton.on('click', () => {
      location = '/?logged_out=True'
    });
  });
}
else if (location.pathname === '/') {
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