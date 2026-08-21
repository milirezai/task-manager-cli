from main import App

operation = int(input('things you can do badly: \n 1 - create task \n 2 - list task \n 3 - search task \n 4 - update task \n 5 - complecte task \n 6 - delete task \n 7 - close \n     ')) 

App(operation).run()