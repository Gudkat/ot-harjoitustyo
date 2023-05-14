from invoke import task


@task
def start(ctx):
    ctx.run("python3 python-study-grouper/src/index.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest python-study-grouper/src/", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest python-study-grouper/src/", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task
def lint(ctx):
    ctx.run("pylint python-study-grouper/src", pty=True)
