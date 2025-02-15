import pandas as pd


df = pd.read_csv("titanic.csv")
print(df.head())

# วิธีการเรียกดูค่าใน Column
# df["Survived"]
# df.Survived

df.info()

PassengerId_not_null = df.Age.notnull()
dq_PassengerId = PassengerId_not_null.sum() / len(PassengerId_not_null)
print(f"Data Quality of PassengerId: {dq_PassengerId}")

Survived_not_null = df.Age.notnull()
dq_Survived = Survived_not_null.sum() / len(Survived_not_null)
print(f"Data Quality of Survived: {Survived_not_null}")

Pclass_not_null = df.Age.notnull()
dq_Pclass = Pclass_not_null.sum() / len(Pclass_not_null)
print(f"Data Quality of Pclass: {dq_Pclass}")

Name_not_null = df.Age.notnull()
dq_Name = Name_not_null.sum() / len(Name_not_null)
print(f"Data Quality of PName: {dq_Name}")

Sex_not_null = df.Age.notnull()
dq_Sex = Sex_not_null.sum() / len(Sex_not_null)
print(f"Data Quality of Sex: {dq_Sex}")

age_not_null = df.Age.notnull()
dq_age = age_not_null.sum() / len(age_not_null)
print(f"Data Quality of Age: {dq_age}")

SibSp_not_null = df.Age.notnull()
dq_SibSp = SibSp_not_null.sum() / len(SibSp_not_null)
print(f"Data Quality of SibSp: {dq_SibSp}")

Parch_not_null = df.Age.notnull()
dq_Parch = Parch_not_null.sum() / len(Parch_not_null)
print(f"Data Quality of arch: {dq_Parch}")

Ticket_not_null = df.Age.notnull()
dq_Ticket = Ticket_not_null.sum() / len(Ticket_not_null)
print(f"Data Quality of Ticket: {dq_Ticket}")

Fare_not_null = df.Age.notnull()
dq_Fare = Fare_not_null.sum() / len(Fare_not_null)
print(f"Data Quality of Fare: {dq_Fare}")

cabin_not_null = df.Cabin.notnull()
dq_cabin = cabin_not_null.sum() / len(cabin_not_null)
print(f"Data Quality of Cabin: {dq_cabin}")

embarked_not_null = df.Embarked.notnull()
dq_embarked = embarked_not_null.sum() / len(embarked_not_null)
print(f"Data Quality of Embarked: {dq_embarked}")

print(f"Completeness: {(dq_PassengerId + dq_Survived + dq_Pclass + dq_Name + dq_Sex + dq_age + dq_SibSp + dq_Parch + dq_Ticket + dq_Fare + dq_cabin + dq_embarked) / 11}")