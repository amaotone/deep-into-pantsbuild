from invoke import task


@task
def hello(c, name=""):
    if name:
        print(f"hello, {name}")
    else:
        print("hello, world!")


if __name__ == "__main__":
    from invoke import Collection, Program

    ns = Collection()
    ns.add_task(hello, name="hello")
    program = Program(namespace=ns)
    program.run()
