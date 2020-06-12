from flask_sqlalchemy import SQLAlchemy
from .app import app

# database instance
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/bank"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



# begin models
# name rules of all fields: The uppercase char in model name concat attribute name
# e.g. model 'Customer' attribute 'identity_code' is named as 'c_identity_code'
# note: the name in class is Big-Camel-Case, and in sql table is underline

IDENTITY_CODE_LEN = 256
NAME_LEN = 256
PHONE_LEN = 256
ADDRESS_LEN = 256
EMAIL_LEN = 256
RELATIONSHIP_LEN = 256
CODE_LEN = 256
CITY_LEN = 256
TYPE_LEN = 256


class Customer(db.Model):
    # start attributes
    c_identity_code = db.Column(db.String(IDENTITY_CODE_LEN), primary_key=True)
    c_name = db.Column(db.String(NAME_LEN), nullable=False)
    c_phone = db.Column(db.String(PHONE_LEN), nullable=False)
    c_address = db.Column(db.String(ADDRESS_LEN), nullable=False)
    c_contact_name = db.Column(db.String(IDENTITY_CODE_LEN), nullable=False)
    c_contact_phone = db.Column(db.String(NAME_LEN), nullable=False)
    c_contact_email = db.Column(db.String(EMAIL_LEN), nullable=False)
    c_contact_relationship = db.Column(db.String(RELATIONSHIP_LEN), nullable=False)
    # end attributes

    # start foreign keys
    c_loan_staff_identity_code = db.Column(
        db.String(IDENTITY_CODE_LEN),
        db.ForeignKey('staff.s_identity_code'),
        nullable=False
    )
    c_account_staff_identity_code = db.Column(
        db.String(IDENTITY_CODE_LEN),
        db.ForeignKey('staff.s_identity_code'),
        nullable=False
    )
    # end foreign keys

    def __init__(self, id, name, phone, address, c_name, c_phone, c_email, c_relationship, loan_staff=None, account_staff=None):
        self.c_identity_code = id
        self.c_name = name
        self.c_phone = phone
        self.c_address = address
        self.c_contact_name = c_name
        self.c_contact_email = c_email
        self.c_contact_phone = c_phone
        self.c_contact_relationship = c_relationship
        if loan_staff is not None:
            self.c_loan_staff_identity_code = loan_staff
        if account_staff is not None:
            self.c_account_staff_identity_code = account_staff
    pass


class Staff(db.Model):
    # start attributes
    s_identity_code = db.Column(db.String(IDENTITY_CODE_LEN), primary_key=True)
    s_name = db.Column(db.String(NAME_LEN), nullable=False)
    s_phone = db.Column(db.String(PHONE_LEN), nullable=False)
    s_address = db.Column(db.String(ADDRESS_LEN), nullable=False)
    s_start_work_date = db.Column(db.Date, nullable=False)
    # end attributes

    # start foreign keys
    s_d_code = db.Column(
        db.String(CODE_LEN),
        db.ForeignKey('department.d_code'),
        nullable=True
    )
    # end foreign keys

    def __init__(self, id, name, phone, address, start_work_date, department_id=None):
        self.s_identity_code = id
        self.s_name = name
        self.s_phone = phone
        self.s_address = address
        self.s_start_work_date = start_work_date
        if department_id is not None:
            self.s_d_code = department_id
    pass


class SubBank(db.Model):
    # start attributes
    sb_name = db.Column(db.String(NAME_LEN), primary_key=True)
    sb_city = db.Column(db.String(CITY_LEN), nullable=False)
    sb_assets = db.Column(db.Float, nullable=False)
    # end attributes

    # start foreign keys
    # no foreign key
    # end foreign keys

    def __init__(self, name, city, assets):
        self.sb_name = name
        self.sb_city = city
        self.sb_assets = assets

    pass


class Department(db.Model):
    # start attributes
    d_code = db.Column(db.String(CODE_LEN), primary_key=True)
    d_name = db.Column(db.String(NAME_LEN), nullable=False)
    d_type = db.Column(db.String(TYPE_LEN), nullable=False)
    # end attributes

    # start foreign keys
    d_m_identity_code = db.Column(
        db.String(IDENTITY_CODE_LEN),
        db.ForeignKey('manager.m_identity_code'),
        nullable=True
    )
    d_sb_name = db.Column(
        db.String(NAME_LEN),
        db.ForeignKey('sub_bank.sb_name'),
        nullable=True
    )
    # end foreign keys

    def __init__(self, id, name, type, m_id=None, sb_name=None):
        self.d_code = id
        self.d_name = name
        self.d_type = type
        if m_id is not None:
            self.d_m_identity_code = m_id
        if sb_name is not None:
            self.d_sb_name = sb_name

    pass


class Manager(db.Model):
    # start attributes
    m_identity_code = db.Column(
        db.String(IDENTITY_CODE_LEN),
        db.ForeignKey('staff.s_identity_code'),
        primary_key=True)
    # end attributes

    # start foreign keys
    m_d_code = db.Column(
        db.String(CODE_LEN),
        db.ForeignKey('department.d_code'),
        nullable=True
    )
    # end foreign keys

    def __init__(self, id, d_id=None):
        self.m_identity_code = id
        if d_id is not None:
            self.m_d_code = d_id

    pass


