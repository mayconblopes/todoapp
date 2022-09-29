import flet
from flet import Checkbox, FloatingActionButton, Page, TextField, icons, Column, Row, UserControl

class TodoApp(UserControl):
    def build(self):
        self.new_task = TextField(hint_text='O que deve ser feito?', expand=True)
        self.tasks = Column()

        # app's root control
        root = Column(
            width=375,
            height=667,
            controls=[
                Row(
                    controls=[
                        self.new_task,
                        FloatingActionButton(icon=icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                self.tasks,
            ],
        )

        return root

    def add_clicked(self, e):
        self.tasks.controls.append(Checkbox(label=self.new_task.value))
        self.new_task.value = '' 
        self.update()

def main(page: Page):
    page.title = 'ToDo App'
    page.horizontal_alignment = 'center'
    page.update()

    todo = TodoApp()

    page.add(todo)

flet.app(target=main, port=8000, route_url_strategy='path')