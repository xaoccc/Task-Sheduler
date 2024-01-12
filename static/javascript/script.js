document.addEventListener('DOMContentLoaded', function() {
    var addNewTask = document.getElementById('new_task');
    var newTaskForm = document.getElementById('new-task-form');

    addNewTask.addEventListener('click', function(event) {
        newTaskForm.style.display = 'block';

    });

    document.addEventListener('click', function(event) {
    if (!newTaskForm.contains(event.target) && event.target !== addNewTask) {
        newTaskForm.style.display = 'none';
        }
    });
});