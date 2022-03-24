from Tutorial import User, Session, engine

local_session = Session(bind=engine)

user_to_update = local_session.query(User).filter(User.username == "Jona").first

user_to_update.username = "jonathan"
user_to_update.email = "jonathan@company.com"

local_session.commit()
