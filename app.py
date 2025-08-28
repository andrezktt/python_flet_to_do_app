import flet as ft

class Task(ft.Column):
    def __init__(self, task_name, task_delete):
        super().__init__()
        self.task_name = task_name
        self.task_delete = task_delete
        self.display_task = ft.Checkbox(value=False, label=self.task_name)
        self.edit_name = ft.TextField(expand=1)
        
        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.CREATE_OUTLINED,
                            tooltip='Edit To-do',
                            on_click=self.edit_task
                        ),
                        ft.IconButton(
                            icon=ft.Icons.DELETE_OUTLINE,
                            tooltip='Delete To-do',
                            on_click=self.delete_task
                        )
                    ]
                )
            ]
        )
        
        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.Icons.DONE_OUTLINE_OUTLINED, 
                    icon_color=ft.Colors.GREEN, 
                    tooltip='Update To-do', 
                    on_click=self.save_task
                )
            ]
        )
        self.controls = [self.display_view, self.edit_view]
        
    def edit_task(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()
        
    def save_task(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()
    
    def delete_task(self, e):
        self.task_delete(self)

class TodoApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(hint_text="What's needs to be done?", expand=True)
        self.tasks = ft.Column()
        self.controls = [
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=self.add_task)
                ],
            ),
            self.tasks
        ]
        
    def add_task(self, e):
        task = Task(task_name=self.new_task.value, task_delete=self.task_delete)
        self.tasks.controls.append(task)
        self.new_task.value = ''
        self.update()
        
    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()
            

def main(page:ft.Page):
    page.title = 'To-Do Flet'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()
    
    todo = TodoApp()
    
    page.add(todo)

ft.app(target=main)