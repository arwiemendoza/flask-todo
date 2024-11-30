
document.addEventListener("DOMContentLoaded", function() {
  const deleteButtons = document.querySelectorAll(".todo-delete");

  deleteButtons.forEach(button => {
    button.addEventListener("click", function() {
      const todoId = this.getAttribute("data-id");
      const todoItem = document.getElementById(`todo-${todoId}`);
      
      if (todoItem) todoItem.remove();
    });
  });

  const checkBoxes = document.querySelectorAll(".checkbox")

  checkBoxes.forEach(checkbox => {
    checkbox.addEventListener("click", function() {
      todoName = this.closest("div").querySelector("span.todo-name")

      if (checkbox.checked) {
        todoName.classList.add("underlined")
      } else {
        todoName.classList.remove("underlined")
      }
    })
  })
});
