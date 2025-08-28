import flet as ft

class TodoApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(hint_text="What's needs to be done?")
        self.task_view = ft.Column()
        self.width = 600
        self.controls = [
            ft.Row(
                controls=[
                   self.new_task,
                    ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=self.add_task)
                ],
            ),
            self.task_view
        ]
        
    def add_task(self, e):
        self.task_view.controls.append(ft.Checkbox(label=self.new_task.value))
        self.new_task.value = ''
        self.update()

def main(page:ft.Page):
    page.title = 'To-Do Flet'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()
    
    todo = TodoApp()
    
    page.add(todo)

ft.app(target=main)