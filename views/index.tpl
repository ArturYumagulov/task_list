<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Список задач</title>
	<link rel="stylesheet" href="static/style.css">
	<script src="http://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
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
			<a class="remove" id="remove" href="#">x</a></li>
		%else:
			<li>
			<input class="checkbox" data-uid="{{ task.uid }}" type="checkbox">
		% end
		{{ task }}
		<a class="remove" href="api/delete/{{ task.uid }}">x</a>
		<hr/>
		</li>
	% end
	</ul>
	</br>
	<form action="/add_task" method='post'>
		<input name="description" type="text" placeholder="Добавить задачу"/>
	<button type="submit">+</button>
	</div>
</div
</body>
</html>
