import uvicorn

from app import models, api


Login = api.app

"""@app.post("/personnes/", response_model=personne_schema.Personne)
def create_user_compte_endpoint(personne: personne_schema.PersonneCreate, db: Session = Depends(get_db)):
    print("end point")
    print(type(crud))
    return crud.create_personne(db=db, personne=personne)"""

"""@app.post("/user_comptes/", response_model=user_compte_schema.UserCompte)
def create_user_compte(user_compte: user_compte_schema.UserCompteCreate, personne_id: int, db: Session = Depends(get_db)):
    return crud_user_compte.create_user_compte(db=db, user_compte=user_compte, personne_id=personne_id)
"""

if __name__ == "__main__":
    print("main")
    uvicorn.run("main:Login", host="0.0.0.0", port=8000, reload = True)# workers=4)




