Если я всё правильно понял, то можно добавить данную функция, дабы проверить находится ли обращение в обработке в данный момент.

	if (request.state != 'inprogress')
		request.state = 'inprogress'
		request.assignee = login
		request.version += 1
		request_data.upload(request) // загружаем новую версию обращения в БД (старая не удаляется)


Но если стоит вопрос, чтобы обращение от одного человека обрабатывался одним менджером, то можно сделать вот так.

	if (request.state != 'inprogress' && requests.assignee = login)
		request.state = 'inprogress'
		request.assignee = login
		request.version += 1
		request_data.upload(request) // загружаем новую версию обращения в БД (старая не удаляется)

Возможно я ошибаюсь, но язык очень похож на python и изучить его не составит труда.