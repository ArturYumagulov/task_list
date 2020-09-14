<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Список задач</title>
	<link rel="stylesheet" href="static/style.css"
</head>
<body>
<div class="container">
	<div class="row">
		<h1>Список задач</h1>
		<ul class="todo-list"></ul>
		% for task in tasks:
		<li><input class="checkbox" type="checkbox"/>{{ task.desc }}
		<a class="remove" id="remove" href="#">x</a></li>
		% end
	</br>
	<form class="add">
	<input type="text" placeholder="Добавить задачу"/>
	<button type="submit">Add</button>
	</div>
</div>
</body>
</html>
