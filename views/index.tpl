<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Список задач</title>
	<link rel="stylesheet" href="static/style.css">
	<script src="http://code.jquery.com/jquery-3.5.1.js"></script>
	<script src="static/script.js"></script>
</head>
<body>
<div class="container">
	<div class="row">
		<h1>Список задач</h1>
		<ul class="todo-list">
		% for task in tasks:
		%if task.in_active:
			<li class="completed">
			<input class="checkbox" type="checkbox" data-uid="{{ task.uid }}" disabled='disabled' cheked='cheked'/>
		%else:
			<li>
			<input class="checkbox" data-uid="{{ task.uid }}" type="checkbox">
		% end
		{{ task }}
		<a class="remove" href="api/delete/{{ task.uid }}">x</a>
		</li>
	% end
	</ul>
	</br>
	%if true:
		<form action="/add_task" method='post'>
		<input name="description" type="text" placeholder="Невозможно добавить задачу" disabled/>
		<button type="submit">+</button>
	%else:
		<form action="/add_task" method='post'>
		<input name="description" type="text" placeholder="Добавить задачу"/>
		<button type="submit">+</button>
	</div>
	% end
	<div>
		<p class="line">Всего задач: {{ total_tasks }}, не выполнено: {{ incomplete }}</p>
	</div>
</div
</body>
</html>
