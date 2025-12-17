<div id="todo-list">
    {% for todo in todos %}
    <div class="todo-item">
        <div class="todo-info">
            <h3>{{ todo.subject }}</h3>
        </div>
        <div class="actions">
            <button class="btn btn-view">View</button>
            <button class="btn btn-delete">Delete</button>
        </div>
    </div>
    {% empty %}
    <p style="text-align:center; color:#999;">No tasks yet. Add one above!</p>
    {% endfor %}
</div>