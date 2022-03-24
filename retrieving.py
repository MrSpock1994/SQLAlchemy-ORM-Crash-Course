from Tutorial import User, Session, engine

local_session = Session(bind=engine)

users = local_session.query(User).all()

for user in users:
    print(user.username)
    print(user.email)


# Query for one object

jona = local_session.query(User).filter(User.username == "Jona").first()

print(jona)