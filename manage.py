import click
from sqlalchemy import insert

from app.models import Base
from app.session import engine


@click.group()
def cli():
    pass


@click.command()
@click.option('--host', default="0.0.0.0", help='Host name')
@click.option('--port', default=8000, help='Port')
def runserver(host, port):
    import uvicorn
    from app.main import app
    uvicorn.run(app, host=host, port=port)


@click.command()
def initdb():
    click.echo('Initialized the database')
    with engine.begin() as connection:
        Base.metadata.create_all(connection)
    click.echo('Finished!')


@click.command()
def populatedb():
    from app.models.api import TodoItem
    click.echo('Populating the database')
    with engine.begin() as connection:
        with connection.begin():
            for i in range(10_000):
                connection.execute(insert(TodoItem), dict(title=f"Input {i}", text="example_data", done=False))
    click.echo('Finished!')


@click.command()
def dropdb():
    click.echo('Dropped the database')
    with engine.begin() as connection:
        Base.metadata.drop_all(connection)
    click.echo('Finished!')


cli.add_command(runserver)
cli.add_command(initdb)
cli.add_command(populatedb)
cli.add_command(dropdb)

if __name__ == "__main__":
    cli()
