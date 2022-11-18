python_sources()

pex_binary(
    name="binary",
    entry_point="app.py",
    layout="packed",
    execution_mode="venv",
    platforms=[
        "current",
        "linux-x86_64-cp-39-cp39",
    ],
)

docker_image(
    name="docker",
    repository="dice_fastapi",
    instructions=[
        "FROM python:3.9-slim",
        'ENTRYPOINT ["/usr/local/bin/python", "/bin/binary.pex"]',
        "COPY src.dice_fastapi/binary.pex /bin/binary.pex",
    ],
)
