import datetime
from typing import Optional
from sqlalchemy import Integer, String, MetaData, create_engine, select, types
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

engine = create_engine("sqlite:///coffeebot.db", echo=True)
metadata_obj = MetaData()

class Base(DeclarativeBase):
    pass

# More information: https://docs.sqlalchemy.org/en/20/orm/mapping_styles.html#declarative-mapping
class CoffeeEvent(Base):
    __tablename__ = "coffeebotLog"

    # More information: https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#using-annotated-declarative-table-type-annotated-forms-for-mapped-column
    Timestamp: Mapped[int] = mapped_column(Integer, primary_key= True)
    State: Mapped[str] = mapped_column(String)
    # Power: Mapped[float] = mapped_column(default = 0.0)
    Power: Mapped[Optional[float]] = mapped_column(nullable=True)


    def __repr__(self) -> str:
        return f"CoffeeEvent(Timestamp={self.Timestamp!r}, State={self.State!r}, Power={self.Power!r})"
        
class Database:
    def __init__(self):
        # self.useSlack = os.environ['USE_SLACK']
        Base.metadata.create_all(engine)
        return

    def insert(self, state: String, power: float):
        timey = int(datetime.datetime.timestamp(datetime.datetime.now()))
        row = CoffeeEvent(Timestamp = timey, State = state)
        latestEvent: CoffeeEvent = self.selectLatest()
        
        if(latestEvent.State == state):
            print(r'State is NONE or already saved in database.')
            return
        else:
            with Session(engine) as session:
                session.add(row)
                session.commit()
                return

    def selectLatest(self) -> CoffeeEvent:
        with Session(engine) as session:
            latestEvent: CoffeeEvent = session.scalars(select(CoffeeEvent).order_by(CoffeeEvent.Timestamp.desc())).first()
            
            if latestEvent == None:
                a = CoffeeEvent()
                a.State = 'foo'
                return a

            return latestEvent