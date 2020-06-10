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

IDENTITY_CODE_LEN = 18
NAME_LEN = 20
PHONE_LEN = 13
ADDRESS_LEN = 256
EMAIL_LEN = 20
RELATIONSHIP_LEN = 15
CODE_LEN = 30
CITY_LEN = 15
TYPE_LEN = 10


class Customer(db.Model):
    # start attributes
    c_identity_code = db.Column(db.String(IDENTITY_CODE_LEN), primary_key=True)
    c_name = db.Column(db.String(NAME_LEN), nullable=True)
    c_phone = db.Column(db.String(PHONE_LEN), nullable=True)
    c_address = db.Column(db.String(ADDRESS_LEN), nullable=True)
    c_contact_name = db.Column(db.String(IDENTITY_CODE_LEN), nullable=True)
    c_contact_phone = db.Column(db.DECIMAL(NAME_LEN), nullable=True)
    c_contact_email = db.Column(db.String(EMAIL_LEN), nullable=True)
    c_contact_relationship = db.Column(db.String(RELATIONSHIP_LEN), nullable=True)
    # end attributes

    # start foreign keys
    c_loan_staff_identity_code = db.Column(
        db.String(IDENTITY_CODE_LEN),
        db.ForeignKey('staff.s_identity_code'),
        nullable=True
    )
    c_account_staff_identity_code = db.Column(
        db.String(IDENTITY_CODE_LEN),
        db.ForeignKey('staff.s_identity_code'),
        nullable=True
    )
    # end foreign keys
    pass


class Staff(db.Model):
    # start attributes
    s_identity_code = db.Column(db.String(IDENTITY_CODE_LEN), primary_key=True)
    s_name = db.Column(db.String(NAME_LEN), nullable=True)
    s_phone = db.Column(db.String(PHONE_LEN), nullable=True)
    s_address = db.Column(db.String(ADDRESS_LEN), nullable=True)
    s_start_work_date = db.Column(db.Date, nullable=True)
    # end attributes

    # start foreign keys
    s_d_code = db.Column(
        db.String(CODE_LEN),
        db.ForeignKey('department.d_code'),
        nullable=True
    )
    # end foreign keys
    pass


class SubBank(db.Model):
    # start attributes
    sb_name = db.Column(db.String(NAME_LEN), primary_key=True)
    sb_city = db.Column(db.String(CITY_LEN), nullable=True)
    sb_assets = db.Column(db.Float, nullable=True)
    # end attributes

    # start foreign keys
    # no foreign key
    # end foreign keys
    pass


class Department(db.Model):
    # start attributes
    d_code = db.Column(db.String(CODE_LEN), primary_key=True)
    d_name = db.Column(db.String(NAME_LEN), nullable=True)
    d_type = db.Column(db.String(TYPE_LEN), nullable=True)
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
    pass


class Account(db.Model):
    # start attributes
    a_code = db.Column(db.String(CODE_LEN), primary_key=True)
    a_balance = db.Column(db.Float, nullable=True)
    a_open_date = db.Column(db.Date, nullable=True)
    # end attributes

    # start foreign keys
    # no foreign keys
    # end foreign keys
    pass


class CheckingAccount(db.Model):
    # start attributes
    ca_credit = db.Column(db.Float, nullable=True)
    # end attributes

    # start foreign keys
    ca_a_code = db.Column(
        db.String(CODE_LEN),
        db.ForeignKey('account.a_code'),
        primary_key=True
    )
    # end foreign keys
    pass


class SavingsAccount(db.Model):
    # start attributes
    sa_rate = db.Column(db.Float, nullable=True)
    sa_currency_type = db.Column(db.String(TYPE_LEN), nullable=True)
    # end attributes

    # start foreign keys
    sa_a_code = db.Column(
        db.String(CODE_LEN),
        db.ForeignKey('account.a_code'),
        primary_key=True
    )
    # end foreign keys
    pass


class Loan(db.Model):
    # start attributes
    l_code = db.Column(db.String(CODE_LEN), primary_key=True)
    l_money = db.Column(db.Float, nullable=True)
    # end attributes

    # start foreign keys
    l_sb_name = db.Column(
        db.String(NAME_LEN),
        db.ForeignKey('sub_bank.sb_name'),
        nullable=True
    )
    # end foreign keys
    pass


class LoanPayment(db.Model):
    # start attributes
    lp_code = db.Column(db.String(CODE_LEN), primary_key=True)
    lp_date = db.Column(db.Date, nullable=True)
    lp_money = db.Column(db.Float, nullable=True)
    # end attributes

    # start foreign keys
    lp_l_code = db.Column(
        db.String(CODE_LEN),
        db.ForeignKey('loan.l_code'),
        primary_key=True
    )
    # end foreign keys
    pass


class CheckingAccountRecord(db.Model):
    # start attributes
    car_last_visit_time = db.Column(db.DateTime, nullable=True)
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
    pass


class SavingsAccountRecord(db.Model):
    # start attributes
    sar_last_visit_time = db.Column(db.DateTime, nullable=True)
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
    pass

# end models


if __name__ == '__main__':
    db.create_all()
