// LifeOS Application JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize task checkboxes
    const checkboxes = document.querySelectorAll('.task-checkbox');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const taskId = this.dataset.taskId;
            if (taskId) {
                toggleTask(taskId, this.checked);
            }
        });
    });
});

function toggleTask(taskId, completed) {
    // TODO: Implement API call to update task
    console.log(`Task ${taskId} ${completed ? 'completed' : 'uncompleted'}`);
    // For now, just visual feedback
    const taskItem = document.querySelector(`[data-task-id="${taskId}"]`).closest('.task-item');
    if (completed) {
        taskItem.style.opacity = '0.6';
        taskItem.style.textDecoration = 'line-through';
    } else {
        taskItem.style.opacity = '1';
        taskItem.style.textDecoration = 'none';
    }
}

function saveDailyPlan() {
    // TODO: Implement save functionality via API
    console.log('Saving daily plan...');
}

function addTask(event) {
    event.preventDefault();
    // TODO: Implement add task functionality via API
    console.log('Adding task...');
}

