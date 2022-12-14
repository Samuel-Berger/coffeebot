import datetime
from sqlalchemy import Integer, String, MetaData, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

engine = create_engine("sqlite:///coffeebot.db", echo=True)
metadata_obj = MetaData()

class Base(DeclarativeBase):
    pass

class CoffeeEvent(Base):
    __tablename__ = "coffeebotLog"

    Timestamp: Mapped[int] = mapped_column(Integer, primary_key= True)
    State: Mapped[str] = mapped_column(String)

    def __repr__(self) -> str:
        return f"CoffeeEvent(Timestamp={self.Timestamp!r}, State={self.State!r})"
        
class Database:
    def __init__(self):
        # load_dotenv('.env')
        # self.useSlack = os.environ['USE_SLACK']
        return

    def createDatabase(self) -> None:
        Base.metadata.create_all(engine)

    def insert(self, state: String):
        timey = int(datetime.datetime.timestamp(datetime.datetime.now()))
        row = CoffeeEvent(Timestamp = timey, State = state)
        
        with Session(engine) as session:
            # stmt = select(CoffeeEvent).order_by(CoffeeEvent.c.Timestamp.desc).first
            # stmt = session.scalars(select(CoffeeEvent())).first()
            # print(stmt)
            session.add(row)
            session.commit()
            return