function generateString() {
  const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  let result = "";
  const stringLength = 20; // Adjust the length as desired

  for (let i = 0; i < stringLength; i++) {
    result += characters.charAt(Math.floor(Math.random() * characters.length));
  }

  document.getElementById("output").textContent = result;
}
