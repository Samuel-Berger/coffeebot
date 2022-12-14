import sqlalchemy
engine = sqlalchemy.create_engine("sqlite:///coffeebot.db")

class Database:
    def __init__(self):
        # load_dotenv('.env')
        # self.useSlack = os.environ['USE_SLACK']
        return

    def helloWorld(self) -> None:
        with engine.connect() as conn:
            result = conn.execute(sqlalchemy.text("select 'hello world'"))
            print(result.all())