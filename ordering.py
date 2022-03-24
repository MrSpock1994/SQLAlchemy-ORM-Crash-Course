from Tutorial import User, Session, engine
from sqlalchemy import desc
local_session = Session(bind=engine)

# ascending order

users = local_session.query(User).order_by(User.username).all()

for user in users:
    print(user.username)

# descending order

users_desc = local_session.query(User).order_by(desc(User.username)).all()

for user in users_desc:
    print(user.username)

