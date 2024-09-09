from cx_Freeze import setup, Executable

executables = [Executable("snake.py")]

setup(
    name="snake",
    version="1.0",
    description="Um jogo da cobrinha feito em Python",
    executables=executables
)
