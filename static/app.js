if (location.href === 'http://localhost:5000/show_profile') {
  $(() => {
    $logoutButton = $('button')
    $logoutButton.on('click', () => {
      location = 'http://localhost:5000/'
    });
  });
}