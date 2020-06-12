from app import models, app, views


def init_db():
    # Create all tables
    models.db.create_all()

    bank = [
        ('Beijing Bank', 'Beijing', 0.0),
        ('Shanghai Bank', 'Shanghai', 0.0),
        ('Hefei Bank', 'Hefei', 0.0),
        ('Nanjing Bank', 'Nanjing', 0.0)
    ]
    staff = [
        ('staff_1', '大司马', '13312312345', '芜湖市起飞区', '2012-08-17', 'depart_1'),
        ('staff_2', '李姐', '13323323333', '理解市李姐万岁', '2019-08-31', 'depart_3'),
        ('staff_3', '韩金龙', '13323311451', '这波市肉弹冲击', '2020-01-31', 'depart_5'),
        ('staff_4', '神魔恋', '17344455555', '李在赣神魔市', '2020-01-01', 'depart_2'),
        ('staff_5', '小王', '18912345678', '北京市海淀区', '2018-01-31', 'depart_4'),
        ('staff_6', '小李', '13012345678', '合肥市包河区', '2018-02-28', 'depart_2'),
        ('staff_7', '小郭', '18900011100', '合肥市蜀山区', '2018-10-31', 'depart_3'),
        ('staff_8', '小史', '18912321232', '广东省深圳市', '2000-01-31', 'depart_3')
    ]

    department = [
        ('depart_1', '市场部', '普通', 'staff_1', 'Beijing Bank'),
        ('depart_2', '市场部', '普通', 'staff_2', 'Beijing Bank'),
        ('depart_3', '市场部', '特殊', 'staff_3', 'Shanghai Bank'),
        ('depart_4', '人事部', '普通', 'staff_4', 'Nanjing Bank'),
        ('depart_5', '人事部', '普通', 'staff_5', 'Hefei Bank')
    ]

    manager = [
        ('staff_1', 'depart_1'),
        ('staff_2', 'depart_2'),
        ('staff_3', 'depart_3'),
        ('staff_4', 'depart_4'),
        ('staff_5', 'depart_5'),
    ]

    # add Banks
    for item in bank:
        models.db.session.add(models.SubBank(*item))
    # add Staffs without foreign key
    for item in staff:
        models.db.session.add(models.Staff(*item[:-1]))
    # add department without foreign key
    for item in department:
        models.db.session.add(models.Department(*item[:-2]))
    models.db.session.commit()

    # add foreign key
    for item in manager:
        models.db.session.add(models.Manager(*item))
    models.db.session.commit()
    for item in staff:
        result = models.Staff.query.filter(models.Staff.s_identity_code == item[0]).first()
        result.s_d_code = item[-1]
        models.db.session.commit()

    for item in department:
        result = models.Department.query.filter(models.Department.d_code == item[0]).first()
        result.d_m_identity_code = item[-2]
        result.d_sb_name = item[-1]
        models.db.session.commit()


if __name__ == '__main__':
    # init_db()
    app.app.run(debug=True)
