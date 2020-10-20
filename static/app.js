if (location.pathname === '/show_profile') {
  $(() => {
    $logoutButton = $('button')
    $logoutButton.on('click', () => {
      location = '/'
    });
  });
}