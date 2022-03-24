from Tutorial import User, Session, engine


users = [
    {
        "username": "jerry",
        "email": "jerry@company.com"
    },
    {
        "username": "jordan",
        "email": "jordan@company.com"
    },
    {
        "username": "maria",
        "email": "maria@company.com"
    },
    {
        "username": "pedro",
        "email": "pedro@company.com"
    },
    {
        "username": "nikolas",
        "email": "nikolas@company.com"
    }
]

local_session = Session(bind=engine)

# new_user = User(username="Jona", email="jona@company.com")
# local_session.add(new_user)
# local_session.commit()

for u in users:
    new_user = User(username=u["username"], email=u["email"])
    local_session.add(new_user)
    local_session.commit()