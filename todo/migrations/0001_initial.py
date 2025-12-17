<div id="todo-list">
    {% for todo in todos %}
    <div class="todo-item">
        <div class="todo-info">
            <h3>{{ todo.subject }}</h3>
            <p style="color: #666; font-size: 0.85rem;">{{ todo.notes|truncatechars:40 }}</p>
        </div>
        
        <div class="actions">
            <a href="{% url 'todo_detail' todo.id %}" class="btn btn-view" style="text-decoration: none;">View</a>
            
            <form action="{% url 'todo_delete' todo.id %}" method="POST" style="display:inline;">
                {% csrf_token %}
                <button type="submit" class="btn btn-delete" onclick="return confirm('Delete this task?')">
                    Delete
                </button>
            </form>
        </div>
    </div>
    {% empty %}
    <p style="text-align:center; color:#999;">No tasks yet. Add one above!</p>
    {% endfor %}
</div>