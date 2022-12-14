import sqlalchemy
from sqlalchemy import Integer, String, Time, MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
import datetime

engine = create_engine("sqlite:///coffeebot.db", echo=True)
metadata_obj = MetaData()

class Base(DeclarativeBase):
    pass

class CoffeeEvent(Base):
    __tablename__ = "coffeebotLog"

    Id: Mapped[int] = mapped_column(primary_key=True)
    Number: Mapped[int] = mapped_column(Integer)
    Unit: Mapped[str] = mapped_column(String)
    Timestamp: Mapped[int] = mapped_column(Integer)

    def __repr__(self) -> str:
        return f"CoffeeEvent(Id={self.Id!r}, Number={self.Number!r}, Unit={self.Unit!r}, Timestamp={self.Timestamp!r})"
        
class Database:
    def __init__(self):
        # load_dotenv('.env')
        # self.useSlack = os.environ['USE_SLACK']
        return

    def helloWorld(self) -> None:
        with engine.connect() as conn:
            result = conn.execute(sqlalchemy.text("select 'hello world'"))
            print(result.all())

    def createDatabase(self) -> None:
        # metadata_obj.create_all(engine, checkfirst=True)
        Base.metadata.create_all(engine)

    def showTables(self) -> None:
        for t in metadata_obj.sorted_tables:
            print("Tables: " + t.name)

        # for c in coffebotLog.c:
            # print(c)

    def insert(self, number, unit):
        timey = int(datetime.datetime.timestamp(datetime.datetime.now()))
        row = CoffeeEvent(Number = number, Unit = unit, Timestamp = timey)
        with Session(engine) as session:
            session.add(row)
            session.commit()
            return