class Account(db.Model):
    # start attributes
    a_code = db.Column(db.String(CODE_LEN), primary_key=True)
    a_balance = db.Column(db.Float, nullable=False)
    a_open_date = db.Column(db.Date, nullable=False)
    # end attributes

    # start foreign keys
    # no foreign keys
    # end foreign keys

    def __init__(self, id, balance, open_date):
        self.a_code = id
        self.a_balance = balance
        self.a_open_date = open_date

    pass


class CheckingAccount(db.Model):
    # start attributes
    ca_credit = db.Column(db.Float, nullable=False)
    # end attributes

    # start foreign keys
    ca_a_code = db.Column(
        db.String(CODE_LEN),
        db.ForeignKey('account.a_code'),
        primary_key=True
    )
    # end foreign keys

    def __init__(self, credit, a_id):
        self.ca_credit = float(credit)
        self.ca_a_code = a_id

    pass


class SavingsAccount(db.Model):
    # start attributes
    sa_rate = db.Column(db.Float, nullable=False)
    sa_currency_type = db.Column(db.String(TYPE_LEN), nullable=False)
    # end attributes

    # start foreign keys
    sa_a_code = db.Column(
        db.String(CODE_LEN),
        db.ForeignKey('account.a_code'),
        primary_key=True
    )
    # end foreign keys

    def __init__(self, rate, c_type, a_id):
        self.sa_rate = float(rate)
        self.sa_currency_type = c_type
        self.sa_a_code = a_id

    pass


class Loan(db.Model):
    # start attributes
    l_code = db.Column(db.String(CODE_LEN), primary_key=True)
    l_money = db.Column(db.Float, nullable=False)
    # end attributes

    # start foreign keys
    l_sb_name = db.Column(
        db.String(NAME_LEN),
        db.ForeignKey('sub_bank.sb_name'),
        nullable=True
    )
    # end foreign keys

    def __init__(self, id, money, sb_name=None):
        self.l_code = id
        self.l_money = money
        if sb_name is not None:
            self.l_sb_name = sb_name

    pass


class LoanPayment(db.Model):
    # start attributes
    lp_code = db.Column(db.String(CODE_LEN), primary_key=True)
    lp_date = db.Column(db.Date, nullable=False)
    lp_money = db.Column(db.Float, nullable=False)
    # end attributes

    # start foreign keys
    lp_l_code = db.Column(
        db.String(CODE_LEN),
        db.ForeignKey('loan.l_code'),
        primary_key=True
    )
    # end foreign keys

    def __init__(self, lp_id, lp_date, lp_money, l_id):
        self.lp_code = lp_id
        self.lp_date = lp_date
        self.lp_money = lp_money
        self.lp_l_code = l_id

    pass


class CheckingAccountRecord(db.Model):
    # start attributes
    car_last_visit_time = db.Column(db.Date, nullable=True)
    # end attributes

    # start foreign keys
    car_c_identity_code = db.Column(
        db.String(IDENTITY_CODE_LEN),
        db.ForeignKey('customer.c_identity_code'),
        primary_key=True
    )
    car_sb_name = db.Column(
        db.String(NAME_LEN),
        db.ForeignKey('sub_bank.sb_name'),
        primary_key=True
    )
    car_a_code = db.Column(
        db.String(CODE_LEN),
        db.ForeignKey('account.a_code'),
        nullable=True
    )
    # end foreign keys

    def __init__(self, c_id, sb_name, a_id, la):
        self.car_c_identity_code = c_id
        self.car_sb_name = sb_name
        self.car_a_code = a_id
        self.car_last_visit_time = la

    pass


class SavingsAccountRecord(db.Model):
    # start attributes
    sar_last_visit_time = db.Column(db.Date, nullable=True)
    # end attributes

    # start foreign keys
    sar_c_identity_code = db.Column(
        db.String(IDENTITY_CODE_LEN),
        db.ForeignKey('customer.c_identity_code'),
        primary_key=True
    )
    sar_sb_name = db.Column(
        db.String(NAME_LEN),
        db.ForeignKey('sub_bank.sb_name'),
        primary_key=True
    )
    sar_a_code = db.Column(
        db.String(CODE_LEN),
        db.ForeignKey('account.a_code'),
        nullable=True
    )
    # end foreign keys

    def __init__(self, c_id, sb_name, a_id, la):
        self.sar_c_identity_code = c_id
        self.sar_sb_name = sb_name
        self.sar_a_code = a_id
        self.sar_last_visit_time = la


    pass


class LoanCustomer(db.Model):
    # start attributes

    # end attributes

    # start foreign keys
    lc_l_code = db.Column(
        db.String(CODE_LEN),
        db.ForeignKey('loan.l_code'),
        primary_key=True
    )
    lc_c_identity_code = db.Column(
        db.String(IDENTITY_CODE_LEN),
        db.ForeignKey('customer.c_identity_code'),
        primary_key=True
    )
    # end foreign keys

    def __init__(self, l_id, c_id):
        self.lc_l_code = l_id
        self.lc_c_identity_code = c_id

    pass

# end models


if __name__ == '__main__':
    pass

