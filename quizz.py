import marimo

__generated_with = "0.10.9"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md("""# Mines AP 2024-2025 Groupe 6 - Quizz 5""")
    return


@app.cell
def _(mo):
    mo.md("""## Question 1""")
    return


@app.cell(hide_code=True)
def _(mo):
    widget_1 = mo.ui.code_editor(
    value = 
    """class HelloAlarm(Alarm):
        # 🚧 TODO!
        pass

    HelloAlarm(delay=5.0)
    """    
    )

    comments_1 = mo.ui.text_area(debounce=False)

    mo.md(f'''
    On vous fournit une classe `Alarm` (que vous n'avez pas le droit de modifier) qui est définie comme suit :

    ```python
    import time 

    class Alarm():
        def __init__(self, delay):
            time.sleep(delay)
            self.action()
        def action(self):
            pass
    ```

    Complétez la classe `HelloAlarm` afin que le code suivant affiche "Hello! 👋" après 5 secondes.

    Votre code:

    {widget_1}

    Commentaires:

    {comments_1}
    ''')
    return comments_1, widget_1


@app.cell
def _(mo):
    mo.md("""## Question 2""")
    return


@app.cell(hide_code=True)
def _(mo):
    widget_2 = mo.ui.code_editor(value='''\
    class B(A):
        def __init__(self, x, y):
            self.x = x 🚧 TODO: improve this line
            self.y = y
        def print_attrs(self):
            print(f"x = {self.x}") 🚧 TODO: improve this line
            print(f"y = {self.y}")
    ''')

    comments_2 = mo.ui.text_area(debounce=False)

    mo.md(f'''

    On définit la classe

    ```python
    class A:
        def __init__(self, x):
            self.x = x
        def print_attrs(self):
            print(f"x = {{self.x}}")
    ```

    Quelqu'un vous fournit ensuite la classe `B` suivante :

    ```python
    class B(A):
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def print_attrs(self):
            print(f"x = {{self.x}}")
            print(f"y = {{self.y}}")
    ```

    Pouvez-vous modifier l'implémentation de la classe `B` (à fonctionnalités constantes) en réduisant la duplication de code entre `A` et `B` ?


    Votre code:
    {widget_2}

    Commentaires:

    {comments_2}
    ''')
    return comments_2, widget_2


@app.cell(hide_code=True)
def _(mo):
    widget_3 = mo.ui.array([mo.ui.checkbox()] * 4)
    comments_3 = mo.ui.text_area(debounce=False)


    mo.md(f"""## Question 3

    La bibliothèque Python [Flet](https://flet.dev/) donne dans sa documentation un exemple de création de bouton personnalisé :

    ```python
    import flet as ft

    class MyButton(ft.ElevatedButton)
        def __init__(self, text):
            super().__init__()
            self.bgcolor = ft.Colors.ORANGE_300
            self.color = ft.Colors.GREEN_800
            self.text = text  

    button = MyButton()
    ```

    Quelles assertions sont vraies ?


     - {widget_3[0]} `type(button) == ft.ElevatedButton`

     - {widget_3[1]} `type(button) == MyButton`

     - {widget_3[2]} `isinstance(button, ft.ElevatedButton)`

     - {widget_3[3]} `isinstance(button, MyButton)`

    Commentaires :

    {comments_3}


    """)
    return comments_3, widget_3


@app.cell
def _(mo):
    mo.md("""## Validation""")
    return


@app.cell(hide_code=True)
def _():
    import pprint
    import urllib
    return pprint, urllib


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(
    comments_1,
    comments_2,
    comments_3,
    pprint,
    widget_1,
    widget_2,
    widget_3,
):
    widgets = [widget_1, widget_2, widget_3]
    comments = [comments_1, comments_2, comments_3]
    answer = pprint.pformat([
        {f"Question {i+1}": widget.value, f"Comment {i+1}": comment.value} for i, (widget, comment) in enumerate(zip(widgets, comments))
    ], indent=4)
    return answer, comments, widgets


@app.cell(hide_code=True)
def _(mo):
    autosave = mo.ui.checkbox(label="Sauvegarde automatique dans le fichier answer.py", value=True)
    autosave
    return (autosave,)


@app.cell(hide_code=True)
def _(answer, autosave):
    if autosave.value:
        with open("answer.py", mode="tw", encoding="utf-8") as file:
            file.write(answer)
    return (file,)


@app.cell(hide_code=True)
def _(answer, mo, urllib):
    to = "Sebastien.Boisgerault@minesparis.psl.eu"
    subject = "Quizz AP #5"
    body = answer

    q = urllib.parse.quote


    mailto = f"mailto:{to}?subject={q(subject)}&body={q(body)}"


    mo.vstack(
        [
            mo.md(f"""
    Envoyez le texte suivant à {mo.icon('lucide:mail')} `Sebastien.Boisgerault@minesparis.psl.eu`
    ```python
    {answer}
    ```
    """),
            mo.Html(f"""
    <div>
      <style>
        #send {{
          text-decoration: none;
          background-color: #EEEEEE;
          color: #333333;
          padding: 2px 6px 2px 6px;
          border-top: 1px solid #CCCCCC;
          border-right: 1px solid #333333;
          border-bottom: 1px solid #333333;
          border-left: 1px solid #CCCCCC;
        }}
        </style>
        <a id="send" href="{mailto}">Envoyez votre réponse</a>
    <div>
    """),
        ]
    )
    return body, mailto, q, subject, to


if __name__ == "__main__":
    app.run()
