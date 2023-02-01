function validateForm(form)
{
  if(checkConfirmPassword(form) && checkRestaurantId(form))
      return true;
  else
    return false
}

function checkConfirmPassword(form)
{
  const password = form.password.value;
  const confirmPassword = form.confirmPassword.value;

  if (password != confirmPassword) 
  {
    alert("Erro! A senha não correspondeu.");
    return false;
  } else {
    return true;
  }
}

function checkRestaurantId(form)
{
  const restaurantId = parseInt(form.fieldRestaurant.value)

  if (restaurantId == 0) 
  {
    alert("Por favor, selecione um restaurante.");
    return false;
  } else {
    return true;
  }
}