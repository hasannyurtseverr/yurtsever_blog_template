# from test import db, Human

# CREATE
# db.create_all()
# human1 = Human ('Hasan', 23)
# human2 = Human('Ecra',22)

# db.session.add_all([human1,human2])
# db.session.commit()

# print(human1.id)
# print(human2.id)


# READ
# all_human = Human.query.all()
# print(all_human)

# all_human = Human.query.get(3)
# print(all_human.name)

# UPDATE
# first = Human.query.get(1)
# first.age = 100
# db.session.add(first)
# db.session.commit()
# print(first.age)


# DELETE
# sec_human = Human.query.get(2)
# db.session.delete(sec_human)
# db.session.commit()
# print(Human.query.get(2))