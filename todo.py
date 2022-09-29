import flet
from flet import Checkbox, FloatingActionButton, Page, TextField, icons, Column, Row

def main(page: Page):

    def add_clicked(e):
        tasks_view.controls.append(Checkbox(label=new_task.value))
        new_task.value=''
        page.update()

    new_task = TextField(hint_text='O que deve ser feito?', expand=True)
    tasks_view = Column()
    view = Column(
        width=600,
        controls=[
            Row(
                controls=[
                    new_task,
                    FloatingActionButton(icon=icons.ADD, on_click=add_clicked),
                ],
            ),
            tasks_view,
        ],
    )

    page.horizontal_alignment = 'center'
    page.add(view)

flet.app(target=main, port=8000, route_url_strategy='path')