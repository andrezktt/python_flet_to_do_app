import flet as ft

def main(page:ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = 'To-Do Flet'
    
    def add_clicked(e):
        task_view.controls.append(ft.Checkbox(label=new_task.value))
        new_task.value = ''
        page.update()
        
    new_task = ft.TextField(hint_text="What's needs to be done?")
    task_view = ft.Column()
    view = ft.Column(
        width=600,
        controls=[
            ft.Row(
                controls=[
                    new_task,
                    ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_clicked)
                ],
            ),
            task_view
        ]
    )

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view)

ft.app(target=main)